# Proposal: byescaleira plugin

## 1. Problem

Rafael Escaleira builds many personal projects across iOS, tools, and experiments. Without a consistent system, each project starts from scratch: different structures, unclear scope, forgotten documentation, and no clear release process.

The result is a graveyard of half-built repos and lost context.

## 2. Audience

Primarily Rafael Escaleira. Secondarily, any iOS engineer or builder who wants a lightweight, opinionated system for personal projects.

## 3. Solution

A Claude Code plugin that encodes a personal operating system into the agent itself:

- Global `CLAUDE.md` with identity, voice, principles, codenames, and rules.
- Slash commands for starting projects, writing proposals, reviewing roadmaps, and shipping releases.
- A specialist agent (`@byescaleira`) that can be invoked for any task.

The plugin is stored in a public GitHub repository and installed into `~/.claude/`.

## 4. Success Criteria (90 days)

- [ ] Plugin installed and used in at least 3 new or refactored projects.
- [ ] Every new project starts with `PROPOSAL.md` and the skeleton.
- [ ] At least one release follows the `vX.Y.Z` + planet codename convention.
- [ ] No abandoned projects without a clear `ROADMAP.md` update.

## 5. MVP

1. `CLAUDE.md` with identity, voice, principles, codenames, repository skeleton, and operating rules.
2. Four slash commands: `init`, `proposal`, `roadmap`, `ship`.
3. One agent: `@byescaleira`.
4. Public GitHub repository with the byescaleira skeleton.

## 6. Out of Scope

- MCP server integration.
- Hooks for automatic linting/formatting.
- Rules directory split (can come later).
- Design system implementation (only definitions for now).

## 7. Differentiation

Most personal systems live in Notion or private notes. This one lives inside the coding agent itself. It is actionable at the moment of creation, not just reference material.

## 8. Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| CLAUDE.md becomes too large | Medium | Medium | Split into rules/ later |
| Slash commands feel gimmicky | Low | Medium | Keep them practical and checklist-driven |
| Agent conflicts with default Claude behavior | Low | High | Prefix all rules clearly and keep scope narrow |

## 9. Why now?

Rafael is actively refactoring all personal projects and wants enterprise-grade governance applied at personal scale. The current moment — after moving to iOS Specialist at Globo and leading AI adoption — is the right time to formalize the system.

## 10. Open Questions

- [ ] Should the plugin include a GitHub repository template in addition to the Claude Code plugin?
- [ ] Should there be a separate repo for iOS-specific components?
- [ ] How often should the plugin be reviewed and versioned?

## Decision

| Date | Decision | By |
|---|---|---|
| 2026-06-21 | Approved for MVP | Rafael Escaleira |
