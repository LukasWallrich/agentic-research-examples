# Collabra: Psychology (University of California Press; e-ISSN 2474-7394)

All sources accessed 2026-09-27.

**Sources and how they were read**
- Submit page: https://online.ucpress.edu/collabra/pages/submit. Links to the guidelines Google Doc and the Scholastica submission system.
- Submission guidelines (Google Doc linked from the Submit page): https://docs.google.com/document/d/1WpA8_6Ko0-jmcqFZythDB7aA51pDRgsRblnL-LkSZJc/. Exported as plain text with curl; quotes are verbatim. Local copy: `scratch_collabra_guidelines.txt`.
- Journal Policies: https://online.ucpress.edu/collabra/pages/journalpolicies. Also covers the Transparency and Openness policy and section policies.
- Publication Fees: https://online.ucpress.edu/collabra/pages/publicationfees
- About: https://online.ucpress.edu/collabra/pages/About
- Editorial Team: https://online.ucpress.edu/collabra/pages/editorial
- UC Press AI Guidelines: https://www.ucpress.edu/about/ai-guidelines. Fetched with curl; quotes are verbatim. Local copy: `scratch_collabra_ai.txt`.
- Registered Reports detailed guidelines (.docx on Google Drive, linked from the guidelines): https://drive.google.com/file/d/1mApMxCmFH2GFd3m-qiw89y6rLjUDRDdY/view. Local copy: `scratch_collabra_rr.txt`.
- online.ucpress.edu pages return 403 to curl and WebFetch (Cloudflare). I read them in a real browser tab and extracted `document.body.innerText`, so these quotes are verbatim from the rendered page.

---

## 1. Article types, fit, length, reference style

**Article types** (guidelines doc, "Article Types"):
- "Original research reports: These should present original findings. Null/negative findings, reanalyses of previous studies with new results, replication studies, and registered reports are also considered."
- Review articles
- Perspective / Opinion articles
- Registered Reports
- Commentary

The Journal Policies page ("Section Policies") lists only four types: Original research report, Review article, Perspective/Opinion, and Registered report.

The About page says: "Collabra: Psychology publishes empirical papers as well as review papers and meta-analyses, theory papers, methods papers, simulations, commentaries (including opinion pieces and critiques of other published papers), and data papers. We are also open to other non-traditional submission types."

**Best fit: Original research report.** This type explicitly names "reanalyses of previous studies with new results". The About page also names "simulations" as a publishable type.

**Registered Report route: not available for this manuscript.**
- There is no route for a Stage 2 submission without Stage 1. In the Collabra RR guidelines, Stage 1 review and in-principle acceptance (IPA) must come before the analyses.
- Secondary-data RRs exist, but they require no prior access to the data: "The journal welcomes submissions proposing secondary analyses of existing data sets, provided authors can supply sufficient evidence (e.g. self-certification; letter from independent gatekeeper) to confirm that they have had no prior access to the data in question nor to summary reports of the data through descriptive or inferential statistics or narrative descriptions of the data, in talks, papers, or personal communication with others)." (RR detailed guidelines, "Secondary Registrations")
- At Stage 2, authors of secondary RRs "should confirm that no data (other than pilot data included at Stage 1) was subjected to the pre-registered analyses prior to IPA".
- Collabra is also "PCI:RR-friendly" (guidelines doc). The PCI RR route also needs a Stage 1 recommendation before the analyses, so it does not apply to a completed study.

**Sections** (Journal Policies, "Focus and Scope"): Cognitive Psychology; Social Psychology; Personality Psychology; Clinical Psychology; Developmental Psychology; Organizational Behavior; Methodology and Research Practice.
- **Recommended: Cognitive Psychology.** This manuscript tests cognitive process models of anchoring. The Senior Editor is Nathan Evans (University of Liverpool). The Associate Editors include Michael Schulte-Mecklenbeck (University of Bern).
- **Alternative: Organizational Behavior.** Its Associate Editors include JDM researchers Don Moore (UC Berkeley Haas) and George Wu (Chicago Booth).
- Source: https://online.ucpress.edu/collabra/pages/editorial. The editors' research areas are my inference, not stated on the page.

**Length:** "We do not have arbitrary restrictions on manuscript length. However we do not accept monographs, and we do ask you to employ a clear and concise writing style."

**Abstract:** "Abstracts should not exceed 300 words, and should not include sub-headings." Also: "Please do not include citations in your abstract and avoid the use of abbreviations, if possible."

**Title:** "The full title must be 250 characters or fewer."

**Reference style:** APA. "The style of the Publication Manual of the American Psychological Association, must be followed with respect to handling of references." The submission checklist requires DOIs: "All DOIs for the references have been provided, when available."

