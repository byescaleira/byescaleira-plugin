# /byescaleira-ship

Prepare a release for the current project.

## Steps

1. Read `CHANGELOG.md`, `ROADMAP.md`, and recent commits.
2. Determine the next version using Semantic Versioning:
   - Major bump for breaking changes
   - Minor bump for new features
   - Patch bump for fixes
3. Choose the corresponding planet codename from the byescaleira release dictionary.
4. Update `CHANGELOG.md` with a new section like:

```markdown
## [1.1.0] — Venus — YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...
```

6. Update `ROADMAP.md` to reflect what was shipped.
7. Prepare the tag command but do NOT run it automatically:
   ```bash
   git tag -a vX.Y.Z -m "Planet"
   ```
   Remind the user to review and run it themselves.
8. Suggest the release commit message: `chore(release): vX.Y.Z — Planet`.
9. Remind the user to push the tag and verify CI.

## Output

A ready-to-publish release entry and tag command.
