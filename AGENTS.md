# AGENTS.md — WEB Designer Portfolio

## Project

Portfolio package for job applications. Contains cover letter + 3 case studies as Markdown files.

## Structure

```
.
├── AGENTS.md                  # This file
├── README.md                  # Usage instructions
├── cover-letter.md            # Cover letter template
├── project-01-figma-tilda.md  # Case: Figma + Tilda landing
├── project-02-figma-wordpress-ai.md  # Case: Figma + WordPress + AI
└── project-03-automation-ai.md       # Case: AI automation workflows
```

## Before Sending to Client

- Replace contacts in `cover-letter.md` (Telegram, Email, portfolio link)
- Replace contacts in `project-03-automation-ai.md`
- Replace Figma links (currently placeholders: `figma.com/file/...`)
- Adapt project descriptions to match your real work if needed

## Workflow

1. Review `cover-letter.md` — adjust tone and details
2. Review case studies — verify metrics and project names
3. Export to PDF or send as-is (Markdown)

## Secrets and API Tokens

Global secrets file: `~/.env`
- FIGMA_TOKEN — для работы с Figma API
- Другие токены добавлять по мере необходимости
- Файл имеет права 600 (только владелец)

## Rules

- Do not commit `.env` files
- Keep filenames consistent (used as links in cover-letter.md)
- Maintain Markdown format — client may read raw files
- Do not include real client data without permission

## Git

- Branch: `main`
- No PRs needed (personal repo)
- Commit after each significant update
