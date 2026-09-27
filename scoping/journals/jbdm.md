# Journal of Behavioral Decision Making (JBDM)

Wiley; ISSN 0894-3257, e-ISSN 1099-0771. All sources accessed 2026-09-27.

**Sources**

- **[JBDM-AG]** JBDM Author Guidelines, https://onlinelibrary.wiley.com/page/journal/10990771/homepage/forauthors.html. The page returns HTTP 403 (Cloudflare bot check) to curl, WebFetch and r.jina.ai. The live text was captured through a real Chrome session (codex Chrome plugin) into `scratch_jbdm_live_forauthors.txt`. A Wayback snapshot of 2024-10-13 (http://web.archive.org/web/20241013030947/https://onlinelibrary.wiley.com/page/journal/10990771/homepage/ForAuthors.html) differs from the live text only in three ways. A line diff of the two stripped texts shows: the portal is renamed ("Research Exchange" to "Wiley Authors"), and the live page adds two sections ("Refer and Transfer Program", "Continuous Publication"). Table formatting differs, but the table content is the same.
- **[W-ETH]** Wiley, Best Practice Guidelines on Research Integrity and Publishing Ethics, https://authors.wiley.com/ethics-guidelines/index.html (redirected from https://authorservices.wiley.com/ethics-guidelines/index.html). Fetched with curl.
- **[W-AI]** Wiley, AI guidelines ("A guide for research authors, editors, and reviewers"), https://www.wiley.com/en-gb/publish/article/ai-guidelines/. Fetched with curl. The page shows no "last updated" date. Its own methodology note refers to drafting in July–August 2025.
- **[W-DATA]** Wiley Data Sharing Policy, https://authors.wiley.com/author-resources/Journal-Authors/open-access/data-sharing-citation/data-sharing-policy.html. Fetched with curl.
- **[W-APC]** Wiley hybrid OA price list, https://authors.wiley.com/asset/Wiley-Journal-APCs-OnlineOpen.xlsx (linked from https://authors.wiley.com/author-resources/Journal-Authors/open-access/article-publication-charges/index.html). The file says "Updated: 2 September 2026".
- **[COPE]** COPE position statement "Authorship and AI tools". The live URL (https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools) returns 403. Text taken from the Wayback snapshot of the earlier URL, 2024-09-21: https://web.archive.org/web/20240921062544/https://publicationethics.org/cope-position-statements/ai-author. **The current wording is UNVERIFIED.**

## 1. Article types, length, abstract, reference style

- **One article type only** [JBDM-AG, live]: "Research Articles | reports of new research findings or conceptual analyses that make a significant contribution to knowledge | 10,000 limit | Yes, Structured | Data Availability Statement / IRB Statement".
- **No registered reports, brief reports or research notes are listed** [JBDM-AG, live]. Crossref searches (ISSN 0894-3257, 2021 onwards) for "registered report" returned 0 results. The Crossref result is weak evidence because the API also returned 0 for "replication" in the same session.
- **Fit:** this manuscript is a "Research Article". The preregistration can be reported in the text, but the journal has no RR track.
- **Word limit:** "10,000 limit". The page does not say what the count includes.
- **Abstract:** the page gives two instructions that do not agree. The main-text list says "Abstract of up to 250 words;". The article-types table says "Yes, Structured". The page does not say what headings a structured abstract needs. Ask the editorial office or check recent JBDM articles.
- **Keywords:** "Up to six keywords;".
- **Main body:** "Main body: formatted as introduction, materials & methods, results, discussion, conclusion;".
- **Reference style:** "This journal uses the Publication Manual of the American Psychological Association reference style." The page does not name an edition. APA 7 is the current edition.
- **File format:** "The main manuscript file can be submitted in Microsoft Word (.doc or .docx) or LaTex (.tex) format." A LaTeX submission also needs a PDF. A Quarto project can render to .docx or .tex.
- **Preprints:** "This journal accepts articles previously published on preprint servers." and "You may also post the submitted version of a manuscript to a preprint server at any time."

## 2. Required sections and statements

All quotes are from [JBDM-AG, live] unless marked otherwise.

