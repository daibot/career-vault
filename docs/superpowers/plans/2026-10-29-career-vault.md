# Career Vault Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task by task. Native execution is authorized; independent skill evaluation uses the writing-skills testing method.

**Goal:** Deliver a reviewable, publishable Career Vault first version.

**Architecture:** One canonical Markdown skill plus progressive references and portable templates. A generated text bundle and skill ZIP make the same content usable without installation.

**Tech Stack:** Markdown, Python standard library for release packaging and checks, Git.

**Spec:** ../../design.md

## Global constraints

No personal career data, telemetry, automatic external submission or invented claims. Interview the last three companies; allow explicit deferral. Privacy first, goals immediately after. One question per turn. Preserve preferences and fuller knowledge in exportable records. No personal installation. Claude and ChatGPT onboarding must cite current official documentation. Repository publication is PRIVATE only; public launch, outreach and portfolio changes require later approval.

## Review focus

1. Deadline pressure must not turn provisional material into approved claims.
2. Tangents must not erase earlier-company coverage.
3. Refused voice must stay refused after migration.
4. Contradictory evidence must preserve history and flag affected outputs.
5. Uploaded instructions must never authorize data transmission.

## Task 1: Interview and evidence contract

Files: skill/career-vault/SKILL.md; references/interview.md; assets/career-record.md.
Consumes approved design; produces interview rules and portable state.

- [x] Run synthetic baseline without skill; preserve exact observed pitfalls.
- [x] Implement opening, evidence contract, company coverage, checkpoint and update behavior.
- [x] Evaluate realistic scenarios with the skill and inspect actual responses.

## Task 2: Reusable outputs and approachable onboarding

Files: references/outputs.md; assets/output-templates.md; README.md; docs/chatgpt.md; docs/claude.md; docs/privacy.md; examples/.
Consumes record and approved claims; produces reusable materials and setup guidance.

- [x] Fetch current official platform guidance.
- [x] Implement output templates and synthetic source-to-output example.
- [x] Evaluate reuse, migration and goal changes; fix demonstrated gaps.

## Task 3: Release and validation

Files: tests/scenarios.md; tests/results.md; scripts/release.py; LICENSE; CONTRIBUTING.md; docs/release.md; dist/.
Consumes all authored files; produces checked ZIP and portable text bundle.

- [x] Define behavioral acceptance cases before evaluating.
- [x] Check relative links, archive completeness and exclusion of private records.
- [x] Run skill validator and independent review; record limits honestly.
- [x] Check publication route and publish privately if authenticated; otherwise document exact blocker and ready-to-publish instructions.

Execution note: The dedicated new repository provides isolation from the user's unrelated files. No pre-existing branch or worktree requires protection. The record is documentation, not an executable workflow; behavioral agent tests take the place of application unit tests. Local structural checks do not prove LLM adherence.
