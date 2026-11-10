import os
import sys
import time
import json
import wave
import argparse
from google import genai
from google.genai import types

STRICT_TTS_MODEL = "gemini-3.1-flash-tts-preview"

def load_env(env_path=".env"):
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip().strip("'\"")

def pcm_to_wav(pcm_bytes, wav_path, sample_rate=24000):
    os.makedirs(os.path.dirname(wav_path), exist_ok=True)
    with wave.open(wav_path, "wb") as wav_file:
        wav_file.setnchannels(1)       # Mono
        wav_file.setsampwidth(2)      # 16-bit (2 bytes)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm_bytes)

class GeminiKeyPool:
    def __init__(self, preferred_env="GEMINI_API_KEY_04"):
        load_env()
        candidate_names = [
            preferred_env,
            "GEMINI_API_KEY_04",
            "GEMINI_API_KEY_97",
            "GEMINI_API_KEY_MAILPIT",
            "GEMINI_API_KEY_SIS",
            "GEMINI_API_KEY_STF",
            "GEMINI_API_KEY",
        ]
        seen = set()
        self.keys = []
        for name in candidate_names:
            if name and name not in seen:
                seen.add(name)
                val = os.environ.get(name)
                if val:
                    self.keys.append((name, val))
        self.current_idx = 0
        if not self.keys:
            raise ValueError("No Gemini API keys found in environment!")
        self._init_client()

    def _init_client(self):
        name, key = self.keys[self.current_idx]
        print(f"Menggunakan API key: {name} (awalan: {key[:8]}...)")
        self.client = genai.Client(api_key=key)

    def rotate_to_next(self):
        self.current_idx += 1
        if self.current_idx >= len(self.keys):
            raise RuntimeError("Semua API key Gemini di .env telah kehabisan kuota harian!")
        name, key = self.keys[self.current_idx]
        print(f"🔄 Berpindah otomatis ke API key berikutnya: {name} (awalan: {key[:8]}...)")
        self._init_client()

