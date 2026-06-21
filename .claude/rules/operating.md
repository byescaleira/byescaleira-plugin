# Operating Rules

## Hard rules

1. No project starts without `PROPOSAL.md`.
2. `main` is always stable. Never push directly to it.
3. Use semantic commits: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`.
4. Every release has a version `vX.Y.Z` and a planet codename.
5. Keep `CHANGELOG.md`, `ROADMAP.md`, and `DECISIONS.md` alive.
6. Work in 6-week cycles + 2-week cooldown.
7. Maximum 3 big tasks in "Now" on the roadmap.
8. Default license: MIT.
9. All public-facing project documentation is in English.
10. When using AI in a project, document it honestly in `DECISIONS.md` or the README.

## Project lifecycle

| Phase | Deliverable |
|---|---|
| Spark | Note or issue |
| Proposal | `PROPOSAL.md` (one page) |
| Build | Code + `ROADMAP.md` |
| Ship | Release + `CHANGELOG.md` |
| Review | Updated roadmap + `DECISIONS.md` |

## Scope rules — The Three Nos

1. If it does not fit in a 6-week cycle, it does not enter.
2. If it has no clear done criterion, it does not start.
3. If it is not essential for the MVP, it does not happen now.

## Commits

Use conventional commits:

- `feat:` — new feature
- `fix:` — bug fix
- `refactor:` — code change with no behavior change
- `test:` — tests
- `docs:` — documentation
- `chore:` — maintenance

## Releases

1. Choose next version by semver.
2. Match it to the planet codename table.
3. Update `CHANGELOG.md`.
4. Update `ROADMAP.md`.
5. Run: `git tag -a vX.Y.Z -m "Planet"`.
6. Push tag to trigger `release.yml`.
