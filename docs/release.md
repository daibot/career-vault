# Release 0.1.0 — private pilot

## Publication status

Repository: [daibot/career-vault](https://github.com/daibot/career-vault), **private**, with source on `main`. GitHub account authorization and private visibility were verified on October 31, 2026. Git authentication is configured; this project's author uses the account's GitHub noreply address.

The [v0.1.0 private pilot release](https://github.com/daibot/career-vault/releases/tag/v0.1.0) is the download entry point. Invited testers must sign into GitHub with an account granted access. No collaborators have been invited automatically. Keep personal career records outside this repository. No personal skill installation is required.

Do not make this repository public. The user superseded earlier public-release authorization with **private publication only** while friends test. Public launch, outreach and portfolio changes await a later instruction.

Suggested repository description:

> An AI interview playbook for creatives to discover their career value, preserve a portable record, and tailor resumes and stories. No collection by Career Vault; AI provider settings still apply.

MIT is the proposed license default, recorded in `LICENSE`. This is a documentation-first pilot, not a verified employment outcome product.

## Build and check

Run from the repository root:

```sh
python3 scripts/release.py
```

This uses only the Python standard library. It checks relative Markdown file links, validates the skill header, builds an allowlisted skill ZIP, checks its exact contents, and creates a single complete text playbook with references inline. It does not use the network. Output is in ignored `dist/`:

- `career-vault-skill-0.1.0.zip`: skill folder and four supporting files, plus license.
- `career-vault-playbook.txt`: complete core and reference/template content for upload or paste.
- `career-vault-pilot-0.1.0.zip`: explicitly listed public-safe source, guides, templates and validation evidence. No personal records, `.git`, caches or local configuration.
- `SHA256SUMS`: artifact checksums.

The repository is the reviewable source; generated artifacts should be attached only to a private release during the pilot. Run the bundled skill validator too if available in your development environment; it is not required by users.

## Manual release checklist

- Review `git status` and every staged file; no personal data or secrets.
- Run packaging checks and read `tests/results.md` for behavioral evidence and limits.
- Confirm friend-pilot setup, privacy copy and platform citations remain current.
- Configure a real Git identity; commit reviewed source. Keep `dist/` ignored unless deliberately attaching checked release artifacts.
- Create/push to a private repository and verify actual visibility and owner.
- Record private repository/release URL and real live-test results when available.
- Public visibility, outreach and portfolio links await a later explicit owner decision.

## Known limits

Instructions cannot guarantee a model follows them. Large records may exceed context limits; use full checkpoints and load relevant sections while preserving the complete record outside chat. Host file, browsing, OCR, voice and export capabilities vary. No encryption, automated backups, telemetry, external submission, resume scoring or hiring guarantees are provided. The first release includes simulated tests, not live Claude/ChatGPT tests.
