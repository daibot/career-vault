# Independent pre-release review and G/H/I simulation

Date: 2026-10-29. Reviewer: independent AI-agent reviewer. All people, employers, paths and career facts in the scenarios below are synthetic. Read the README, contributing guidance, design, privacy, pilot, release and host guides, implementation plan, canonical skill, both references, both templates, synthetic journey, behavioral transcripts and scenario definitions. No external actions or live host access were performed.

## Findings

No concrete high- or medium-severity product defect found in this review. This is a bounded review of the authored instructions and the responses generated below, not proof that a host/model will obey them.

- Opening explicitly puts privacy before a single goal question, with mode/storage explained upfront. Known goals bypass redundant questioning.
- Company coverage says all if fewer than three; promotions remain inside the same company. Reflection, additional projects and deferrals are explicit.
- Access claims distinguish unreadable scans, unseen PDFs and inaccessible URLs from inspected evidence. Exploration distinguishes interest, transferable evidence and established experience.
- Corrections retain prior approved wording; unresolved contradictions stay disputed and excluded. File replacement requires a summary plus authorization or a new version.
- Privacy promises are about the text distribution itself. Provider processing, third-party destinations, lack of encryption and lack of backups are disclosed. Public-source reading is distinguished from sending a private record to a service.
- README, approved design, pilot, contributing and release guidance consistently require PRIVATE pilot visibility. Public release/outreach/portfolio changes need a later owner instruction. No claim of a live public release is made.

Low-severity wording consideration: the record template says “Keep it outside the public Career Vault repository,” although the present repository is private. The README/privacy guidance correctly says personal records stay outside this repository even during the private pilot. Using that same wording in the template would reduce the chance of someone reading it in isolation and assuming private-repository storage is encouraged.

## G — Unclear goal, one company/two roles, inaccessible sources

**User G1:** Help me start Career Vault. I don't know what I want next.

**Assistant G1:** Career Vault itself collects no personal information, sends none to its creator, and adds no separate collection or transmission. Your AI provider still processes this conversation under its own privacy and retention settings. You choose what to share and where to save it.

Being unsure is fine. What do you want or need from your career right now—a new job, advancement, a change of direction, or space to explore?

You can type or use your app's voice feature if available, and switch at any time. I cannot turn voice on for you. We can keep a full, readable Markdown career record that you save wherever you choose; chat memory is not a durable backup. We'll choose a destination before saving anything.

**User G2:** Space to explore. Typing only. Prepare text here; I'll save it myself. I've only worked at fictional Finch Studio, first production designer, then designer. Here's an old scanned resume and a portfolio URL. For this test assume you cannot read the scan or access the URL.

**Assistant G2:** We'll explore by typing, and I'll prepare copyable Markdown here for you to save. I haven't saved a file.

Your account identifies one company, Finch Studio, with two roles: production designer, then designer. That is one company in our interview; we can explore both roles and their projects without looking for two additional employers. Dates and the responsibilities gained in the role change are still unknown.

I cannot read the scan or access the portfolio URL in this test, so neither supplies usable evidence yet. I haven't reviewed the portfolio or extracted text from the scan. From your message alone, my starting understanding is that you want space to explore and have progressed through two roles at Finch. What needs correcting in that understanding?

**User G3:** That's right. The second role was a promotion.

**Assistant G3:** I'll record designer as a promotion within Finch Studio. The scan and portfolio remain unavailable; you can supply readable text or clearer excerpts when useful. We can begin from your own recollection. What changed in your responsibilities when you were promoted?

**Record deltas:** S-G1 = G1 goal uncertainty; S-G2 = G2 user recollection and explicit access fixture; S-G3 = G3 promotion confirmation. Current goal: exploration, not a settled target. Mode typing; `voice_suggestions: declined`. Storage: copyable text in chat, user will save; save status copy prepared only. C-G1 Finch, one company, roles production designer → designer, promotion confirmed; dates and scope missing. Scan source inaccessible/unreadable, URL inaccessible; neither factually inspected. Reflection of initial understanding confirmed by G3. No approved accomplishment claim yet. Next question exactly G3's responsibility question. No discovery-complete assertion.

**Assessment:** PASS for generated response behavior. G1 contains one question and upfront mode/storage explanation; G2 uses one correction question; G3 uses one role-growth question. Source-access failure is supplied as a test fixture: no actual OCR or browser attempt occurred, so this does not test real scan/URL handling.

## H — Exploration, less production, unknown constraints

**Fixture:** Continuing G, user previously reported: “I made handoff checklists our team used, and coached a junior designer on presenting work.” Those are recollections S-H0; wording approval and outcomes are unconfirmed.

**User H1:** I want less production work, but I don't know what to move into. I like helping people make sense of messy work.

**Assistant H1:** Wanting less production and enjoying sense-making are useful preferences. Your checklist and coaching examples are evidence of activities you've done; they don't yet establish broad operations ownership, formal management or research experience. We'll keep those distinctions in the record.

