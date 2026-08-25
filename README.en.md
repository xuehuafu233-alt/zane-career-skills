# Zane Career Skills

[简体中文](README.md) | English

> No resume template. Turn what you have actually done into career assets that recruiters can understand quickly and want to explore further.

[![Version](https://img.shields.io/badge/version-v0.7_beta-2563EB.svg?style=flat-square)](VERSION.md)
[![Skills](https://img.shields.io/badge/skills-11-0F766E.svg?style=flat-square)](docs/skill-inventory.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](LICENSE)

One command installs 11 independently usable Agent Skills for evidence intake, hiring positioning, multilingual resumes, portfolio websites, case storytelling, visual direction, privacy decisions, and release QA.

**Works with Claude Code, Codex, and other tools that support Agent Skills.**

[Quick start](#quick-start) · [What it solves](#what-it-solves) · [Capabilities](#capabilities) · [Install](#install) · [Method boundaries](#method-boundaries)

![From experience to application-ready career assets](docs/zane-career-assets-flow.en.svg)

## What it solves

Most people do not lack experience. They lack a reliable path from experience to a hiring decision.

| Where you are now | What these Skills help you reach |
| --- | --- |
| An old resume, scattered project files, and partial memories | A fact ledger and a clear view of which evidence matters |
| Plenty of experience, but no obvious role fit | A defined audience, positioning, and claim hierarchy |
| A resume that reads like a task log | Evidence-led achievements with defensible attribution |
| A portfolio idea with no content architecture | A reading path from a 30-second scan to deep case proof |
| Strong source material but stiff, literal English | Market-aware localization of tone, order, and emphasis |
| Visual references that keep turning into generic templates | A visual personality derived from your content and taste |
| Web, PDF, Word, QR codes, and live links drifting apart | Cross-format, cross-language, cross-device release QA |
| Uncertainty about employer data or public claims | Clear keep, redact, defer-to-interview, or remove decisions |

## Quick start

### 1. Install

```bash
npx -y skills add xuehuafu233-alt/zane-career-skills -g --all
```

### 2. Tell your Agent where you are

If you do not know which Skill to use, start with the router:

```text
Use zane-career-assets.
I am applying for Head of Consumer Brand Marketing roles. I currently have an old resume,
several project files, and scattered metrics. Build a fact ledger and hiring position first,
then decide whether I need a resume, a portfolio website, or deep case studies.
Keep my voice. Do not use a fixed template or invent experience.
```

If the deliverable is already clear, call a specialist directly:

```text
Use zane-career-resume-builder to rebuild this resume for a senior product marketing role.

Use zane-career-portfolio-website-design to design a portfolio from my target role,
case evidence, writing voice, and visual references.

Use zane-portfolio-multi-format-qa to check desktop, 390px mobile, PDF, Word,
QR codes, and live links before release.
```

## How it works

```text
Your target role, experience, evidence, and taste
                       ↓
             Fact ledger and positioning
                       ↓
       Decide what belongs in resume / site / cases
                       ↓
          Content, structure, visuals, localization
                       ↓
          Web / PDF / Word / link release QA
                       ↓
              User approval, application, deploy
```

A generated file is not automatically application-ready. Candidate, user-approved, submitted, and deployed are separate states.

## Capabilities

| Goal | Main Skill | Typical output |
| --- | --- | --- |
| Decide which career assets you actually need | `zane-career-assets` | Fact ledger, positioning, asset roles, next step |
| Build the complete system from zero | `zane-career-portfolio-builder` | Resume, portfolio, cases, index, delivery state |
| Create or localize a resume | `zane-career-resume-builder` | Recruiter scan structure, multilingual copy, PDF QA |
| Design portfolio information architecture | `zane-career-portfolio-architecture` | Homepage hook, deep cases, work index, application entry |
| Build a distinctive portfolio website | `zane-career-portfolio-website-design` | Visual personality, page system, responsive implementation, QA |
| Turn work into credible case stories | `zane-career-case-editor-zh`, `zane-evidence-weighted-case-storytelling` | Decisions, actions, results, tradeoffs, evidence weight |
| Decide what employer data can be public | `zane-former-employer-data-redactor` | Keep, redact, defer, or remove decisions |
| Write the first application message | `zane-career-application-greeting` | Chinese or English outreach with the correct language entry |
| Validate a release candidate | `zane-portfolio-multi-format-qa` | Desktop/mobile, web/PDF/Word, QR, and link checks |
| Turn design references into an original direction | `zane-design-reference-to-prompt` | Design judgments, responsive rules, implementation prompt |

See the [Skill Inventory](docs/skill-inventory.md) for the complete scope.

## Why this is not a template

The repository ships decision methods, not Zane's resume, career path, website colors, or page layout.

Each run should be derived again from:

- target role, seniority, market, and hiring channel;
- verified experience, evidence strength, and publication boundaries;
- what the recruiter needs to see first and what can wait;
- the user's own writing voice, information density, and visual taste;
- the actual deliverables: web, PDF, Word, or a combination.

If two users get the same structure with only names and colors swapped, the method has not done its job.

## Install

### Recommended: install the complete collection

```bash
npx -y skills add xuehuafu233-alt/zane-career-skills -g --all
```

Then start with:

```text
Use zane-career-assets to decide which career asset I need first.
```

You can also call individual Skills. Exact installation paths and invocation syntax depend on your Agent.

## What to prepare

You do not need to organize everything before starting. A useful first pass needs:

- target role, level, and hiring market;
- an old resume or a rough experience summary;
- verifiable projects, actions, outcomes, and dates;
- examples of writing and visuals you like or dislike;
- what may be public and what should stay interview-only;
- the files or links you want at the end.

When evidence is missing, the Skills should leave an evidence gap, not invent a polished story.

## Method boundaries

- Never invent experience, metrics, clients, outcomes, or testimonials.
- Do not claim a full team result as an individual achievement.
- Not every complex fact belongs on a resume or homepage, but material misrepresentation, privacy, and compliance issues still matter.
- Do not let exhaustive auditing block a reversible next step, and do not replace judgment with disclaimers.
- A machine check is not the same as visual approval, user confirmation, submission, or a hiring result.

## Provenance and license

This collection grew from repeated problems, failed iterations, and verified improvements in real career-asset work. It contains no personal resume, employer source files, contact details, client data, or private local paths.

See [Provenance](docs/provenance.md) for source and third-party boundaries. Unless otherwise stated, the repository is released under the [MIT License](LICENSE).

Author: Zane
