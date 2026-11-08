# scripts/merge_and_save_batch_98_to_105.py
import json

from polish_stories_98_to_101 import get_stories_98_to_101
from polish_stories_102_to_105 import get_stories_102_to_105

def merge_all():
    batch = []
    batch.extend(get_stories_98_to_101())
    batch.extend(get_stories_102_to_105())

    print(f"Loaded {len(batch)} polished stories (Stories 98 to 105).")

    # Load data/stories_full.json
    master_path = "data/stories_full.json"
    with open(master_path, "r", encoding="utf-8") as f:
        stories = json.load(f)

    # Map by storyNumber
    story_map = {s["storyNumber"]: s for s in batch}

    updated_count = 0
    for idx, s in enumerate(stories):
        num = s.get("storyNumber")
        if num in story_map:
            stories[idx] = story_map[num]
            updated_count += 1
            print(f"  ✓ Updated Story #{num}: '{story_map[num]['title']}' (10 pages)")

    # Save to data/stories_full.json
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Successfully updated {updated_count} stories in '{master_path}'!")

    # Also mirror to kerjakan-cerita-2 worktree if present
    worktree_paths = [
        "/Users/bayu/.ao/data/worktrees/storybooks/kerjakan-cerita-2/data/stories_full.json",
        "/Users/bayu/.ao/data/worktrees/storybooks/kerjakan-cerita-2/preview/stories_all_105.json"
    ]
    for wp in worktree_paths:
        try:
            with open(wp, "w", encoding="utf-8") as f:
                json.dump(stories, f, ensure_ascii=False, indent=2)
            print(f"  ✓ Mirrored to '{wp}'")
        except Exception as e:
            pass

if __name__ == "__main__":
    merge_all()