**Format constraints for the Quarto workflow:**
- "You may submit your manuscript files in Microsoft Word (.doc or .docx), Open Office, LaTeX (as .pdf), or RTF format. Only RTF and .doc/.dox files can be used during the production process."
- A PDF is fine for review. After acceptance, a .docx render is needed, or the .tex files for a LaTeX route.
- Figures must be embedded in the text and also uploaded separately as JPEG. The checklist says: "at least 150dpi (300dpi or above preferred)".
- Tables are embedded in the text.
- Figures need alt text, placed "below the actual figure legend". Accessibility Requirements doc: https://docs.google.com/document/d/1wFn3sWrNdjN9htiNdtZbO6eDvvVuC_2muxlizvcvRUY/edit

## 2. Required sections and statements

Guidelines doc, "Manuscript Organization": "All submissions should begin with the following sections: Title, Abstract". "All submissions should end with the following sections":
- References
- Contributions
- Acknowledgements (if applicable)
- Funding information (if applicable)
- Ethics statement
- Competing interests ("mandatory, even if to state that no competing interests exist")
- Supplemental material (if applicable)
- Data accessibility statement ("mandatory")
- Figure titles and legends (if applicable)

**Contributions / CRediT:** "Please indicate author contributions as clearly as possible. One option to do so is through the Contributor Role Taxonomy, or CRediT (see https://credit.niso.org/)." CRediT is optional. The alternative is an ICMJE-style list.

**Data / code (mandatory), from the guidelines doc and the Journal Policies page:**
- "Authors reusing data available from public repositories must provide program code, scripts for statistical packages, and other documentation sufficient to allow an informed researcher to precisely reproduce all published results."
- "We require that authors include a 'data accessibility statement' (DAS) with their submission."
- Journal Policies, Citation Standards: "All data sets and program code used in a publication must be cited in the text and listed in the reference section. References for data sets and program code must include a persistent identifier, such as a Digital Object Identifier (DOI)." OpAQ and the analysis code therefore both need DOI citations.
- "Dissemination of data, methods, and materials can be delayed until article publication, as long as reviewers have adequate access."
- Design transparency (APS standard): disclose "any data exclusions", "all of the conditions/groups tested", and "all of the dependent variables or measures collected for each study".

**Preregistration** (Journal Policies):
- "Collabra: Psychology encourages, but does not require, preregistration of studies."
- Placement rule: "Authors should state in the Acknowledgements section whether the conducted research was preregistered with an analysis plan in an independent, institutional registry ... and that the preregistration adheres to the disclosure requirements of the institutional registry. If the conducted research was preregistered, authors must provide links to the time-stamped pre-registration(s) at the institutional registry."
- No open-science badges are mentioned on any page I read.

**Funding:** "Please provide a list of the sources of funding, as well as the relevant grant numbers, where possible. ... You will also enter this information in a form during the submission process, but it must be repeated here."

**Competing interests:** "Corresponding authors must provide a statement of competing interests on behalf of all authors, and, if no competing interests exist, state this specifically."

**Ethics statement:**
- The rule is written for primary research: "All research involving human participants must have been approved by the authors' Institutional Review Board (IRB) ... Please explicitly state that ethics approval was obtained in this section."
- Suggested wording: "either 'IRB approval for this study was obtained (#<SOME NUMBER>) by <SOME INSTITUTION>.' or 'This study did not involve testing of human participants'".
- Judgment call: the second suggested sentence fits literally. A more precise version would be a sentence stating that this is a secondary analysis of openly licensed (CC-BY 4.0), de-identified data collected under the original studies' approvals.

**Anonymisation:** "Manuscript (required, author names and affiliations must be masked for a double-blind review process)". Names and affiliations go on a separate title page. The Journal Policies page also allows "Non-blind peer-review, meaning that reviewers can sign their reviews."

**Not mentioned in the guidelines doc or on the Journal Policies page:** keywords, running head, significance/public statement. Keywords may be requested in the Scholastica form, which requires login. UNVERIFIED.

**Transparent peer review:**
- Journal Policies: "Whether double-blind or non-blind, Collabra:Psychology utilizes an open peer review process. This means that the correspondence and comments during the review process will be openly available in a single document along with the published article, if accepted."
- Inconsistency: the same page's Focus and Scope section says "an option for authors to choose open peer review". So open review is either mandatory or opt-in, and the pages disagree.
- About page: "We also share the value created by the psychology community in the peer review process, by publishing the content of editors' and reviewers' comments along with each published article."
- No reviewer payment or reviewer-reward scheme is described on the current pages.
- The journal is "an official publication of the Society for the Improvement of Psychological Science (SIPS)".