- **Title page:** "i. A brief informative title containing the major key words. The title should not contain abbreviations ... ii. A short running title of less than 40 characters; iii. The full names of the authors; iv. The author's institutional affiliations ... Include a 50-word biographical sketch of each author; v. Acknowledgments. Include the name(s) of any sponsor(s) of the research contained in the paper, along with grant number(s);"
- **Masked review:** none. "This journal operates under a single-blind peer review model." No anonymisation is needed. The main document itself must include author names, affiliations and 50-word biographical sketches.
- **Desk screening:** "Papers will only be sent to review if the Editor-in-Chief determines that the paper meets the appropriate quality and relevance requirements."
- **Data availability:** "This journal expects data sharing. Review Wiley's Data Sharing policy where you will be able to see and select the data availability statement that is right for your submission." The "expects" level [W-DATA] means: "The journal expects that data supporting the results in the paper will be archived in an appropriate public repository. Authors are required to provide a data availability statement for research- and synthesis-based articles to describe the availability or explain the absence of shared data. When data have been shared, authors are required to include in their data availability statement a link to the repository they have used, and to cite the data they have shared. Whenever possible the scripts and other artefacts used to generate the analyses presented in the paper should also be publicly archived."
  - Matching template [W-DATA], "Data derived from public domain resources": "The data that support the findings of this study are available in [repository name] at [URL/DOI], reference number [reference number]. These data were derived from the following resources available in the public domain: [list resources and URLs]". Cite OpAQ as data ("Please review Wiley's Data Citation policy" [JBDM-AG]).
- **Preregistration and open science badges:** not mentioned on the author-guidelines page. The words "preregist", "badge", "registered report" and "CRediT" do not appear in the live text.
- **CRediT:** not required by JBDM. [W-ETH] only describes CRediT: "CRediT (Contributor Role Taxonomy) is a community-owned 14-role taxonomy that can be used to describe the key types of contributions typically made to the production and publication of research."
- **Authorship:** "All listed authors should have contributed to the manuscript substantially and have agreed to the final submitted version."
- **ORCID:** "This journal requires ORCID."
- **Conflicts of interest:** "You will be expected to declare all conflicts of interest, or none, on submission."
- **Funding:** "You should list all funding sources in the Acknowledgments section."
- **Ethics / IRB statement:** "The journal requires that you include in the manuscript details IRB approvals, ethical treatment of human and animal research participants, and gathering of informed consent, as appropriate." The article-types table lists "IRB Statement" as a requirement for Research Articles. For secondary data, [W-ETH] "Retrospective studies" says: "Retrospective studies are typically based on already available data sets or samples. ... In such studies, authors must consult with their institution's requirements to determine the most appropriate course of action. If ethical approval is not required or has been formally waived by an institutional ethics committee, authors must clearly state this in their manuscript." So the manuscript needs an explicit IRB statement, for example an exemption or waiver from Lukas's institution, or a statement that approval was not required, with the reason.
- **Significance or public statement:** none required.
- **Figures and supporting information:** "Figures, supporting information, and appendices should be supplied as separate files." At initial submission, figures may sit inside the main file.
- **COPE:** "This journal follows the core practices of the Committee on Publication Ethics (COPE)".

## 3. AI policy (verbatim)

**The journal level has no AI text.** The live JBDM author-guidelines page has no AI section. "Artificial" occurs nowhere in the text. JBDM therefore defers to the Wiley publisher-wide policy [W-ETH, W-AI]. Wiley in turn cites COPE for the authorship rule.

### Can AI be an author? No.

- [W-ETH], "AI & Authorship": "AI Technology is not considered capable of initiating an original piece of research without human direction. Such tools cannot be held accountable for published work or for research design, which are both requirements of authorship (as discussed in the Authorship section in these guidelines). AI Technology also lacks legal standing and cannot hold or assign copyright. Therefore, in accordance with COPE's position statement on Authorship and AI tools these tools cannot fulfil the role of an author and must not be listed as one on an article."
- [W-AI] quotes a slightly different version of the same rule: "these tools cannot fulfil the role of, nor be listed as, an author of an article."
- [COPE] (2024 snapshot; current text UNVERIFIED): "COPE joins organisations, such as WAME and the JAMA Network among others, to state that AI tools cannot be listed as an author of a paper. AI tools cannot meet the requirements for authorship as they cannot take responsibility for the submitted work. As non-legal entities, they cannot assert the presence or absence of conflicts of interest nor manage copyright and license agreements."

### Is AI-generated text or analysis allowed with disclosure? Yes, with human oversight. There are restrictions.

- [W-ETH], "General Guidance & Best Practice": "When used responsibly, AI Technology can help authors maintain high editorial standards ... We welcome the responsible use of AI technology ... Authors remain fully accountable for their submissions and any tools or sources they use."
- [W-ETH], "Human Oversight": "Authors may only use AI Technology as an additional tool in their writing process, not a replacement for their own expertise and judgement. As always, authors remain fully responsible for the accuracy of all content and must verify that all claims, citations, and analyses align with their expertise and research. Before including AI-generated content in a journal submission, authors must carefully review it to ensure the final work reflects their own expertise, voice, and originality and that it complies with Wiley's ethical and editorial standards."
- [W-AI], "Human oversight", gives a parallel version: "Authors may only use AI Technology as a companion to their writing process, not a replacement."
- [W-AI], copyright FAQ ("How does AI use affect copyright protection of my research?"):
  - "Your methodology, analysis, and conclusion must demonstrate that you directed the work using your expertise, made final decisions about content, and maintained intellectual control throughout the research process."
  - "Your manuscript must demonstrate that the substance and expression of the work are yours, with AI serving only as assistant at your direction."