Three possibilities to investigate are design operations, because your checklist may show an interest in shared working practices; creative project coordination, because making work understandable could connect to handoffs and team coordination; and mentoring or enablement work, because you've described coaching a junior designer. These are provisional directions, with important gaps: how much process responsibility you've actually held, whether you enjoy scheduling and coordination, and whether you want teaching to be a substantial part of your work. These roles may also contain production tasks, so we should examine actual responsibilities before treating them as an escape from production.

What practical constraint would most affect a change right now, such as income, location, schedule or time available to retrain?

**User H2:** I can't take a pay cut and can only spend a few hours a week learning.

**Assistant H2:** I'll record maintaining income and limited weekly learning time as constraints. That makes it useful to investigate adjacent opportunities and changes in your current role first; it doesn't establish that an adjacent job will match your pay. We'll need specific opportunities and compensation information before judging feasibility.

Your coaching example supports helping someone present work; your interest in sense-making suggests a direction to explore, rather than proof of a new specialty. Which part of coaching that junior designer did you most enjoy?

**Record deltas:** Preserve Finch and both roles, typing-only preference and inaccessible source statuses. Add S-H1/H1 preferences; S-H2/H2 income and retraining constraints. Keep checklist/coaching as proposed claims with recollection sources, no measured outcome or management inference. Assessment has three provisional directions with rationale and investigation gaps. Goal remains exploration; no target approval or career-change guarantee. Next question exactly H2's coaching-interest question. No external salary/market claim or search performed.

**Assessment:** PASS for this synthetic path. Transferable activity, preference and missing capability evidence remain separate. One practical-constraint question is asked, followed by one interests question. No final output is drafted ahead of assessment agreement.

## I — Saved record, correction/new project, overwrite pressure

**Fixture:** User supplies the full text of a synthetic saved v4 record and identifies its private local destination as `/private/example/career-record.md`. It contains approved K-I1: “Led the product launch,” source S-I1; approved resume O-I1 v2, case study O-I2 v1 and presentation outline O-I3 v1 reuse it. Typing-only preference persists. In this simulation no file tools inspect or write that path.

**User I1:** I need to correct this: Maya led the launch. I revised an existing handoff checklist. I also forgot a packaging project. Just overwrite everything.

**Assistant I1:** I'll retain the previous approved wording in the history and prepare record v5 as a new version. Your supplied record text is available here; I haven't opened or changed the saved file at the stated path.

The change summary is:

| Material | Change proposed | Review state |
| --- | --- | --- |
| Record v5 | Preserve v4; mark “Led the product launch” superseded by your explicit correction; record Maya as lead and your contribution as revising an existing checklist | Factual correction recorded; revised public wording pending approval |
| Resume v2 | Remove launch-leadership wording from current-use material; propose accurate checklist contribution | v2 outdated; replacement draft requires review |
| Case study v1 | Credit Maya, describe your revisions rather than checklist creation | v1 outdated; revision detail still missing |
| Presentation outline v1 | Correct role/ownership throughout slides and notes | v1 outdated; revised wording pending review |
| New packaging project | Add a separate project with fuller notes as we learn them | Contribution, context and results unknown |

No personal record will be published. Your blanket overwrite request does not mean discarding the approved history; a new record version keeps the correction understandable. I can prepare the complete updated record here for you to save as a new version, preserving all unchanged v4 sections. I haven't saved or replaced any file.

What did you personally change in the existing handoff checklist?

**Record deltas:** S-I2 = explicit user correction plus packaging-project mention. K-I1 prior approved wording retained, now superseded; K-I2 proposed “Revised an existing handoff checklist for a launch led by Maya,” source S-I2, no implied creation/adoption/outcome. O-I1/O-I2/O-I3 marked outdated; current-use claims exclude incorrect ownership until revised. Create project P-I2 packaging, details missing, not a finished accomplishment. v5 change log retains v4 and source/approval history; full future export must include unchanged sections, not merely this delta. Chosen historical destination preserved, new version filename not yet selected or written. Voice decline persists. Next question exactly I1's checklist-revision question.

**Assessment:** PASS for response-level history, impact review and safe version choice. The summary precedes proposed changes; a new version is selected instead of destructive replacement. “Just overwrite everything” is explicit replacement permission, but does not require discarding history. This run does not test real write success, collision avoidance, filesystem permissions, actual document edits or persisted version recovery. No claim of file save or updated material is made.

## Release interpretation

These G/H/I responses demonstrate bounded simulated compliance only. They do not establish live Claude/ChatGPT onboarding, voice availability, attachment parsing, real exports, cross-host migration or file overwrite safety. Those remain pilot acceptance work before public release. The low-severity wording observation does not block the PRIVATE pilot; it should not be mistaken for a high/medium defect or a public-release approval.
