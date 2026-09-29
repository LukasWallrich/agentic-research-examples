# Decision (American Psychological Association)

ISSN 2325-9965, e-ISSN 2325-9973. Editor: Tim Rakow (King's College London). Access date for all sources: 2026-09-27.

**How the sources were fetched.** apa.org blocks curl and WebFetch with a bot wall (Incapsula). The live pages were read through the r.jina.ai reader proxy, which returns the current page as markdown. Quotes were cross-checked against the Wayback Machine snapshot of the old combined journal page (`https://www.apa.org/pubs/journals/dec/index?tab=4`, snapshot 2026-03-05) where the wording is the same. Each quote below is labelled **[live]** (jina, 2026-09-27) or **[archive, date]**. The jina markdown has small formatting artefacts ("7 th edition", "additional$600"); the quotes below restore normal spacing.

Key URLs:
- Decision submission guidelines (live, new page, "Date created: March 2026"): https://www.apa.org/pubs/journals/dec/submit
- Decision journal info page: https://www.apa.org/pubs/journals/dec/about
- APA Publishing Policies (live, "Last updated: October 2025"): https://www.apa.org/pubs/journals/resources/publishing-policies
- APA Journals policy on generative AI, additional guidance (live, "Last updated: August 2025"): https://www.apa.org/pubs/journals/resources/publishing-tips/policy-generative-ai
- APA open access page (live): https://www.apa.org/pubs/journals/resources/open-access
- APA–Jisc agreement page (live, "Last updated: January 2024"): https://www.apa.org/pubs/journals/resources/open-access-jisc
- APA open science page (archive 2026-08-10): https://www.apa.org/pubs/journals/resources/open-science
- COPE position "Authorship and AI tools" (archive 2025-09-13 only; the live page returned 403/CAPTCHA to curl, WebFetch and jina): https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools

---

## 1. Article types, length, abstract, reference style

**Article types** [live, /submit; identical in archive 2026-03-05]:
> "*Decision* will publish three types of articles. All page limits are exclusive of tables, figures, and references:
> - full length articles (35 pages) that make major theoretical contributions
> - shorter articles (15 pages) that make major empirical contributions addressing important theoretical issues
> - brief review articles (15 pages) that target rapidly rising theoretical trends or new theoretical topics in decision making"

Also offered: **Registered Reports** (two-stage) and **Registered Adversarial Collaborations** (a sub-type of Registered Reports). The editor's 2024 interview also mentions "registered replication reports" (https://www.apa.org/pubs/highlights/editor-spotlight/dec-rakow).

- **Which type fits (decision for the user):** "full length article" (35 pages) or "shorter article" (15 pages). The choice depends on manuscript length. The manuscript combines a 95-study reanalysis with four simulated process models, so a 15-page limit (double-spaced, excluding tables, figures, references) is probably too tight. A full-length article is appropriate if the paper is framed as a theoretical contribution: adjudicating among process models of anchoring.
- **Registered Report does not apply.** A Stage 1 manuscript was not submitted before the analysis. The preregistration is instead covered by the Preregistered / Preregistered+Analysis Plan badges (section 2).
- **Word limits:** not stated. Only page limits are given. Formatting rule: "Double-space all copy."
- **Abstract and keywords** [live]: "All manuscripts must include an abstract containing a maximum of 250 words typed on a separate page. After the abstract, please supply up to five keywords or brief phrases."
- **Reference style** [live]: "Prepare manuscripts according to the *Publication Manual of the American Psychological Association* using the 7th edition." So, APA 7.
- **Data and code must be cited** [live, /submit only]: "All data, program code, and other methods must be appropriately cited in the text and listed in the references section." The page gives a "Data set citation" example, so OpAQ needs its own data-set reference entry, and the R packages need software references.
- **File format** [live]: "in Microsoft Word (.docx) or LaTex (.tex) as a zip file with an accompanied Portable Document Format (.pdf) of a manuscript file." A Quarto manuscript would need to render to .docx, or to .tex plus .bib in a zip with a PDF.
- **Code** [live]: "Runnable source code should be included as supplemental material to the article."

## 2. Required sections and statements

| Item | Status | Exact text / note | Source |
|---|---|---|---|
| **Data, materials, code availability** | Required | "Authors must state whether data and study materials are available and, if so, where to access them." / "In both the author note and at the end of the method section, specify whether and where the data and material will be available or note the legal or ethical reasons for not doing so. For submissions with quantitative or simulation analytic methods, state whether the study analysis code is available, and, if so, where to access it (or the legal or ethical reason why it is not available)." | [live] /submit |
| **Informed consent / IRB (applies to secondary data)** | Required | "The method section also must include a statement describing how informed consent was obtained from the participants (or their parents/guardians), including for secondary use of data if applicable, and indicate that the study was conducted in compliance with an appropriate Internal Review Board." For OpAQ: state the consent and ethics basis of the original data collections, the CC-BY 4.0 licence, and whether an ethics exemption or approval was obtained for the reanalysis. | [live] /submit |
| **Constraints on generality** | Required (listed as "required" under EDI reporting standards) | "In a subsection of the discussion titled "Constraints on generality," authors should include a detailed discussion of the limits on generality … They should address limits on generality not only for participants but for materials, procedures, and context." | [live] /submit; "(required)" label from [archive 2026-03-05] EDI tab |
| **Participant description** | Encouraged | "Authors are encouraged to include a detailed description of the study participants in the method section … including (but not limited to) age, sex, gender". Also encouraged in the abstract and discussion: "discuss the diversity of their study samples and the generalizability of their findings". | [live] /submit |
| **CRediT** | Required, entered in Editorial Manager | "Submitting authors will be prompted to select one or more contributor roles for each author at initial submission. All authors should have reviewed and agreed to their individual contribution(s) before submission. If the manuscript is accepted for publication, an Author Contributions Statement will be generated during the typesetting process … It is not necessary for authors to provide a written Author Contributions Statement upon submission." | [live] /submit |
| **Conflicts of interest** | Required | "APA requires authors to reveal any possible conflict of interest in the conduct and reporting of research". Publishing Policies: "instructs authors to provide funder and conflict-of-interest information in the author note." | [live] /submit; [live] publishing-policies |
| **Funding** | Required, in author note | As above: "funder and conflict-of-interest information in the author note". | [live] publishing-policies |
| **Prior dissemination** | Required, in author note | "APA requires authors to provide information on prior dissemination of the data and narrative interpretations of the data/research appearing in the manuscript … This information (2–4 sentences) must be provided as part of the author note." Preprints: "Authors who have posted their manuscripts to preprint archives, such as PsyArXiv, prior to submission should include a link to the preprint in the author note." | [live] /submit; [archive 2026-06-23] publishing-policies |
| **Ethics compliance certification** | Required on acceptance | "If the manuscript is accepted, the corresponding author is required to sign and submit a Certification of Compliance with APA Ethical Principles". | [live] /submit |
| **Open science badges (optional)** | Optional | "Articles are eligible for open science badges recognizing publicly available data, materials, and/or preregistered plans and analyses. These badges are awarded on a self-disclosure basis." "At submission, authors must confirm that criteria have been fulfilled in a signed badge disclosure form … that must be submitted as supplemental material." "For the preregistered badge, this is an institutional registration system." Preregistered+Analysis Plan: "At least one study's design has been preregistered along with an analysis plan for the research — and results are recorded according to that plan." "Applying for open science badges is optional." Relevant here: Open Data, Open Materials, Preregistered+Analysis Plan. | [live] /submit |
| **TOP Guidelines levels** | Not stated for Decision | The Decision page has no TOP table. The APA open science page says TOP is adopted by "a growing number of APA journals" and that "authors are required to disclose TOP compliance only in the Methods section". The /about page "Features" list names only CRediT, Registered Reports, Open Science Badges and Impact factor. | [live] /about; [archive 2026-08-10] open-science |
| **Public significance statement** | Not required | Not mentioned on the Decision /submit page. | [live] /submit |
| **Running head** | Not journal-specific | Defers to the APA Publication Manual (7th ed.). | [live] /submit |
| **Masked review** | Author's choice | "Upon selecting an article type, authors can also choose between masked or unmasked review (i.e., "Unmasked article" or "Article with Masked review requested")." With masked review, the manuscript and supplementary files (OSF links, preregistration, the AI-disclosure wording) must be anonymised. | [live] /submit |
| **Bias-free language** | Required | "Manuscripts may be copyedited for bias-free language (see Chapter 5 of the *Publication Manual*)." Listed as "(required)" among EDI reporting standards. | [live] /submit; [archive 2026-03-05] |

## 3. AI policy (verbatim)

Decision has **no journal-specific AI policy**. The /submit page repeats the APA-wide rule and refers to the APA Publishing Policies page.

**Decision /submit page** [live], section "Generative artificial intelligence":
> "APA's current policies on generative AI include:
> - When a generative AI model is used in the drafting of a manuscript for an APA publication, the use of AI must be disclosed in the methods section and cited.
> - AI cannot be named as an author on an APA scholarly publication."

**APA Publishing Policies**, "APA policy on the use of generative artificial intelligence (AI) in scholarly materials" [live, "Last updated: October 2025"; identical in archive 2026-06-23]:
> "For this policy, AI refers to generative LLM AI tools and does not include grammar-checking software, citation software, or plagiarism detectors.
> - When a generative artificial intelligence (AI) model is used in the drafting of a manuscript for an APA publication, the use of AI **must** be disclosed in the manuscript and cited. For examples, see disclosure guidance.
> - AI **cannot** be named as an author on an APA scholarly publication.
> - The authors are responsible for the accuracy of any information in their article. Authors must verify any information and citations provided to them by an AI tool. Authors may use but must disclose AI tools for specific purposes such as editing.
> - No submitted content may be entered into generative AI tools as this violates the confidentiality of the process."

**Location of disclosure: the sources disagree.** The Publishing Policies page says "disclosed in the manuscript and cited". The /submit page and the AI guidance page say "disclosed in the methods section and cited". The guidance page's principles say "Disclose the use in the most relevant place in the manuscript, most likely the Introduction or Method sections." Safe approach: put a full disclosure in the Method section, cite the tool in the references, and add a summary in the author note.

**APA Journals policy on generative AI: Additional guidance** [live, "Last updated: August 2025 Date created: November 2023"]:
> "APA's current policies on generative AI are:
> - When a generative AI model is used in the drafting of a manuscript for an APA publication, the use of AI must be disclosed in the methods section and cited.
> - AI cannot be named as an author on an APA scholarly publication."

> "APA policy states that authors are responsible for the accuracy of any information in their article. This means that authors must verify any information and citations provided to them by an AI tool. Authors may use, but must disclose, AI tools for specific purposes such as editing."

Disclosure principles (verbatim):
> "Authors need to **be transparent**, providing the necessary information for readers to understand how generative artificial intelligence (AI) was used during the research and manuscript drafting process. Disclose the use in the most relevant place in the manuscript, most likely the Introduction or Method sections."

> "Authors need to **take responsibility** for the information provided by generative AI tools, including verifying the information received via generative AI searches by reading original sources used in AI output."

> "Authors need to **provide attribution** to the generative AI tool in cases where the tool was used to generate ideas, content, analysis, code, or research elements. If you would provide attribution to a human contributor, you should most likely provide attribution to a generative AI tool for a similar activity."

> "Researchers should document for their own records the prompts used with AI tools. To the extent that it helps readers, these prompts can be included where the AI use is disclosed, or elsewhere as appropriate, such as an appendix."

Disclosure table rows that apply to this manuscript (verbatim; the page calls the table "guidance only"):

| Generative AI use | How to disclose |
|---|---|
| "Create or refine code" | "In the Method section, including the tool used and number of iterations (preserve the output in case of inquiry)" |
| "Analyze, refine, format, or visualize data" | "In the Method section, including the tool used and number of iterations (preserve the output in case of inquiry)" |
| "Write or draft manuscript content, including literature summaries and outlines" | "In the introduction section, including your prompts and tool used" |
| "Create or edit figures, tables, and/or images" | "In the section where the figures, tables, and/or images appear (e.g., Results section), including your prompts and tool used (preserve the output in case of inquiry)" |
| "Create or edit research design elements, data, or results" | "In the Method section (preserve the output in case of inquiry)" |
| "Translate text … or implement extensive copyediting" | "In a general note in the author note, including the tool used" |

> "*Authors should consider this as guidance only and defer to the requirements of the journal editor as relevant."

**Authorship rules that interact with the AI policy** (APA Publishing Policies, "Author contributorship and responsibilities of authors") [live]:
> "Authorship is reserved for persons who make a substantial contribution to and who accept responsibility for a published work. Individuals should take authorship credit only for work they have performed or to which they have substantially contributed (APA Ethics Code Standard 8.12a, Publication Credit)."

> "Each author is expected to have made substantial contributions to the conception or design of the work; or the acquisition, analysis, or interpretation of data; or the creation of new software used in the work; or have drafted the work or substantively revised it; AND to have approved the submitted version … AND to have agreed both to be personally accountable for the author's own contributions and to ensure that questions related to the accuracy or integrity of any part of the work, even ones in which the author was not personally involved, are appropriately investigated, resolved, and the resolution documented in the literature."

**APA Style blog** (guidance, not policy), "Citing generative AI in APA Style: Part 1—Reference formats" [live] https://apastyle.apa.org/blog/cite-generative-ai-references:
> "Although it's still not a good idea to submit AI-generated work as though you did it yourself—doing so would be considered unethical, for example, academic misconduct for students—there are many potentially legitimate ways to use AI tools within the context of academic writing."

Reference format example from the same blog: "Anthropic. (2025, May 20). *Essential grammar topics for high school graduates* [Generative AI chat]. Claude Sonnet 4. https://claude.ai/share/…". In-text: "(Anthropic, 2025)". The blog adds: "you might also make a general mention of how AI was used in your paper's author note."

**Prohibition on substantially AI-generated manuscripts:** none stated. No APA page found caps the extent of AI use. The rules are disclosure, citation, human verification and responsibility, and no AI authorship.

**COPE level.** The APA Publishing Policies page lists the COPE statement under "Additional reading material" ("COPE Position Statement: Authorship and AI tools"). APA does not formally adopt it. COPE text [archive 2025-09-13; live page not retrievable]:
> "COPE joins organisations, such as WAME and the JAMA Network among others, to state that AI tools cannot be listed as an author of a paper."
> "AI tools cannot meet the requirements for authorship as they cannot take responsibility for the submitted work. As non-legal entities, they cannot assert the presence or absence of conflicts of interest nor manage copyright and license agreements."
> "Authors who use AI tools in the writing of a manuscript, production of images or graphical elements of the paper, or in the collection and analysis of data, must be transparent in disclosing in the Materials and Methods (or similar section) of the paper how the AI tool was used and which tool was used. Authors are fully responsible for the content of their manuscript, even those parts produced by an AI tool, and are thus liable for any breach of publication ethics."

COPE and APA agree on the main rules: no AI authorship, disclosure in Methods, and authors are fully responsible.

## 4. APC / open access model

**Hybrid subscription journal.** The Decision page shows "Open access offered".

- **APC** [live, open-access page]: "APC Open Access is offered for all APA subscription-based journals. Authors can make their article freely available for an article processing charge (APC) of $3,500 USD."
- **Licence** [live]: "APC Open Access articles are published under a CC-BY-NC-ND (Creative Commons Attribution-Noncommercial-No Derivatives) license … all requests for APC Open Access must be submitted BEFORE publication. APA will not grant post-publication requests to make articles open access."
- **Submission fee** [live]: "Submitting a manuscript for peer review is free of charge."
- **Green OA** [live]: "All APA authors, including those without APC funding, have the option of self-archiving (also known as "green" open access)". Authors whose funders require it may self-archive the accepted manuscript under CC BY (UKRI, Wellcome and NIHR requirements are explicitly supported).
- **Jisc Read-and-Publish agreement** [live, Jisc page, "Last updated: January 2024"]: "Authors affiliated with UK institutions participating in APA's Jisc agreement may publish open access in hybrid journals published by APA at no cost to the author, provided that: The article's corresponding author is affiliated with a participating institution's UK campus. … All articles under this agreement will be published under the CC-BY copyright license." **Birkbeck, University of London** is on the list of participating institutions. If the corresponding author is at Birkbeck, OA under CC BY should cost nothing. The page also says "APA and Jisc have set a limit on the maximum number of open access articles to be published for each year". Confirm with the library before relying on it.
- **Colour print figures** (optional) [live]: "$900 for one figure … An additional $600 for the second figure … An additional $450 for each subsequent figure". Colour online is free.

## 5. Fit: recent related articles (Crossref-verified)

**Anchoring papers: none found.** Crossref lists 205 Decision records from 2021 onwards (136 excluding supplementary-material records), up to issue 2026-1. No title contains "anchor". A Crossref query for "anchoring" filtered to the Decision ISSN returned 0 results. A web search also found no Decision anchoring article.

Verified with `curl https://api.crossref.org/works/<DOI>` (title, container-title, published date-parts as returned):

1. **10.1037/dec0000237**: "Using artificial intelligence to fit, compare, evaluate, and discover computational models of decision behavior." — Decision — [[2024, 10]]. Authors: Kvam, Sokratous, Fitch, Hintze. Published in the special issue "The Interface Between Artificial Intelligence, Machine Learning and Decision Research". Shows that the journal publishes both computational process-model comparison and AI-assisted modelling. https://doi.org/10.1037/dec0000237
2. **10.1037/dec0000150**: "Regression to the mean: Experimental evidence and a proposed heuristic." — Decision — [[2021, 7]]. Authors: Hogarth, Soyer. A heuristic account of a classic judgment bias with numerical judgments; the nearest topic to anchoring. https://doi.org/10.1037/dec0000150
3. (Optional) **10.1037/dec0000192**: "No evidence for a causal effect of exogenous testosterone on risky decision-making in women: An experiment and meta-analysis." — Decision — [[2022, 10]]. Precedent for pooled or secondary synthesis of existing studies. https://doi.org/10.1037/dec0000192

## 6. Cover letter

- No required cover-letter content is specified on the Decision /submit page, apart from this sentence [live]: "Authors should also note their eligibility for the badge(s) in the cover letter."
- Other items to raise in the letter or in Editorial Manager:
  - **Concurrent submission:** APA prohibits submitting the same manuscript to two outlets at once ("APA policy prohibits an author from submitting the same manuscript for concurrent consideration by two or more publications").
  - **Related reports:** "the author should inform the editor about the existence of other reports from the same research project at the time of submission" [archive 2026-06-23, publishing-policies].
  - **Funder source:** "Please indicate your funder source at the manuscript submission stage" [live, open-access page].
  - **Ringgold affiliation ID:** required at submission for the Jisc OA route [live, Jisc page].
- Recommended: state the AI role openly in the cover letter as well, so the editor learns about it before the reviewers do. The rules do not require this.

## Fit assessment

**Scope fit is good.** Decision's scope names "probabilistic inference, prediction, evaluation", and the journal "generally favors articles that include large-scale confirmatory tests of theory". A preregistered test of four process models on about 95 studies matches that description. The journal also ran a special issue on AI and machine learning in decision research (dec0000237 appears there). The editorial board includes several modellers (e.g., Bhatia, Lee, Pleskac, Trueblood, Turner, Stewart; archive 2026-03-05 board list). Weaknesses:
- Decision has published no anchoring paper since 2021.
- The volume is small (roughly 25 research articles a year).
- The reported rejection rate is 79.5% [live, /about].
- The impact factor is 1.6 [live].

**AI-authorship risk: moderate, and it comes from the authorship-credit rules.** The ban on AI authors is not the main issue:
- APA explicitly allows AI use with disclosure. APA does not prohibit substantially AI-generated work, and no APA page caps the extent of AI use.
- Claude cannot be on the byline. Lukas would be the sole author, and must select CRediT roles in Editorial Manager at submission.
- Ethics Code 8.12a says authors "take authorship credit only for work they have performed or to which they have substantially contributed". Claiming roles such as Formal analysis, Software or Writing—original draft for work the AI performed conflicts with this. The APA Style blog calls submitting "AI-generated work as though you did it yourself" unethical.
- The defensible configuration:
  - Lukas claims only the roles he actually held: Conceptualization, Supervision, Methodology (if he shaped the design), Validation (if he checked the results), and Writing—review and editing.
  - The Method section describes in detail what the AI did: design, code, analysis, simulations and drafting. Following the disclosure table, it gives the tool and model versions and the number of iterations, and says prompts and logs are preserved.
  - Claude is cited in the reference list in APA format.
  - The author note summarises the AI role.
- A 35-page limit leaves room for this disclosure. Under masked review, the disclosure must avoid identifying the author.
- **Remaining risk: editor judgement.** No APA rule bars the paper. However, an editor or reviewers could judge that a sole human author who did not perform the analysis or write the draft does not meet the "substantial contribution" criteria. Before submitting, consider a pre-submission enquiry to Tim Rakow (tim.rakow@kcl.ac.uk, listed on /submit) that describes the AI's role.
