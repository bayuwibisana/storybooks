#!/usr/bin/env python3
"""
Upload Kisah Krayon assets (Covers, Pages, and Audio) to Cloudflare R2 bucket.

Usage:
    python3 scripts/upload_to_r2.py [--dry-run] [--images-only] [--audio-only]
"""

import os
import sys
import glob
import mimetypes
from pathlib import Path
import boto3
from botocore.config import Config

def load_env_file(env_path):
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip("'\"")
    return env_vars

def get_s3_client(env):
    account_id = env.get("R2_ACCOUNT_ID", "425148ed4de08261ce3f2cdf337752f2")
    access_key = env.get("R2_ACCESS_KEY_ID") or env.get("S3_ACCESS_ID")
    secret_key = env.get("R2_SECRET_ACCESS_KEY") or env.get("S3_SECRET_KEY")
    endpoint_url = f"https://{account_id}.r2.cloudflarestorage.com"

    return boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
        config=Config(retries={"max_attempts": 5, "mode": "standard"})
    )

def collect_files():
    base_dir = Path("/Users/bayu/local/storybooks")
    items = []

    # 1. Covers -> covers/storyX_cover.jpg
    for p in sorted(base_dir.glob("preview/images/story*_cover.jpg")):
        items.append((p, f"covers/{p.name}", "image/jpeg"))

    # 2. Pages -> pages/storyX_pageY.jpg
    for p in sorted(base_dir.glob("preview/images/story*_page*.jpg")):
        items.append((p, f"pages/{p.name}", "image/jpeg"))

    # 3. Audio -> audio/story.../page_X.wav
    audio_base = base_dir / "preview/audio"
    if audio_base.exists():
        for p in sorted(audio_base.rglob("*.wav")):
            rel = p.relative_to(audio_base)
            items.append((p, f"audio/{rel.as_posix()}", "audio/wav"))

    return items

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Upload storybooks assets to Cloudflare R2")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without uploading")
    parser.add_argument("--images-only", action="store_true", help="Only upload images")
    parser.add_argument("--audio-only", action="store_true", help="Only upload audio")
    parser.add_argument("--force", action="store_true", help="Re-upload even if size matches")
    args = parser.parse_args()

    env_paths = [
        "/Users/bayu/local/storybooks/web/.env",
        "/Users/bayu/local/storybooks/.env"
    ]
    env = {}
    for ep in env_paths:
        env.update(load_env_file(ep))

    bucket_name = env.get("R2_BUCKET", "kisah-krayon")
    public_url = env.get("R2_PUBLIC_URL", "https://pub-225fbf98db8843d786cf3b6d188c7837.r2.dev")

    print(f"Connecting to Cloudflare R2 bucket: '{bucket_name}'...")
    s3 = get_s3_client(env)

    # Fetch existing objects
    print("Listing existing objects in bucket to skip already uploaded files...")
    existing_objects = {}
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get("Contents", []):
            existing_objects[obj["Key"]] = obj["Size"]

    print(f"Found {len(existing_objects)} existing objects in R2 bucket.")

    all_files = collect_files()
    if args.images_only:
        all_files = [f for f in all_files if f[2].startswith("image/")]
    elif args.audio_only:
        all_files = [f for f in all_files if f[2].startswith("audio/")]

    to_upload = []
    skipped = 0
    for local_path, key, content_type in all_files:
        local_size = local_path.stat().st_size
        if not args.force and key in existing_objects and existing_objects[key] == local_size:
            skipped += 1
        else:
            to_upload.append((local_path, key, content_type, local_size))

    print(f"\nTotal files collected: {len(all_files)}")
    print(f"Already up-to-date in R2: {skipped}")
    print(f"To upload: {len(to_upload)}")

    if args.dry_run:
        print("\n[DRY RUN] First 10 items to upload:")
        for lp, k, ct, sz in to_upload[:10]:
            print(f"  {k} ({sz} bytes, {ct})")
        return

    if not to_upload:
        print("✨ Semua berkas sudah up-to-date di R2!")
        return

    total_bytes = sum(item[3] for item in to_upload)
    print(f"Starting upload ({total_bytes / (1024*1024):.2f} MB across {len(to_upload)} files)...")

    from concurrent.futures import ThreadPoolExecutor, as_completed

    uploaded = 0
    failed = 0
    
    def upload_single_file(item):
        local_path, key, content_type, local_size = item
        try:
            with open(local_path, "rb") as f:
                s3.put_object(
                    Bucket=bucket_name,
                    Key=key,
                    Body=f,
                    ContentType=content_type,
                    CacheControl="public, max-age=31536000, immutable"
                )
            return True, key, local_size
        except Exception as e:
            return False, key, str(e)

    # Use 8 concurrent worker threads for maximum throughput
    max_workers = 8
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(upload_single_file, item): item for item in to_upload}
        for idx, fut in enumerate(as_completed(futures), 1):
            success, key, info = fut.result()
            if success:
                uploaded += 1
                if idx % 10 == 0 or idx == len(to_upload):
                    print(f"[{idx}/{len(to_upload)}] Uploaded {key} ({info/1024:.1f} KB) ✅")
            else:
                failed += 1
                print(f"[{idx}/{len(to_upload)}] FAILED {key}: {info} ❌")

    print(f"\n🎉 Berhasil mengunggah {uploaded} berkas ke Cloudflare R2 ({bucket_name})! (Gagal: {failed})")
    print(f"Public URL Sample: {public_url}/covers/story1_cover.jpg")

if __name__ == "__main__":
    main()