**Other routes (guidelines doc):**
- PCI:RR-friendly.
- PCI:Psych "category 2 friendly".
- MetaROR partner: "authors can submit the peer review history with MetaROR along with their manuscripts and Collabra commits to providing streamlined review".
- Streamlined review after rejection elsewhere, within the previous 365 days (Journal Policies).
- Automated checks: "Collabra: Psychology is currently investigating the use of tools in the peer review process to enhance scientific rigor. ... Your manuscript may undergo additional checks as part of this study."

## 3. AI policy (verbatim)

**Journal level** (guidelines doc, "AI Policy"). This is the entire section: "Collabra: Psychology follows the AI policy of UC Press. See here for more information." The link goes to https://www.ucpress.edu/about/ai-guidelines. The journal adds no text of its own.

**Publisher level:** "UC Press Guidelines on the Use of AI Tools by Authors, Peer Reviewers, and Freelancers", dated on the page "as of July 31, 2025".

Scope: "These guidelines and policies represent UC Press's expectations for content creators (e.g. book authors, authors of journal articles, and authors of other works published by UC Press) ... These guidelines and policies are generally applicable to those working with UC Press throughout the publishing process; however, in some cases, they have been adapted by specific groups such as journal editorial teams."

"Content Creators" section, complete:
> "Authors are responsible and legally accountable for the content of their work. AI tools may not be credited or attributed as an author on any work published by UC Press. Any content generated by artificial intelligence does not meet the requirements of authorship. AI-assisted improvements to human-generated texts for readability, formatting, and style, and to ensure that the texts are free of errors in grammar, spelling, punctuation and tone are permitted. However, authors who use AI tools to produce text or images/graphics, or to collect or process data, must inform their editors of this use and be transparent about it in their manuscripts so that readers understand the role of these tools in the development of the work. The author is fully responsible for the entirety of their work. They must ensure that it is original, accurate, does not plagiarize others' work, and appropriately cites and references others' work, including any content that is generated by AI."

Closing paragraph (excerpt): "We will continue to revisit and revise these guidelines as the tools and technologies develop."

**Answers to the brief's questions:**
- **Can AI be an author?** No. "AI tools may not be credited or attributed as an author on any work published by UC Press."
- **Is AI-generated text or analysis allowed with disclosure?** Yes, by implication. The policy does not prohibit it. It requires disclosure when AI is used "to produce text or images/graphics, or to collect or process data". Light editing of "human-generated texts" needs no disclosure.
- **Where must disclosure be made?** In two places: to the editors ("must inform their editors") and in the manuscript ("be transparent about it in their manuscripts so that readers understand the role of these tools"). The policy names no specific section, such as Methods or Acknowledgements.
  - The cover letter is the only channel the guidelines describe for telling the editor.
  - I could not check whether the Scholastica submission form has an AI-disclosure question (login required). UNVERIFIED.
- **Is a substantially AI-generated manuscript prohibited?** No such prohibition is stated. The limit is authorship: "Any content generated by artificial intelligence does not meet the requirements of authorship." Also, "The author is fully responsible for the entirety of their work."
  - Unresolved ambiguity: the policy assumes a human author who writes the work. It does not address a manuscript in which the AI designed the study, ran the analyses, and wrote the text, with the human in a supervisory role. Whether the human's contribution qualifies him as author of "the entirety of their work" is an editorial judgment the policy does not settle.
- **COPE:** The AI page does not mention COPE. The Journal Policies page says: "Collabra: Psychology supports the principles of the Committee on Publication Ethics (COPE) and follows its guidelines for dealing with potential cases of misconduct. We expect our authors to comply with best practices in publication ethics, particularly with respect to authorship..." COPE's own AI position statement was not fetched, because neither Collabra nor UC Press refers to it for AI.
- **Levels:** The journal defers to UC Press in full. The two levels do not differ. The UC Press page allows journal-specific adaptation, but Collabra has published none.

## 4. APC / open-access model

Source: Publication Fees page.

**Model:** fully (gold) open access with an APC.
- "Collabra: Psychology is a fully open access journal ... the University of California Press charges a flat article processing charge (APC) of $1,450." The currency is USD, implied by "$".
- Licence (guidelines doc, Copyright Notice): authors keep copyright, and articles are published under "a Creative Commons Attribution License" (link to CC BY 4.0).

**Discounts and waivers:**
- **SIPS member discount:** "Active members of the Society for the Improvement of Psychological Science (SIPS) are entitled to a $475 APC discount if their submissions are made prior to July 1, 2026." That date has passed. The discount no longer applies to new submissions unless the page is updated.
- **UC system:** fees are waived for University of California corresponding authors.
- **Low and middle-income countries:** Research4Life Group A and B affiliations "are currently automatically offered a 75% discount".
- **Fee waivers:**
  - Waivers must be requested "during the submission process". They "will not be considered in editorial decisions". They "will not be granted once an article has been accepted".
  - They are limited to "two waivers per corresponding author per open-access journal per year".
  - "Authors are expected to pursue and exhaust other funding options before requesting an APC waiver".
  - The guidelines doc adds: "Editorial decisions are made independently from the ability to pay the APC."

