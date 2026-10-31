# Validation evidence — 2026-10-29

All examples and test career facts are synthetic. No real career record or source-thread personal details are included. This report records the original private-pilot evaluation. The creator subsequently approved a public beta; no additional live-host results are implied. See the [public release review](../docs/public-release-review.md).

## Baseline before writing the skill

An independent agent received the urgent-resume/tangent/exaggeration/typed-only scenario without Career Vault. It refused invented sales and sole-leadership claims, but immediately drafted a generic resume and offered to omit Alder House before investigating it. Exact observed excerpts:

> “Here’s a fast starting point.”

> “We can keep Alder House off this focused draft if it’s older and less relevant.”

It then asked about mentoring at Pebble. Its self-review identified premature omission of older work and unconfirmed implications in “shaping launch work,” “creative leadership,” and “creative development and growth.” The skill addresses these with an assessment/claim approval step, retained three-company coverage and explicit evidence boundaries. The baseline did not exhibit invented metrics or unwanted voice suggestions; no improvement is claimed for those behaviors from this comparison.

## Behavioral evaluations

See [actual agent-generated turns and checkpoints](behavior-transcripts.md) for A–F from [scenarios](scenarios.md), including an urgent three-company interview with a productive tangent, declined voice, a pause/export, import with changed goal, corrected ownership, embedded upload instructions and a single supported accomplishment reused across three outputs.

Observed in this run: no invented numerical results or sole ownership, three-company partial coverage retained with deferrals, declined voice preserved, full first checkpoint, proposed impact review and source-linked output reuse. The corrected ownership is treated as a user-confirmed factual correction; proposed public wording still requires approval. Later updates are versioned addenda and must travel with the base record until consolidated.

See [independent review and additional simulations](review.md) for opening, fewer-company/multiple-role handling, inaccessible material, exploration and overwrite/versioning checks.

These are simulated conversations produced by AI evaluators in this environment. They are not recordings of actual Claude or ChatGPT use and do not establish live browsing, PDF/OCR parsing, voice activation, file saving, upload prevention, skill installation, long-session consistency or reliable behavior across models. One behavioral run per scenario is insufficient to claim statistical reliability. No five-repeat wording experiment was run; this is a pilot validation, not a controlled effectiveness study. No behavioral failure required wording refactoring in the first evaluation; further pilot failures should drive narrow changes and retesting.

Independent review found no high/medium issue. Its low-severity template wording concern was corrected: personal records must stay outside the repository, including during the private pilot. The private-pilot package was rebuilt after that correction.

## Structural checks

Run `python3 scripts/release.py` from the repository root. The release script validates allowlisted file existence, internal Markdown file links, the minimal skill header and nonempty body, archive manifests/CRC and artifact checksums. It includes no network operations and packages only named reusable files, not arbitrary working-tree content. These checks prove packaging integrity, not interview quality or absence of every possible sensitive fact. Source content was also manually reviewed for synthetic-only examples.

The upstream skill-creator `quick_validate.py` was attempted with system and bundled Python. Both stopped because the optional PyYAML dependency is absent (`ModuleNotFoundError: No module named 'yaml'`). No package was installed into personal settings. The release script's simpler checks passed when run; they do not replace the full upstream validator. On October 31, 2026, a follow-up run used PyYAML 6.0.3 in an isolated temporary environment and the upstream validator reported “Skill is valid!” for the public-beta skill. The original dependency failure remains part of the historical record.

## Remaining gates

Live testing on Claude and ChatGPT, actual checkpoint migration and voice/file availability remain to be verified. The upstream structural validator passed on October 31; it does not establish those behavioral results. Follow the [beta testing guide](../docs/pilot.md). Historical publication restrictions were superseded by the creator's later public-beta approval; current distribution details are in the [release guide](../docs/release.md).

## LinkedIn onboarding follow-up

Beta.2 explicitly offers a LinkedIn profile URL among optional starting sources, with authorized-browser access or a pasted/exported fallback. The [synthetic evaluation](linkedin-onboarding.md) records the before/after invitation and inaccessible-profile behavior. This evaluates response wording in an agent simulation; it does not establish live LinkedIn access, scraping coverage, account control or cross-host performance. No personal career information is used in the public test.
