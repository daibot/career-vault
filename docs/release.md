# Career Vault 0.1.1-beta.1 — public beta

## Distribution

[Repository](https://github.com/daibot/career-vault) · [Beta downloads](https://github.com/daibot/career-vault/releases/tag/v0.1.1-beta.1)

The creator approved public beta publication after the original private pilot was packaged. The skill, templates and synthetic examples are reusable under the MIT license. No real career records are part of the distribution. Live-user validation is still pending; this is an early beta.

Version 0.1.0 is the historical private-pilot snapshot. Its wording describes the status at that time. Version 0.1.1-beta.1 provides the current public-beta setup, walkthrough and feedback guidance. The repository's full history and any published historical downloads are visible once it is public.

## Choose a download

- `career-vault-playbook.txt`: complete skill instructions, supporting guides and templates for upload/paste. No installation required.
- `career-vault-skill-0.1.1-beta.1.zip`: installable skill folder for compatible hosts; see the Claude guide for its optional ZIP path.
- `career-vault-beta-0.1.1-beta.1.zip`: complete reusable source, onboarding, walkthrough, templates and validation evidence, plus the two files above.
- `SHA256SUMS`: checksums for the three downloads.

The package does not activate voice, install itself by opening a GitHub URL or provide encryption/backups. Keep personal records outside the repository and public feedback. AI-provider privacy settings still apply.

## What changed from the pilot

- Clear AI-skill positioning and separate installation/copy-upload paths.
- Synthetic walkthrough and optional recording outline.
- Design/build notes with AI assistance disclosed.
- Public feedback template, contribution guidance and draft launch copy.
- Public-release history/download review and updated packaging metadata.

The interview and evidence rules retain the same core workflow. These documentation/packaging changes are not additional evidence of live host reliability.

## Build and verify

From the repository root:

```sh
python3 scripts/release.py
```

The standard-library tool checks allowlisted file existence, internal Markdown file links, a minimal skill header, archive manifests/CRC and SHA-256 checksums. It builds only named reusable files; `.git`, local configuration, arbitrary working-tree contents and personal record directories are excluded. Output is in ignored `dist/`.

Identical inputs produce identical artifacts. Packaging integrity does not prove that an AI follows the instructions or that every possible sensitive fact has been detected. Read the [validation report](../tests/results.md) and [public release review](public-release-review.md).

## For maintainers

Review the whole staged diff, full history when making visibility changes, release downloads and public feedback for unintended private content. Test behavior changes with realistic synthetic scenarios. Keep actual live-host results distinct from simulations. Build and inspect artifacts before upload, then compare uploaded digests and the remote commit with the reviewed local results.

Do not upload user career records. No external announcement, direct outreach, collaborator invitation or portfolio edit is authorized simply by publishing a release.

## Known limits

Host/model compliance, live onboarding on Claude/ChatGPT, actual exports, OCR/browsing, voice/file access and long-session/cross-host migration remain to be established by beta users. Context limits may require loading relevant record sections while preserving the full record separately. No hiring outcomes, automated career-data collection or provider-level privacy guarantee are claimed.
