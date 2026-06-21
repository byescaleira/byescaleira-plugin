# Design System Definitions

This file contains the **definitions** of the byescaleira visual system. It is intentionally not a component library. It is a source of truth for colors, typography, spacing, and visual principles.

## Brand identity

- **Handle:** `byescaleira`
- **Name:** Rafael Escaleira
- **Positioning:** iOS Specialist
- **Tagline:** "I build iOS apps that actually ship."
- **Personality:** precise, native-first, AI-fluent, direct.
- **Tone:** personal, no corporate fluff, AI-honest.

## Design principles

1. **Native first.** The UI should feel like it belongs on iOS. Use native controls, native navigation patterns, and native animations before custom ones.
2. **Space as structure, not decoration.** The space theme informs naming, palette, and mood. It does not mean starry backgrounds everywhere.
3. **Dark by default.** Interfaces should work in dark mode first, then light mode.
4. **Motion with purpose.** Animations explain state changes. Avoid motion for decoration.
5. **Information density over whitespace overdose.** Every screen should earn its space.
6. **AI transparency.** When AI generates content, label it.

## Color palette — Deep Space

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `void-black` | `#0B0F19` | `11, 15, 25` | Primary background, surfaces |
| `nebula-blue` | `#3B82F6` | `59, 130, 246` | Primary accent, interactive elements |
| `starlight` | `#F8FAFC` | `248, 250, 252` | Primary text on dark |
| `orbit-gray` | `#64748B` | `100, 116, 139` | Secondary text, disabled states |
| `supernova` | `#F59E0B` | `245, 158, 11` | Warnings, highlights, CTAs |
| `cosmos-teal` | `#14B8A6` | `20, 184, 166` | Success, positive states |
| `mars-red` | `#EF4444` | `239, 68, 68` | Errors, destructive actions |

### Gradients

- **Void gradient:** `linear-gradient(180deg, #0B0F19 0%, #1E293B 100%)`
- **Nebula glow:** `radial-gradient(circle at 50% 0%, rgba(59, 130, 246, 0.15), transparent 60%)`

## Typography

### Typefaces

| Context | Font | Fallback |
|---|---|---|
| UI headings | Geist | SF Pro Display, Inter, system-ui |
| UI body | Inter | SF Pro Text, system-ui |
| Code | JetBrains Mono | SF Mono, Menlo, monospace |

### Scale

| Level | Size | Usage |
|---|---|---|
| Display | 32–40 pt | Hero text, splash screens |
| H1 | 28 pt | Top-level headings |
| H2 | 22 pt | Section headings |
| H3 | 18 pt | Card titles |
| Body | 16 pt | Primary content |
| Caption | 13 pt | Metadata, timestamps |
| Code | 14 pt | Monospaced content |

## Spacing

| Token | Value |
|---|---|
| `space-xs` | 4 pt |
| `space-sm` | 8 pt |
| `space-md` | 16 pt |
| `space-lg` | 24 pt |
| `space-xl` | 32 pt |
| `space-2xl` | 48 pt |

## Radius

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | 6 pt | Buttons, chips |
| `radius-md` | 12 pt | Cards, sheets |
| `radius-lg` | 20 pt | Modals, full-width containers |

## Elevation / shadows

| Token | Value |
|---|---|
| `shadow-sm` | `0 1px 2px rgba(0, 0, 0, 0.3)` |
| `shadow-md` | `0 4px 12px rgba(0, 0, 0, 0.4)` |
| `shadow-lg` | `0 8px 24px rgba(0, 0, 0, 0.5)` |

## Iconography

- Style: line icons, 1.5 pt stroke.
- Size: 20 pt default, 24 pt for navigation, 16 pt for inline.
- Color: `starlight` or `orbit-gray` by default; `nebula-blue` for active/selected states.

## Layout principles

1. Use a 12-column grid for non-mobile layouts.
2. Mobile first, but iPad/desktop should not feel like a stretched phone.
3. Navigation is the spine of the app. Choose it early and change it rarely.
4. Every screen needs a clear primary action.
5. Empty states are part of the feature, not an afterthought.

## README signature

Every README must end with:

```markdown
---

Built by [Rafael Escaleira](https://byescaleira.com) · [@byescaleira](https://x.com/byescaleira)

If something here helped you, let me know. If something is wrong, tell me louder.
```

## How to use this file

- Reference it when starting a new project.
- Update `DECISIONS.md` when deviating from these definitions.
- Do not turn it into a code library. Keep it as definitions.
