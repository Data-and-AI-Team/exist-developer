# Engineering Process and AI Initiative — publication plan

## Objective

Prepare two Confluence spaces with navigable operating procedures:

1. **Engineering Process** — engineering delivery and operational controls.
2. **AI Initiative** — governance and delivery of AI-enabled solutions and AI-assisted engineering.

The engineering documentation must support the supplied evidence request: a screenshot of the internal documentation table of contents, or uploaded procedures covering pull requests, infrastructure configuration, coding standards, SDLC workflows, monitoring, testing, and incident handling.

## Current state and boundaries

- Target site: https://kb.exist.com, Confluence 9.2.3.
- The signed-in account was denied access to the space creation action. Space provisioning or permission confirmation is pending the administrator request.
- The local MCP connection is authenticated and read-only. This preparation does not change that configuration or publish anything.
- All content in this directory is a **draft for review**, not evidence that these practices are implemented. Named role holders, actual tooling, approval records, and adoption evidence must be confirmed before approval.
- No client records, credentials, production data, or sensitive incident details belong in these pages or screenshots.

## Proposed space structure

Suggested keys are provisional; confirm uniqueness with the administrator.

| Space | Suggested key | Home page source | Accountable role |
| --- | --- | --- | --- |
| Engineering Process | ENGPROC | contents/engineering-process/00-home.md | Engineering leadership |
| AI Initiative | AIINIT | contents/ai-initiative/00-home.md | AI initiative sponsor |

All numbered pages within a space are direct children of its home page. Numeric filename prefixes define publication order, not page title. Each home page provides the table of contents used for navigation and subsequent evidence collection.

## Phase 1 — review and operational alignment

- [ ] Assign a named space owner and procedure owner for each page.
- [ ] Validate procedures against actual repositories, delivery tools, infrastructure environments, monitoring, support coverage, and current contractual obligations.
- [ ] Confirm risk-based review, testing, incident, AI evaluation, and exception expectations with engineering, operations, security, and privacy stakeholders.
- [ ] Replace role references with an approved responsibility directory or named contacts where appropriate.
- [ ] Add actual internal links to repository templates, pipelines, dashboards, runbooks, service inventories, and approval registers.
- [ ] Record deviations from current practice as adoption actions; do not describe an unimplemented control as operational.
- [ ] Obtain accountable-owner approval and record approver, approval date, effective date, and next review date on each approved page.

## Phase 2 — space and permission readiness

- [ ] Administrator creates **Engineering Process** and **AI Initiative**, or grants and verifies the required global space-creation permission.
- [ ] Record actual space keys and home-page IDs.
- [ ] Set group-based access: internal readers, designated editors, and limited space administrators. Confirm anonymous access is disabled and external access matches the intended audience.
- [ ] Verify the publishing account can create and edit pages in both spaces; granting global space creation is unnecessary if administrators provision the spaces.
- [ ] Enable write access for the intended publishing session only after authorization. The current MCP setup is deliberately read-only.
- [ ] Confirm the available MCP tools support page creation/update. Space creation may require administrator UI or REST operations rather than an MCP tool.

## Phase 3 — publication

1. Publish the two home pages, then the numbered child pages in order. Preserve the draft notice until each page is approved.
2. Convert Markdown into a supported Confluence representation; validate headings, lists, tables, links, and code formatting rather than submitting raw Markdown as storage HTML.
3. Keep a publication manifest with source path, space key, page title, page ID, parent page ID, published source revision, and Confluence version. Do not store tokens in the manifest.
4. On subsequent runs, update manifest-mapped pages using the latest version number; do not create duplicate pages by title. Stop and resolve concurrent edits instead of overwriting them.
5. Replace relative Markdown links with the actual Confluence page links. Insert a native table-of-contents macro on long pages and a children/page-tree macro on home pages if supported.
6. Apply labels: `engineering-process` or `ai-initiative`, plus the lifecycle label `draft` or `approved` as appropriate.
7. Verify every page's space, parent, content, status, permissions, and links in Confluence. Validate visibility using the intended reader access.

## Phase 4 — adoption and evidence

- [ ] Run a representative change through the engineering workflow and link the actual PR, test report, release record, and relevant operational evidence.
- [ ] Exercise incident response and recovery through a real incident or clearly identified tabletop exercise.
- [ ] For an AI pilot, link its actual use-case approval, data review, evaluation report, and go/no-go decision.
- [ ] Open the Engineering Process home page with the full table of contents visible. Capture a screenshot showing the site/space identity and all required procedure categories.
- [ ] Immediately open and inspect each screenshot; retake unreadable, incomplete, or cropped captures before proceeding.
- [ ] Capture a second image if one readable image cannot show all entries. Check the images contain no sensitive content.
- [ ] Export approved procedures if the evidence request requires documents instead of screenshots.
- [ ] Submit only reviewed, accurate evidence. A screenshot demonstrates documentation availability, not implementation effectiveness or certification.

## Acceptance criteria

- Both spaces exist with approved access and an identifiable owner.
- Each home page links to all its child pages; no unresolved local links remain.
- Engineering Process explicitly covers every procedure category in the evidence requirement.
- AI Initiative covers intake, permitted use, data protection, evaluation, deployment, and incident handling.
- Approved pages have owner, approver, effective date, and review date; unapproved pages remain clearly marked draft.
- Publishing is repeatable without duplicate pages or overwritten concurrent edits.
- The evidence screenshot is legible and accurately represents the published documentation.

## Local sources

See [contents/README.md](contents/README.md) for the source inventory. The ignored credential file is used by the local launcher only; never upload it to Confluence.