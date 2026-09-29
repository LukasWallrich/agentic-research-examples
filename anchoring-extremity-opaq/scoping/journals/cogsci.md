# Cognitive Science (Wiley, for the Cognitive Science Society)

ISSN 0364-0213, e-ISSN 1551-6709. Access date for all sources: 2026-09-27.

**Sources**
- [A] Journal author guidelines: https://onlinelibrary.wiley.com/page/journal/15516709/homepage/forauthors.html. `curl` and WebFetch return 403 (Cloudflare bot check). The page was read in a real browser session after the check passed; all quotes are copied from the rendered page text (`document.body.innerText`), not paraphrased.
- [B] Wiley Best Practice Guidelines on Research Integrity and Publishing Ethics: https://authorservices.wiley.com/ethics-guidelines/index.html (fetched with curl, text extracted).
- [C] Wiley AI guidelines for researchers: https://www.wiley.com/en-gb/publish/article/ai-guidelines/ (fetched with curl, text extracted).
- [D] COPE position "Authorship and AI tools" (last reviewed 13 February 2023): https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools (curl 403; read in browser).
- [E] Wiley hybrid OA price list, "Updated: 2 September 2026": https://authors.wiley.com/asset/Wiley-Journal-APCs-OnlineOpen.xlsx (linked from https://authorservices.wiley.com/author-resources/Journal-Authors/open-access/article-publication-charges/index.html).
- [F] Cognitive Science Society journal page: https://cognitivesciencesociety.org/cognitive-science/

Quotes in this file use straight apostrophes. The source pages use curly apostrophes (’); the wording is otherwise identical.

## 1. Article types, word limits, abstract, reference style

Source [A], section "2. Article Types". "In all cases, the word limits are intended as approximate upper bounds, excluding references. Authors are encouraged to be as concise as possible within reason and should not aim for the upper limit for their category of article."

| Type | Description (verbatim) | Word limit | Abstract | Other |
|---|---|---|---|---|
| Regular Articles | "Reports of new research findings or conceptual analyses that make a significant contribution to knowledge" | 12,000 | Yes, unstructured | IRB statement if research includes participants |
| Extended Articles | "These are expected to present particularly noteworthy research that cannot be adequately described within the constraints of a regular article" | 18,000 | Yes, unstructured | IRB statement if research includes participants |
| Brief Reports | "Preliminary findings of research in progress or a case report of particular interest" | 4,000 | Yes, unstructured | IRB statement if research includes participants |
| Letter to the Editor | "Commentaries on articles, responses to commentaries, or discussion items of general relevance to the cognitive science community" | 1,000 | Yes, unstructured | N/A |

