# Design and build notes

Career Vault is an AI skill designed by daibot and developed with AI assistance. Its purpose is to help creatives articulate contributions that are easy to lose behind a job title—and preserve those facts for the next opportunity.

## Product decisions

- **Discovery before drafting.** An immediate resume request can hide the strongest story. The skill establishes goals, investigates work and discusses an assessment before drafting approved claims.
- **Three companies, with room for depth.** The interview covers the last three companies, including promotions, multiple projects and less visible work. People can defer questions; the record keeps the gaps.
- **One question at a time.** A structured checklist runs beneath a flexible conversation so productive tangents do not reset progress.
- **The person controls the record.** Readable Markdown preserves fuller knowledge, preferences and unresolved questions across sessions and assistants.
- **Evidence travels with the story.** Source and claim IDs connect personal actions, team contributions, uncertainty, approvals and output versions. Corrections trigger proposed changes across materials.
- **Privacy has a concrete boundary.** The skill contains no telemetry, external career-data submission or hosted database. AI-provider processing and user-chosen storage still have their own privacy settings.

## Technical structure

`skill/career-vault/SKILL.md` is the canonical entry point. Interview/output references load when relevant, while Markdown templates define the career record and output shapes. One core skill supports both initial target hosts through separate onboarding guides.

The Python standard-library release tool builds an allowlisted skill ZIP, a complete text distribution and a source bundle. It checks relative file links, archive manifests/CRC and SHA-256 checksums. Fixed archive metadata makes unchanged inputs reproducible. No network or package dependencies are needed to run that tool.

The copy/upload distribution makes the skill usable when a host has no skill installer or cannot read GitHub links. Actual installation, voice, browsing, OCR and file generation depend on the host. A requested presentation can therefore be a clearly identified text outline when no slide-file tool exists.

## Evaluation and limits

A baseline agent drafted too early and offered to drop a company before investigating it. The skill adds an assessment/approval step and preserves company coverage with explicit deferrals. Subsequent agent simulations exercise urgency, tangents, typing-only preference, changed goals, contradictory evidence, untrusted source instructions, reuse and migration. [Read the evidence and limitations](../tests/results.md).

These are simulated paths. Live Claude/ChatGPT usability, actual exports, long-session consistency and cross-host migration still require user testing. No employment outcome or statistically reliable improvement has been demonstrated. AI assistance was used for implementation, documentation and evaluation; generated work was reviewed and packaging checks were run.

## What happens next

The public beta invites feedback on setup, discovery quality, evidence accuracy and record continuity. Useful progress will be shown through redacted or synthetic reproductions, issue discussions and documented fixes. Any future account of a real user's experience requires their separate consent and appropriate redaction. No testimonials or adoption numbers are claimed.
