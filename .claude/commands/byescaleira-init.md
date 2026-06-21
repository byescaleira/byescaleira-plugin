# /byescaleira-init

Generate the byescaleira universal repository skeleton in the current directory.

## Steps

1. Confirm or ask for the project codename from the byescaleira space dictionary.
2. Create the directory structure:

```
./
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   ├── pull_request_template.md
│   └── issue_templates/
│       ├── bug_report.md
│       └── feature_request.md
├── README.md
├── PROPOSAL.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── LICENSE
└── .gitignore
```

3. Fill each file with the byescaleira templates, replacing `<project>` with the chosen codename.
4. Use English for all generated documentation.
5. Add the byescaleira README signature at the end of README.md.
6. Commit message suggestion: `chore: bootstrap repository skeleton`.

## Notes

- If files already exist, ask before overwriting.
- Do NOT generate code yet. Only the definitions layer.
- The user may specify a stack later; keep templates stack-agnostic for now.