- **Best fit:** Regular Article (12,000 words excluding references). A Brief Report (4,000 words) is defined as "preliminary findings of research in progress", which does not match a completed preregistered analysis.
- **No Registered Report type** is listed [A].
- **Scope (relevant to fit):** "Descriptions of computational or mathematical models that exhibit some human or non-human cognitive process, especially if these models are implemented and tested and relate to observations of behavior in other domains." "Preference will be given to articles that employ a combination of methodologies (e.g., experimental and computational) or that otherwise demonstrate multidisciplinarity." Low priority: "Papers which are very general or speculative, which constitute parametric refinements of well-known ideas, or which are accessible to only a narrow or discipline-specific audience, will be given low priority and may be returned to authors without formal review." [A]
- **Abstract:** "Abstract of 150 to 250 words" [A].
- **Reference style:** "This journal uses APA reference style." Free Format submission applies: "this is for information only and you do not need to format the references in your article. This will instead be taken care of by the typesetter." [A]
- **Format:** Word (.doc/.docx) or LaTeX (.tex; upload a compiled PDF for review). Sections numbered with Arabic numerals to depth 3 (e.g. 2.4.3) [A]. A Quarto manuscript must be rendered to .docx or LaTeX/PDF.
- **Submission system:** "As of February 19, 2026, all new Cognitive Science manuscripts are submitted through the Research Exchange platform" (https://authors.wiley.com/journal/COGS). "This journal does not charge submission fees." [A]

## 2. Required sections and statements

All from [A] unless stated.

- **Masked review:** "Important: this journal operates a double-anonymized peer review policy. Please anonymize your manuscript and supply a separate title page file." Anonymising checks listed: use third person; "Remove or anonymize acknowledgements"; replace self-citations with "(Anonymous, 2005)"-style citations; "Check open material uploads for file names and other potential references to author identities." Preprints are allowed, but "if authors share their manuscript in preprint form this may compromise their anonymity during peer review."
- **Title page (separate file):** title without abbreviations; authors' full names; affiliations; corresponding author's full mailing address; "4-8 keywords"; "Acknowledgments."
- **Statements on the title page**, "which may include any of the following": "data availability statement", "funding statement", "conflict of interest disclosure", "ethics approval statement", "permission to reproduce material from other sources".
- **Funding:** "You should list all funding sources in the Acknowledgments section."
- **Conflicts of interest:** "You will be expected to declare all conflicts of interest, or none, on submission."
- **Ethics:** "This journal requires that you include in the manuscript details Institutional Review Board (IRB) approvals (i.e., ethical approval from the lead author's institution), ethical treatment of human and animal research participants, and gathering of informed consent, as appropriate." The article-type table requires an "IRB statement if research includes participants". No rule specific to secondary analysis of open data was found. A statement that no new data were collected and that OpAQ is de-identified and CC-BY licensed is the safe option.
- **Open Materials Policy (mandatory):** "For submissions that include programming code, experimental data, study stimuli, etc., authors are required to share materials so that reviewers gain a clear sense of how a study was conducted, how data were structured and analyzed, how a computational model was implemented, etc. Final, accepted versions of paper must be accompanied by relevant study materials." During review, "the journal requires anonymized study materials" (OSF anonymized links are named as an option). "Before a paper is accepted, any empirical study will require the sharing of data, code (stimulus presentation, data analysis, cognitive model, etc.) and other materials in such a way that the work can be reproduced by others." "Personal and most departmental websites do not qualify as repositories."
- **Data availability:** "This journal encourages data sharing. Review Wiley's Data Sharing policy where you will be able to see and select the data availability statement that is right for your submission."
- **Preregistration / badges:** "Wiley has now retired badges across most of its journals along with Cognitive Science." No preregistration rule was found on the author guidelines page.
- **CRediT:** not required by the journal page. Wiley's ethics guidelines [B] mention it only as an option: "CRediT (Contributor Role Taxonomy) is a community-owned 14-role taxonomy that can be used to describe the key types of contributions".
- **Authorship:** "All listed authors should have contributed to the manuscript substantially and have agreed to the final submitted version."
- **ORCID:** "This journal requires ORCID for the submitting author only."
- **Significance / public statement:** none required.
- **Running head:** not mentioned.

## 3. AI policy (verbatim)

### 3a. Journal level [A], section "AI Policy" (full text)

> "Artificial Intelligence Generated Content (AIGC) tools—such as ChatGPT and others based on large language models (LLMs)—cannot be considered capable of initiating an original piece of research without direction by human authors. They also cannot be accountable for a published work or for research design, which is a generally held requirement of authorship (as discussed in the previous section), nor do they have legal standing or the ability to hold or assign copyright. Therefore—in accordance with COPE's position statement on AI tools—these tools cannot fulfill the role of, nor be listed as, an author of an article. If an author has used this kind of tool to develop any portion of a manuscript, its use must be described, transparently and in detail, in the Methods or Acknowledgements section. The author is fully responsible for the accuracy of any information provided by the tool and for correctly referencing any supporting work on which that information depends. Tools that are used to improve spelling, grammar, and general editing are not included in the scope of these guidelines. The final decision about whether use of an AIGC tool is appropriate or permissible in the circumstances of a submitted manuscript or a published article lies with the journal's editor or other party responsible for the publication's editorial policy."

Summary:
- **AI as author:** not allowed.
- **AI-generated content:** allowed with disclosure. There is no explicit ban on substantially AI-generated manuscripts.
- **Where to disclose:** "in the Methods or Acknowledgements section", "transparently and in detail".
- **Editor discretion:** the editor makes the final decision on whether the AI use is "appropriate or permissible".

### 3b. Publisher level: Wiley ethics guidelines [B], "Artificial Intelligence"

> "Authors may only use AI Technology as an additional tool in their writing process, not a replacement for their own expertise and judgement. As always, authors remain fully responsible for the accuracy of all content and must verify that all claims, citations, and analyses align with their expertise and research. Before including AI-generated content in a journal submission, authors must carefully review it to ensure the final work reflects their own expertise, voice, and originality and that it complies with Wiley's ethical and editorial standards."

> "Authors should document all AI Technology used, including its purpose, whether it influenced key arguments or conclusions, and how they personally reviewed and verified any AI-generated content. Authors must also disclose their use of AI Technologies when submitting a manuscript to a Wiley journal. If disclosure is not provided at submission, it may be requested during peer review or after publication."

> "Disclosure: If an author has used AI Technology to substantially edit, develop, or translate any part of a manuscript, its use must be described transparently and integrated into the manuscript as described in our guidance on disclosure and declaration of AI use. AI Tools used solely for spelling, grammar, and general editing are not included in these disclosure requirements."

> "The final decision on whether using AI Technology is appropriate or permissible for a submitted manuscript or a published article belongs to the journal's editor or other party responsible for the publication's editorial policy."

> "AI & Authorship: AI Technology is not considered capable of initiating an original piece of research without human direction. Such tools cannot be held accountable for published work or for research design, which are both requirements of authorship (as discussed in the Authorship section in these guidelines). AI Technology also lacks legal standing and cannot hold or assign copyright. Therefore, in accordance with COPE's position statement on Authorship and AI tools these tools cannot fulfil the role of an author and must not be listed as one on an article."

### 3c. Publisher level: Wiley AI guidelines for researchers [C]

Placement of disclosures:
> "In your Acknowledgments when AI assists with manuscript drafting, editing, translation, or formatting."
> "In your Methods when AI is used to assist with your research methodology, data collection or analysis, or literature review processes."
> "In your figure captions when AI generates or edits any visual content that appears in your manuscript."

Methods disclosure:
> "Wiley requires disclosure when AI is used in your research methodology, including study design and data collection, literature review, code development, and data analysis."

Required content of a Methods disclosure ("When disclosing AI use in your methods, we require that you share:"): "AI Technology name and version"; "Date/year of use"; "The AI Technology's role in your work (image processing, code development, statistical analysis, etc.)"; "The author's role in directing or reviewing the work of the AI Technology"; "For sensitive, proprietary, or human subject data describe how privacy and compliance requirements were maintained".

> "If AI contributed substantially to your analysis or methodology, you may be asked to provide supplemental documentation to support reproducibility and transparency, such as: Prompts or parameters used; AI settings or configurations; Code repository; Data protection approach; Compliance with institutional requirements" (list items joined with semicolons here).

Statements with the most risk for an AI-run study ("How does AI use affect copyright protection of my research?"):
> "Your methodology, analysis, and conclusion must demonstrate that you directed the work using your expertise, made final decisions about content, and maintained intellectual control throughout the research process."
> "Your manuscript must demonstrate that the substance and expression of the work are yours, with AI serving only as assistant at your direction."
> "Authors may only use AI Technology as a companion to their writing process, not a replacement."

From the FAQ "Maintaining intellectual leadership with AI Technology" (advisory wording; it contains no explicit prohibition):
> "Think of AI as a research assistant working under your direction, helping you accomplish your goals more efficiently. You're responsible for how you use AI to support your work, and accountable for the quality, accuracy, and integrity of your research and manuscript."

The listed author roles are: "Define your goals and expectations for your AI collaboration"; "Provide directions to the AI based on your specific needs"; "Evaluate outputs using your domain knowledge"; "Seek input from AI, then implement changes in the work yourself"; "Make final decisions about what to include in your work"; "Disclose your use of AI transparently in your manuscript so readers can understand your process". Practices to avoid include "Using AI to make decisions rather than to inform your judgment".

Wiley's own FAQ methods note describes a similar workflow [C]:
> "The drafting authors provided editorial direction for initial section drafts, which were composed by Claude 4 Sonnet based on interview findings. Through iterative rounds of review and revision, all text content was refined and rewritten by the author to ensure accuracy, appropriate tone, and alignment with Wiley's vision for supporting authors in responsible AI use."

### 3d. COPE position [D]

> "AI tools cannot meet the requirements for authorship as they cannot take responsibility for the submitted work. As non-legal entities, they cannot assert the presence or absence of conflicts of interest nor manage copyright and license agreements."
> "Authors who use AI tools in the writing of a manuscript, production of images or graphical elements of the paper, or in the collection and analysis of data, must be transparent in disclosing in the Materials and Methods (or similar section) of the paper how the AI tool was used and which tool was used. Authors are fully responsible for the content of their manuscript, even those parts produced by an AI tool, and are thus liable for any breach of publication ethics."

### 3e. How the levels relate

- **Source of the journal text:** it is an earlier version of Wiley's standard AI paragraph, and it cites COPE.
- **Consistent across all levels:** AI cannot be an author. Disclosure goes in the Methods or Acknowledgements. The editor has the final say.
- **Stricter at Wiley level:** disclosure is also required "when submitting a manuscript". The current Wiley guidance requires a Methods disclosure with the items listed in 3c. It also states that the work must show the human author "directed the work" and "maintained intellectual control", with AI "only as assistant".
- **Wiley FAQ "Maintaining intellectual leadership":** gives advice only. It adds no further prohibition. The co-author FAQ ("How should co-authors coordinate disclosure of AI use?") recommends only that co-authors agree on the wording.
- **Submission-form AI question:** UNVERIFIED whether the Research Exchange form has a dedicated AI question. It cannot be checked without starting a submission.

## 4. APC / open access model

- **Model:** hybrid. "This journal is a subscription journal that offers an Open Access option. You'll have the option to make your article open access after acceptance, which will be subject to an APC unless a waiver applies." [A]
- **APC:** USD 4,200 / GBP 2,780 / EUR 3,470. Licences offered: CC BY, CC BY-NC or CC BY-NC-ND. Source: Wiley hybrid OA price list, "Updated: 2 September 2026" [E]. A Wiley transformational agreement at the author's institution may cover the APC [E].
- **Non-OA access:** "The final, electronic version of each issue of the journal is free to access on Wiley Online Library after a 1 year embargo period." Copyright is held by the Society, and authors may post the publisher PDF on personal websites immediately [F].
- **Submission fee:** none [A].

## 5. Recent related articles (Crossref-verified)

Both DOIs passed the brief's Crossref check. Titles, journal and dates are as Crossref returned them.

1. **10.1111/cogs.70229**: "The Robustness of Anchoring in a Naturalistic VR‐Based Task". *Cognitive Science*, [[2026, 6]] (vol. 50, issue 6). Authors: Wu, Farmer, Pready‐James, Warren. From the abstract: anchoring is framed as possibly deriving "from generic processing underpinning estimation". https://doi.org/10.1111/cogs.70229
2. **10.1111/cogs.70256**: "Quantity Estimation by Repeated Comparative Judgments". *Cognitive Science*, [[2026, 8]] (vol. 50, issue 8). Authors: Kaspersen, Solstad, Sabathiel, Hodgen. A computational model of quantity estimation that includes "an anchoring‐and‐adjustment mechanism", tested in preregistered experiments. https://doi.org/10.1111/cogs.70256

Crossref searches restricted to ISSN 1551-6709 from 2021 ("many labs replication", "open data reanalysis multiple studies", "secondary analysis large dataset judgment", "megastudy data") returned no secondary analyses of multi-lab or open datasets. This check is not exhaustive.

## 6. Cover letter

Required. Verbatim from [A]:
> "Authors should provide a concise cover letter with their submission. The cover letter should: a) present an argument for why the submission is appropriate for Cognitive Science (rather than, for example, for a single-discipline journal); b) for extended articles, indicate why an extended article is appropriate; c) confirm that all authors have approved the submission; and d) where data are reported, confirm that ethical guidelines consistent with local variations were adhered to. In the case of extended articles, authors should also make a case for the article's length."

## Fit assessment

**Topic fit: good.** The manuscript implements and compares four cognitive process models of anchoring against trial-level behavioural data. This matches the journal's stated interest in "computational or mathematical models that exhibit some human or non-human cognitive process, especially if these models are implemented and tested", and its preference for combined computational and empirical work. Two 2026 papers on anchoring and on anchoring-and-adjustment in estimation show current interest in the topic. The fit rests on the model comparison. A paper framed mainly as an anchoring-bias analysis from social psychology or JDM risks the "narrow or discipline-specific audience" / "parametric refinements of well-known ideas" desk-rejection criterion. The cover letter must make the multidisciplinary argument explicitly (item a).

**Formal fit:**
- **Article type:** Regular Article (12,000 words excluding references; abstract 150–250 words).
- **Masked review:** double-anonymised. This complicates the AI-authorship disclosure. The Acknowledgements must be anonymised, and a public preprint or OSF project that names the author compromises anonymity.
- **Materials:** open materials are mandatory. Anonymised code and data are needed at review (for example an OSF view-only link), and full materials in a repository before acceptance. OpAQ's CC-BY licence and an R pipeline make this easy.

**AI-authorship risk: moderate to high.**
- **Explicitly allowed:** disclosed AI use, including AI-written code, analysis and text. There is no ban on substantially AI-generated manuscripts.
- **Explicitly forbidden:** listing Claude as an author.
- **Main risk:** the Wiley-level guidance frames AI as an "assistant at your direction" and a "companion to their writing process, not a replacement". It requires the human author to show they "directed the work" and "maintained intellectual control throughout the research process". A study "designed, run, and written by an AI system" under supervision sits at the edge of this framing. Whether it is acceptable depends on how the supervision and the author's decisions are documented.
- **Precedent:** Wiley's own AI FAQ discloses section drafts "composed by Claude 4 Sonnet" under the authors' "editorial direction", followed by human revision. The publisher therefore accepts AI-drafted prose when a human directs and revises it.
- **Editor discretion:** the editor has explicit discretion ("The final decision ... lies with the journal's editor").
- **Recommendation:** make a detailed Methods disclosure covering model name and version, dates, role, how the human author directed and verified each stage, and prompts and logs in the supplement. Add an Acknowledgements statement. Consider raising the AI-run design with the editor (COGSeditorial@wiley.com) before submission.