## 5. Fit: recent related articles (DOIs verified with the Crossref command from the brief)

| DOI | Title (as returned by Crossref) | Journal | Year | Relevance |
|---|---|---|---|---|
| https://doi.org/10.1525/collabra.126223 | Anchoring, Confirmation and Confidence Bias Among Medical Decision-makers | Collabra: Psychology | 2024 | Anchoring |
| https://doi.org/10.1525/collabra.128514 | The Role of Numeracy in Judgment and Decision Making: The Replication of Eleven Effects Across Various Numeracy Scales | Collabra: Psychology | 2025 | JDM effects; replication |
| https://doi.org/10.1525/collabra.35271 | Many Labs 4: Failure to Replicate Mortality Salience Effect With and Without Original Author Involvement | Collabra: Psychology | 2022 | Multi-lab study. This is primary data collection, not a secondary analysis. |

- Crossref searches restricted to ISSN 2474-7394, 2021 onwards, found no computational or process-model paper on anchoring or judgment.
- Other JDM replications from 2023–2025 also appear, such as hindsight bias (10.1525/collabra.147499) and outcome bias (10.1525/collabra.126266). I did not verify these with the individual Crossref check.

## 6. Cover letter

**Current guidelines doc:**
- The cover letter is listed as "Cover letter (optional)".
- The same doc also says: "Please note that Collabra: Psychology has an important Transparency and Openness policy for its articles—please read this policy in full and acknowledge your understanding of it in your cover letter."
- The Journal Policies page ("Streamlined Review") refers to "the other standard items required in the cover letter, listed here". That link points to collabra.org/about/submissions/, which no longer resolves.
- Result: the current pages contradict each other. A cover letter is formally optional, but in practice it is expected.

**Archived list** (Wayback snapshot of 2020-09-30: http://web.archive.org/web/20200930224518/https://www.collabra.org/about/submissions/). This is historical and may not reflect current requirements. The list asked for "an approximately one-page cover letter" that:
- "briefly summarizes how your paper is a worthy contribution to the scientific literature"
- "specifies the section your submission best pertains to"
- "specifies the type of article you are submitting"
- "acknowledges you have read the Transparency and Openness policy of our Editorial Policies"
- "specifies whether you are opting for open peer review"
- "suggests appropriate or opposed reviewers"
- "details any previous interactions with Collabra: Psychology regarding your submission"
- "indicates, if applicable, that the article is submitted as part of a Research Nexus/Special Collection"

**Recommended cover letter content:**
- all of the items above
- the AI-use disclosure to the editors that the UC Press policy requires
- a request for streamlined or MetaROR review, if applicable

---

## Fit assessment

**Scientific fit: good.**
- Collabra judges manuscripts on rigour, not novelty.
- It names "reanalyses of previous studies with new results" and "simulations" as publishable types.
- It requires open code for reused public data, which this project already provides.
- It is a SIPS journal with a strong open-science profile, and its Cognitive Psychology and Organizational Behavior boards include JDM researchers.
- It has published anchoring and JDM replication work.
- It has no length limit. The abstract limit is 300 words, and APA style applies.
- Practical costs:
  - USD 1,450 APC. The SIPS discount expired on 1 July 2026.
  - A .docx render is needed for production.
  - Open peer review: the review history is likely to be published with the article.

**AI-authorship risk: moderate to high.**
- The journal applies the UC Press policy unchanged.
- That policy bars AI authorship and requires disclosure of AI-produced text and data processing, both to editors and in the manuscript. It does not prohibit AI-generated manuscripts.
- The risk comes from two sentences:
  - "Any content generated by artificial intelligence does not meet the requirements of authorship."
  - "AI-assisted improvements to human-generated texts ... are permitted."
- Both assume human-written text. A manuscript that is designed, analysed and written by Claude, under supervision, goes beyond the use the policy explicitly permits. An editor could read the policy as leaving no human-generated content that meets the authorship requirements.
- The review history will be public, so any debate about AI authorship would also be public.

**Recommendation:**
- Before submitting, send a query to the Editor-in-Chief (Don van Ravenzwaaij) describing the AI role.
- If they agree to consider the manuscript:
  - List Lukas Wallrich as sole author.
  - Describe Claude's role in full in the Methods and the Contributions statement, plus the cover letter.

Scratch files for this journal: `/Users/lukaswallrich/Documents/Coding/ai-jdm-paper/scoping/scratch_journals/scratch_collabra_*`.
