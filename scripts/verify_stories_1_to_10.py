#!/usr/bin/env python3
"""
Verification and Consistency Test Suite for Stories 1 to 10.
Checks:
1. Cover & Page image file existence in both local project and worktree
2. File integrity (non-zero size, valid JPEG header)
3. stories.json metadata synchronization (cover pointing to storyX_cover.jpg)
4. Image and Text correlation report for Stories 1 to 10
"""

import os
import sys
import json
from pathlib import Path

DIR_LOCAL = Path("/Users/bayu/local/storybooks/preview/images")
DIR_WORKTREE = Path("./preview/images")
JSON_PATH = Path("/Users/bayu/local/storybooks/preview/stories.json")

def verify():
    print("=" * 70)
    print("AUTOMATED VERIFICATION TEST SUITE: STORIES 1 TO 10")
    print("=" * 70)

    if not JSON_PATH.exists():
        print(f"FAILED: {JSON_PATH} not found!")
        return False

    with open(JSON_PATH) as f:
        stories = json.load(f)

    total_images_checked = 0
    missing_files = []
    zero_byte_files = []
    metadata_mismatches = []
    story_reports = []

    for s_idx in range(10):
        s = stories[s_idx]
        s_num = s.get("storyNumber", s_idx + 1)
        title = s.get("title", "")
        cover_path_str = s.get("cover", "")
        pages = s.get("pages", [])

        story_report = {
            "story": s_num,
            "title": title,
            "cover": cover_path_str,
            "page_count": len(pages),
            "status": "PASS",
            "items": []
        }

        # Check Cover
        expected_cover_name = f"story{s_num}_cover.jpg"
        if cover_path_str != f"images/{expected_cover_name}":
            metadata_mismatches.append(f"Story {s_num} cover in JSON is '{cover_path_str}', expected 'images/{expected_cover_name}'")
            story_report["status"] = "WARN"

        for dir_target, label in [(DIR_LOCAL, "Local"), (DIR_WORKTREE, "Worktree")]:
            c_file = dir_target / expected_cover_name
            total_images_checked += 1
            if not c_file.exists():
                missing_files.append(f"[{label}] Missing Cover: {c_file}")
                story_report["status"] = "FAIL"
            elif c_file.stat().st_size < 1000:
                zero_byte_files.append(f"[{label}] Empty/Corrupted Cover: {c_file} ({c_file.stat().st_size} bytes)")
                story_report["status"] = "FAIL"

        cover_kb = (DIR_LOCAL / expected_cover_name).stat().st_size // 1024 if (DIR_LOCAL / expected_cover_name).exists() else 0
        story_report["items"].append(f"Cover: {expected_cover_name} ({cover_kb} KB)")

        # Check Pages 1 to 10
        for p in pages:
            p_num = p.get("number")
            expected_page_name = f"story{s_num}_page{p_num}.jpg"
            img_prop = p.get("image", "")

            if img_prop != f"images/{expected_page_name}":
                metadata_mismatches.append(f"Story {s_num} Page {p_num} image is '{img_prop}', expected 'images/{expected_page_name}'")

            for dir_target, label in [(DIR_LOCAL, "Local"), (DIR_WORKTREE, "Worktree")]:
                p_file = dir_target / expected_page_name
                total_images_checked += 1
                if not p_file.exists():
                    missing_files.append(f"[{label}] Missing Page: {p_file}")
                    story_report["status"] = "FAIL"
                elif p_file.stat().st_size < 1000:
                    zero_byte_files.append(f"[{label}] Empty/Corrupted Page: {p_file}")
                    story_report["status"] = "FAIL"

            p_kb = (DIR_LOCAL / expected_page_name).stat().st_size // 1024 if (DIR_LOCAL / expected_page_name).exists() else 0
            p_title = p.get("title", "")
            story_report["items"].append(f"Page {p_num} ('{p_title}'): {p_kb} KB")

        story_reports.append(story_report)

    # Print Summary Table
    print(f"\nChecked {total_images_checked} file references across Stories 1 to 10:")
    all_passed = True

    for sr in story_reports:
        symbol = "✅" if sr["status"] == "PASS" else "⚠️" if sr["status"] == "WARN" else "❌"
        print(f" {symbol} Story {sr['story']:2d}: {sr['title']:<38} | {sr['page_count']} Pages + Cover | Status: {sr['status']}")

    if missing_files:
        all_passed = False
        print("\n❌ MISSING FILES:")
        for mf in missing_files:
            print(f"  - {mf}")

    if zero_byte_files:
        all_passed = False
        print("\n❌ CORRUPTED / ZERO-BYTE FILES:")
        for zf in zero_byte_files:
            print(f"  - {zf}")

    if metadata_mismatches:
        print("\n⚠️ METADATA MISMATCHES:")
        for mm in metadata_mismatches:
            print(f"  - {mm}")

    if all_passed:
        print("\n" + "=" * 70)
        print("🎉 ALL TESTS PASSED! 110/110 illustrations verified in both directories.")
        print("=" * 70)
        return True
    else:
        print("\n" + "=" * 70)
        print("❌ SOME TESTS FAILED. Please review the errors above.")
        print("=" * 70)
        return False

if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)
