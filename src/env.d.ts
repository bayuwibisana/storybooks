/// <reference types="astro/client" />

declare namespace App {
  interface Locals {
    /** memoised by getViewer() — do not set by hand */
    viewer?: import('./db/entitlements').ViewerAccess;
  }
}
