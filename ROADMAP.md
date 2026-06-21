# Roadmap: byescaleira plugin

> Last updated: 2026-06-21

## Now (current cycle)

- [x] v0.1.0 — Dust shipped
- [x] Sync `ROADMAP.md` and mark shipped items as done
- [x] Make slash commands self-contained with embedded templates
- [x] Add `.github/workflows/release.yml`
- [x] Create safe `scripts/install.sh` for local installation
- [x] Update `README.md` to reference the install script
- [x] Split `CLAUDE.md` into `.claude/rules/` modular rules
- [x] Add `.claude/settings.json` with hooks and permissions
- [x] Add design system definitions file (`DESIGN.md`)
- [x] Improve `@byescaleira` agent with embedded templates
- [x] Package as Claude Code native plugin (`.claude-plugin/plugin.json`)
- [x] Add marketplace manifest + GitHub Releases `.zip`
- [x] Document skills-directory install as recommended today

## Next (next cycle)

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