- [W-AI], best practice: "When possible, use AI for editing and refining your own work rather than generating entirely new content"
- [W-AI], FAQ "Maintaining intellectual leadership with AI Technology". This is guidance ("your role is to"), not a "must": "Think of AI as a research assistant working under your direction ... When working with AI, your role is to: - Define your goals and expectations for your AI collaboration - Provide directions to the AI based on your specific needs - Evaluate outputs using your domain knowledge - Seek input from AI, then implement changes in the work yourself - Make final decisions about what to include in your work - Disclose your use of AI transparently in your manuscript so readers can understand your process"
- **Editor's discretion** [W-ETH]: "The final decision on whether using AI Technology is appropriate or permissible for a submitted manuscript or a published article belongs to the journal's editor or other party responsible for the publication's editorial policy."

### Disclosure: what, where, how

- [W-ETH], "Disclosure": "Authors should document all AI Technology used, including its purpose, whether it influenced key arguments or conclusions, and how they personally reviewed and verified any AI-generated content. Authors must also disclose their use of AI Technologies when submitting a manuscript to a Wiley journal. If disclosure is not provided at submission, it may be requested during peer review or after publication."
- [W-ETH], "Specific guidance": "If an author has used AI Technology to substantially edit, develop, or translate any part of a manuscript, its use must be described transparently and integrated into the manuscript as described in our guidance on disclosure and declaration of AI use. AI Tools used solely for spelling, grammar, and general editing are not included in these disclosure requirements."
- **Location** [W-AI], "Where should I disclose AI use in my manuscript?": "For journals published by Wiley, AI disclosure should be placed in the following sections of your manuscript:
  - In your Acknowledgments when AI assists with manuscript drafting, editing, translation, or formatting.
  - In your Methods when AI is used to assist with your research methodology, data collection or analysis, or literature review processes.
  - In your figure captions when AI generates or edits any visual content that appears in your manuscript."
- **Drafting** [W-AI]: "Wiley requires disclosure of AI when used to generate substantial text or restructure arguments." Rows that need disclosure include "Text generation: AI generates or substantially rephrases text for the manuscript; creates first drafts of standard sections" and "Argument and logic: AI identifies gaps in argument structure; provides feedback on whether results follow from methods; ensures discussion connects to findings".
  - Recommended content of the Acknowledgments disclosure: "AI Technology name and version / Date/year of use / The AI Technology's role in your work ... / Specific sections where the AI was used in the document / The author's role in directing or reviewing the work of the AI Technology".
- **Methodology** [W-AI]: "Wiley requires disclosure when AI is used in your research methodology, including study design and data collection, literature review, code development, and data analysis." Rows that apply to this manuscript:
  - "Programming: AI writes analysis scripts or algorithms"
  - "Modeling: AI develops or adapts computational or statistical models for research analysis"
  - "Data pipeline design: AI builds automated workflows to clean, process, and integrate datasets"
  - "Quantitative/statistical analysis: AI performs statistical analyses, flags outliers that alter conclusions, interprets results of tests"
  - "Exploratory or advanced analyses: AI generates interpretations of results, highlights relationships or trends in data, or synthesizes findings across datasets"
  - "Agentic search: AI independently generates or executes search strategies"
- **Required Methods content** [W-AI]: "When disclosing AI use in your methods, we require that you share: AI Technology name and version / Date/year of use / The AI Technology's role in your work (image processing, code development, statistical analysis, etc.) / The author's role in directing or reviewing the work of the AI Technology / For sensitive, proprietary, or human subject data describe how privacy and compliance requirements were maintained".
- **Supplementary documentation** [W-AI]: "If AI contributed substantially to your analysis or methodology, you may be asked to provide supplemental documentation to support reproducibility and transparency, such as: Prompts or parameters used / AI settings or configurations / Code repository / Data protection approach / Compliance with institutional requirements".
- **Submission form and cover letter:** [W-ETH] says disclosure is required "when submitting a manuscript". Neither Wiley page names a specific submission-form field or the cover letter. Whether the Wiley Authors portal has an AI question is UNVERIFIED; the portal was not inspected.

### Levels of policy

JBDM has no journal-level AI text. The Wiley pages [W-ETH, W-AI] ban AI authorship "in accordance with COPE's position statement". Both Wiley and COPE require disclosure, but they name different places:

- **COPE:** disclose "in the Materials and Methods (or similar section) of the paper", including for writing.
- **Wiley:** disclose writing help in the Acknowledgments and methodological use in the Methods.

Wiley adds rules that COPE does not have:

