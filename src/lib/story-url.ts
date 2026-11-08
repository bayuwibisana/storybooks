/**
 * Helper utilities for human-friendly story URLs and flexible slug resolution.
 */

export function slugifyTitle(title: string): string {
  return String(title || '')
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-');
}

export function getStoryUrl(story: { id?: string; title?: string; storyNumber?: number }): string {
  if (story.title) {
    return `/baca/${slugifyTitle(story.title)}`;
  }
  if (story.storyNumber) {
    return `/baca/story-${story.storyNumber}`;
  }
  return `/baca/${story.id || ''}`;
}
