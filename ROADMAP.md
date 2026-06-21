# Roadmap: byescaleira plugin

> Last updated: 2026-06-21

## Now (current cycle)

- [x] v0.1.0 — Dust shipped
- [x] Sync `ROADMAP.md` and mark shipped items as done
- [x] Make slash commands self-contained with embedded templates
- [x] Add `.github/workflows/release.yml`
- [x] Create safe `scripts/install.sh` for local installation
- [x] Update `README.md` to reference the install script
- [ ] Fix small issues from Claude Code review:
  - [ ] `install.sh` backup message
  - [ ] Add placeholder scripts in `/byescaleira-init` template
  - [ ] Clarify user must run `git tag` in `/byescaleira-ship`

## Next (next cycle)

- [ ] Split `CLAUDE.md` into `.claude/rules/` modular rules
- [ ] Add `.claude/settings.json` with hooks and permissions
- [ ] Add design system definitions file
- [ ] Improve `@byescaleira` agent with embedded templates
- [ ] Strengthen CI validation (frontmatter, shellcheck, markdown lint)

- [ ] Add MCP server for project scaffolding
- [ ] Add GitHub repository template
- [ ] Add sample project using the plugin

## Maybe

- [ ] CLI tool `byescaleira` for terminal usage outside Claude Code
- [ ] Automated weekly review prompt
- [ ] Integration with Apple Notes / Reminders for project tracking

## Never / deliberately out of scope

- ❌ Heavy design system implementation — definitions only, no component library
- ❌ Generic project management app — this is a developer's system, not a product