- **Human-oversight rule:** AI may be used only "as an additional tool ... not a replacement".
- **Rights rule:** the AI provider must not gain training rights over the content.

## 4. APC / open access model

- **Model:** hybrid. [JBDM-AG, live]: "This journal is a subscription journal that offers an open access option. You'll have the option to choose to make your article open access after acceptance, which will be subject to an APC."
- **APC** [W-APC, "Updated: 2 September 2026"]: row "Journal of Behavioral Decision Making | Decision Sciences | 10990771 | CC BY, CC BY-NC or CC BY-NC-ND | USD 3960 | GBP 2690 | EUR 3290".
- **Currency:** by location. The price is charged "the US Dollar, Euro or GB Pound rate dependent on the corresponding author's location" (https://authors.wiley.com/author-resources/Journal-Authors/open-access/article-publication-charges/index.html). A UK corresponding author pays GBP 2,690. A Wiley transformational agreement at the author's institution may cover this.
- **Licences:** "This journal uses the CC-BY/CC-BY-NC/CC-BY-NC-ND Creative Commons License." [JBDM-AG].
- **Journal OA page:** https://onlinelibrary.wiley.com/page/journal/10990771/homepage/fundedaccess.html. Its text was not captured (Cloudflare 403; the browser session was interrupted). Journal-specific waivers or discounts on that page are UNVERIFIED. The APC figures above come from the Wiley price list.

## 5. Fit: recent JBDM articles (DOIs verified with the Crossref command from the brief)

1. **10.1002/bdm.2231**: "Perceptual anchoring and adjustment", Journal of Behavioral Decision Making, 2021 (published [[2021, 1, 7]]). This is a direct anchoring-and-adjustment topic match.
2. **10.1002/bdm.2317**: "How the anchor moves: Measuring and comparing the anchoring bias in autistic and neurotypical individuals", Journal of Behavioral Decision Making, 2023 (published [[2023, 1, 5]]).
3. **10.1002/bdm.70069**: "Anchoring Bias in the Tradeoff Procedure Within Multi‐Attribute Value Theory", Journal of Behavioral Decision Making, 2026 (published [[2026, 2, 23]]).
4. **10.1002/bdm.70087**: "Dissociations of Cognitive Control and Reward Sensitivity on Decision‐Making Under Uncertainty in Adolescents: Insights From Computational Modeling", Journal of Behavioral Decision Making, 2026 (published [[2026, 7, 28]]). This is an example of computational modelling in the journal.

5. **10.1002/bdm.2286**: "Revisiting the effect of incentivization on cognitive reflection: A meta‐analysis", Journal of Behavioral Decision Making, 2022 (published [[2022, 5, 17]]). This is an example of a secondary synthesis of existing data.

## 6. Cover letter

- **Not required.** The live author-guidelines page does not mention a cover letter [JBDM-AG]. Whether the Wiley Authors portal has an optional cover-letter field is UNVERIFIED; the portal was not inspected.
- **Recommended:** include one anyway. The EiC desk-screens for "quality and relevance". The AI role should be stated up front because disclosure is due "when submitting".

## Fit assessment

- **Topic fit is good.** JBDM regularly publishes anchoring work (three verified articles 2021–2026) and computational-modelling studies. A preregistered process-model test of anchor extremity on a large open trial-level dataset matches the "Research Article" type (10,000 words, APA style, single-blind review). The "expects data sharing" level fits the fully open OpAQ data and R code.
- **Formal gaps:**
  - The journal has no registered report track and no badges, so the preregistration counts only as a reporting feature.
  - The abstract instructions conflict: 250 words versus "Structured".
  - An explicit IRB or exemption statement is needed even though the data are secondary.
- **AI authorship is the main risk.** Wiley bans AI as an author, so Claude cannot be listed. Disclosure is clearly allowed: in the Methods for design, code, modelling and analysis, and in the Acknowledgments for drafting. Wiley's own Methods examples name Claude.
- **The Wiley text also sets substantive limits.** AI may be used "only ... as an additional tool ... not a replacement for their own expertise and judgement". The manuscript "must demonstrate that the substance and expression of the work are yours, with AI serving only as assistant at your direction". The methodology must show that the human author "directed the work ... made final decisions about content, and maintained intellectual control". A study "designed, run, and written by an AI system" under supervision sits at or beyond the edge of this wording. Acceptability depends on the editor ("The final decision ... belongs to the journal's editor").
- **Human-directed framing:** Lukas as the accountable author who set the research question and made the final decisions stays within the policy only if that description is accurate. Understating the AI's role would breach the disclosure rules. A full, transparent disclosure may lead to a desk rejection under the "not a replacement" clause.
- **Recommendation:** send a pre-submission enquiry to the JBDM EiC that describes the AI's role before a full submission.