def generate_tts_with_retry(key_pool, text, model=STRICT_TTS_MODEL, voice_name="Despina", max_retries=6):
    """
    STRICT TTS RULE:
    Only gemini-3.1-flash-tts-preview is permitted to maintain consistent voice texture,
    audio resolution, and cadence across all 105 picture books.
    Voice: 'Despina' (female) or 'Enceladus' (male).
    """
    safety_settings = [
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY, threshold=types.HarmBlockThreshold.BLOCK_NONE),
    ]

    config = types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=voice_name
                )
            )
        ),
        safety_settings=safety_settings
    )

    for attempt in range(max_retries):
        try:
            response = key_pool.client.models.generate_content(
                model=model,
                contents=text,
                config=config
            )
            if not response.candidates or not response.candidates[0].content:
                finish_reason = response.candidates[0].finish_reason if response.candidates else "NO_CANDIDATE"
                raise ValueError(f"No content returned in response. Finish reason: {finish_reason}")
            part = response.candidates[0].content.parts[0]
            if part.inline_data and part.inline_data.data:
                return part.inline_data.data
            else:
                raise ValueError("No inline_data found in response parts")
        except Exception as e:
            err_str = str(e)
            if "Generate content requests per day limit exceeded" in err_str or "daily limit exceeded" in err_str.lower() or "limit: 10" in err_str:
                print(f"⚠️ Kuota harian model '{model}' tercapai pada key saat ini.")
                try:
                    key_pool.rotate_to_next()
                    return generate_tts_with_retry(key_pool, text, model, voice_name, max_retries)
                except RuntimeError:
                    raise RuntimeError(f"Daily quota exceeded for all keys on {model}. Sesuai AGENTS.md, tidak boleh fallback ke model lain.")
            elif "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                wait_time = (2 ** attempt) * 4 + 6
                print(f"⚠️ Rate limit RPM pada '{model}'. Menunggu {wait_time} detik (Percobaan {attempt+1}/{max_retries})...")
                time.sleep(wait_time)
            else:
                print(f"❌ Error on attempt {attempt+1}/{max_retries}: {e}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(4)
    raise RuntimeError(f"Failed to generate audio using {model}.")

def generate_story_audio(story_num=1, model=STRICT_TTS_MODEL, voice_name="Despina", force=False, target_pages=None, api_key_env="GEMINI_API_KEY_97"):
    key_pool = GeminiKeyPool(preferred_env=api_key_env)

    stories_file = "preview/stories.json"
    bundle_file = "preview/stories_bundle.js"

    with open(stories_file, "r", encoding="utf-8") as f:
        stories = json.load(f)

    story = None
    story_idx = -1
    for idx, s in enumerate(stories):
        if s.get("storyNumber") == story_num:
            story = s
            story_idx = idx
            break

    if not story:
        print(f"Cerita dengan nomor {story_num} tidak ditemukan!")
        return

    is_male = (voice_name.lower() == "enceladus")
    audio_dir = f"preview/audio/story{story_num}/male" if is_male else f"preview/audio/story{story_num}"
    os.makedirs(audio_dir, exist_ok=True)

    print(f"=== Menghasilkan Audio TTS untuk Cerita {story_num}: '{story['title']}' ===")
    print(f"Model: {model} | Karakter Suara: {voice_name} ({'Pria' if is_male else 'Wanita'})")
    print(f"Output Directory: {audio_dir}/")

    def save_state():
        if not is_male:
            stories[story_idx] = story
            with open(stories_file, "w", encoding="utf-8") as sf:
                json.dump(stories, sf, ensure_ascii=False, indent=2)
            with open(bundle_file, "w", encoding="utf-8") as bf:
                bf.write("window.STORIES_DATA = " + json.dumps(stories, ensure_ascii=False, indent=2) + ";\n")

    # 1. Generate Cover Narration (only if target_pages is None or 0 in target_pages)
    if target_pages is None or 0 in target_pages:
        cover_wav = f"{audio_dir}/page_0_cover.wav"
        cover_text = f"{story['title']}. {story.get('synopsis', '')}"
        if force or not os.path.exists(cover_wav) or os.path.getsize(cover_wav) < 1000:
            print(f"\n[Cover] Menghasilkan audio cover...")
            pcm = generate_tts_with_retry(key_pool, cover_text, model, voice_name)
            pcm_to_wav(pcm, cover_wav)
            print(f"  -> Selesai: {cover_wav} ({os.path.getsize(cover_wav)} bytes)")
            if not is_male:
                story["coverAudio"] = f"audio/story{story_num}/page_0_cover.wav"
                save_state()
            time.sleep(6)  # Respect free tier rate limit
        else:
            print(f"\n[Cover] {cover_wav} sudah ada, lewati.")
            if not is_male and not story.get("coverAudio"):
                story["coverAudio"] = f"audio/story{story_num}/page_0_cover.wav"
                save_state()

    # 2. Generate Each Page
    pages = story.get("pages", [])
    for page in pages:
        p_num = page.get("number")
        if target_pages is not None and p_num not in target_pages:
            continue
        text = page.get("textId", "").strip()
        if not text:
            continue

        wav_path = f"{audio_dir}/page_{p_num}.wav"
        rel_audio_path = f"audio/story{story_num}/page_{p_num}.wav"

        if not force and os.path.exists(wav_path) and os.path.getsize(wav_path) > 1000:
            print(f"\n[Halaman {p_num}] {wav_path} sudah ada ({os.path.getsize(wav_path)} bytes), lewati.")
            if not is_male and page.get("audio") != rel_audio_path:
                page["audio"] = rel_audio_path
                save_state()
            continue

        print(f"\n[Halaman {p_num}] Menghasilkan audio...")
        print(f"  Teks: \"{text[:60]}...\"")
        pcm = generate_tts_with_retry(key_pool, text, model, voice_name)
        pcm_to_wav(pcm, wav_path)
        print(f"  -> Selesai: {wav_path} ({os.path.getsize(wav_path)} bytes)")

        if not is_male:
            page["audio"] = rel_audio_path
            save_state()

        # Jeda antar request agar aman dari batas 2-10 RPM Free Tier
        time.sleep(6)

    print(f"\n✨ Selesai! Semua audio Cerita {story_num} ({voice_name}) berhasil disimpan di '{audio_dir}/'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate TTS Audio using STRICT gemini-3.1-flash-tts-preview")
    parser.add_argument("story", type=int, nargs="?", default=5, help="Story number (e.g. 5)")
    parser.add_argument("--voice", type=str, default="Despina", choices=["Despina", "Enceladus"], help="Voice name (Despina / Enceladus)")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing audio files")
    parser.add_argument("--pages", type=str, default=None, help="Comma-separated page numbers to generate (e.g. '1,2' or '1')")
    parser.add_argument("--api-key-env", type=str, default="GEMINI_API_KEY_STF", help="Environment variable name for Gemini API key")
    args = parser.parse_args()

    target_pages = [int(p.strip()) for p in args.pages.split(",")] if args.pages else None
    generate_story_audio(
        story_num=args.story,
        model=STRICT_TTS_MODEL,
        voice_name=args.voice,
        force=args.force,
        target_pages=target_pages,
        api_key_env=args.api_key_env
    )
