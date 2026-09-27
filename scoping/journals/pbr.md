# Psychonomic Bulletin & Review (PB&R): journal policy findings

Springer, for the Psychonomic Society. ISSN 1069-9384, e-ISSN 1531-5320. Publishing model: Hybrid. Editor-in-Chief: Daniel Mirman (University of Edinburgh).
All pages accessed 2026-09-27.

**Sources and how each was retrieved**
- S1. PB&R submission guidelines: https://link.springer.com/journal/13423/submission-guidelines. A direct curl request returns a JavaScript "Client Challenge" page. Full text was retrieved via the r.jina.ai text reader (`scratch_pbr_sg_jina.txt`, cleaned copy `scratch_pbr_sg_clean.txt`). Key sentences were cross-checked with WebFetch.
- S2. PB&R "How to publish with us" (OA and APC): https://link.springer.com/journal/13423/how-to-publish-with-us (via r.jina.ai).
- S3. PB&R journal home: https://link.springer.com/journal/13423 (via r.jina.ai). https://www.springer.com/journal/13423 hits the same client challenge.
- S4. Springer journal policies, including the "Artificial intelligence (AI)" and "Authorship principles" sections: https://link.springer.com/brands/springer/journal-policies (via r.jina.ai). The AI text was cross-checked word for word against the Nature Portfolio AI page (S6), which was fetched directly with curl. All 8 test sentences match.
- S5a. Springer Nature, "AI use in manuscript preparation": https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation (direct curl).
- S5b. Springer Nature, "AI use in research practice": https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research (direct curl).
- S5c. Springer Nature editorial policies hub, "Artificial Intelligence" section: https://www.springernature.com/gp/policies/editorial-policies (direct curl).
- S6. Nature Portfolio AI policy: https://www.nature.com/nature-portfolio/editorial-policies/ai (direct curl). It carries the same framework text as S4.
- S7. Psychonomic Society, Publication Policies / Resources: https://www.psychonomic.org/page/PublicationsResources. Cloudflare blocks curl and jina, so the text was read in a headed browser (browser-use).
- S8. Psychonomic Society, PB&R journal page: https://www.psychonomic.org/PBR (via r.jina.ai).
- S9. COPE position "Authorship and AI tools": https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools (headed browser; last reviewed 13 February 2023).

---

## 1. Article types, fit, word limits, abstract, reference style

PB&R publishes four submission types (S1):

- **Brief Reports.** This is the best fit. The format explicitly admits simulations and secondary analyses. Verbatim (S1):
  > "Brief Reports are concise articles that make substantial contributions to theories of cognition based on new data and are expected to be of broad interest to the general readership of the journal. Typically, these are new empirical studies, but computational model simulations, meta-analyses, or secondary or re-analyses of existing data can also be submitted under this article format provided they can be reported concisely. These articles are restricted to a maximum of 3,000 words for the Introduction, Results, and Discussion sections of the main text. This word limit does not include Methods, References, figures, tables, or the abstract. Authors of Brief Reports should be sparing with regard to the use of figures and tables."
  - The Methods section is excluded from the 3,000-word limit. Model specifications, simulation settings and the OpAQ inclusion rules can therefore go in Methods without counting towards the limit.
- **Theoretical or Review articles.** This is a possible alternative, with no length limit, if the paper is framed mainly as a theoretical comparison of process models. Verbatim (S1):
  > "Theoretical articles should propose a new theoretical treatment of some problem, or modify an existing one. ... While Theoretical and Review articles may include model simulations or results from meta-analyses, papers that rely on the collection of new empirical data are not appropriate for this article format (such work should be submitted to the journal as a Brief Report, see below). ... Papers in this submission category may be of any length."
  - Our paper collects no new data, so this format is not excluded. However, a preregistered empirical test with open data reads as a Brief Report.
- **Registered Reports or Replications.** Not applicable. The data already exist, and the RR route requires Stage 1 review before the study is run. The final Stage 2 manuscript must also follow the Brief Report format of 3,000 words (S1). PB&R is a PCI RR-interested journal.
- **Commentary.** Up to 1,000 words. Not applicable.

**Scope (S1):** "Submissions on topics from all areas of cognitive psychology are welcome. Examples include ... judgment and decision making, reasoning and problem solving, social cognition ... Studies using formal (computational/mathematical) models are particularly welcome."

**Abstract (S1):** "There must be an abstract of no more than 250 words." The Psychonomic Society also invites an optional second abstract in another language, placed immediately below the English abstract (S7).

**Reference and manuscript style (S1):** "Manuscripts are to adhere to the conventions described in the Publication Manual of the American Psychological Association (7th ed.)." The guidelines also state "Citations and References: These should conform to APA style." Figures and tables may be embedded in the text at submission. At acceptance they must move to the end of the manuscript.

**Submission system:** ScholarOne, http://mc.manuscriptcentral.com/pbr (S1).

## 2. Required sections and statements

- **Masked review: double-anonymous (S1, S8).** The Society announced a one-year pilot in June 2025 (S8). The current submission guidelines contain a "Double-anonymous peer review" section. None of the fetched pages say whether the pilot has been made permanent. Rules (S1, verbatim excerpts):
  - "Separate the title page from the rest of the main document."
  - "The first page should start with your title, then abstract and keywords, then main text of manuscript."
  - "Remove information about the institution where the study was conducted and which ethics review panel/board approved it."
  - "Self-citation: Do not anonymise citations to your prior work ... cite it using third person language."
  - "Online materials: if you include links to online data or materials, make sure those are anonymised both at the repository level (e.g., OSF allows creating anonymous view-only links ...) and within the files themselves."
  - "Note that preprints or conference submissions with the same title make it easier to identify the authors."
  - Consequence for us: the preregistration and the code/data repository need anonymised view-only links. The AI disclosure must be written so that it does not name Lukas. Mentioning Claude/Anthropic does not identify the author.
- **Title page (S1):** "The title page must include the authors' names and affiliations and the corresponding author's address, telephone number, and e-mail address." Acknowledgments and funding go on the title page (S1, "Acknowledgments and Funding Information").
- **Keywords:** required on the first page after the abstract (S1, anonymisation tips). No number is specified.
- **Running head:** not mentioned in S1.
- **Open Practices Statement: mandatory (S1).** Verbatim: "all submitted manuscripts must include an Open Practices Statement immediately prior to the References section of the paper. The statement must specify (1) whether data and/or materials are available, and if so, where (as per Level 1 TOP guidelines, URLs are required to have a persistent identifier); and (2) whether any experiments were preregistered, and if so, which." Authors also answer TOP Level 1 questions at submission (S7). These cover data and code availability and preregistration, for example: "Have you clearly distinguished which analyses were preregistered (confirmatory) and which were not (exploratory)?" and "Do you report all pre-registered analyses in the text, or, if there were changes in the analysis plan following preregistration, disclose those changes with appropriate explanations?"
- **Open science badges:** none. Neither S1 nor the Society's publication-policies page (S7) mentions badges. WebFetch on S1 also confirmed that the page never mentions badges. The Society's policy is TOP Level 1 plus the Open Practices Statement.
- **Preregistration:** not required. It is reported through the Open Practices Statement and the TOP questions. The Statistical Guidelines (S1) encourage it, e.g. "Covariate analyses should either be planned in advance (and in that case would benefit from preregistration) or be described as exploratory."
- **Statistical Guidelines:** at submission, the corresponding author must affirm familiarity with them (S1, affirmation (d)). They cover a priori power or sample-size justification, multiple testing, reporting of exclusions, and intervals around effects.
- **Research data policy (S1):** "This journal operates a type 2 research data policy." The journal "strongly encourages" data availability and "encourages" a Data availability statement. Datasets with DOIs may be cited in the reference list. OpAQ should therefore be cited as a dataset reference.
- **Declarations section: mandatory (S1).** Verbatim: "All manuscripts must contain the following sections under the heading 'Declarations'. If any of the sections are not relevant to your manuscript, please include the heading and write 'Not applicable' for that section." Required headings: Funding; Conflicts of interest/Competing interests; Ethics approval; Consent to participate; Consent for publication; Availability of data and materials; Code availability; Authors' contributions. For Authors' contributions, the list adds: "(optional: please review the submission guidelines from the journal whether statements are mandatory)".
  - Caveat: the heading list is directly preceded by the italic line "_To be used for life science journals + articles with biological applications_" (S1). The block looks like Springer boilerplate, not text written for PB&R. The requirement holds regardless: the Competing Interests "Summary of requirements" in S1 says funding and competing interests go "in a 'Declarations' section before the reference list". The safe course is to include all headings and write "Not applicable" where a heading does not apply.
- **Author contributions / CRediT:** PB&R does not require CRediT specifically. S1 says "If desirable, contributions of different authors may be briefly described here" (Author Note). Springer's journal policies (S4) state: "Authors are required to include a statement of responsibility in the manuscript ... that specifies the contribution of every author." Recommendation: include a CRediT-style statement for Lukas and put the AI's role in the AI disclosure.
- **Conflicts of interest (S1):** disclose interests from the last 3 years in the Declarations section. At submission, the corresponding author affirms that any conflict "has been disclosed in a message to the Editor".
- **Funding (S1):** give it in the Declarations section and also in the submission system. Funder names must be written in full.
- **Ethics statement for secondary data (S1, "Ethics approval for retrospective studies"), verbatim:** "Although retrospective studies are conducted on already available data or biological material (for which formal consent may not be needed or is difficult to obtain) ethics approval may be required dependent on the law and the national ethical guidelines of a country. Authors should check with their institution to make sure they are complying with the specific requirements of their country." S1 also states: "If a study was granted exemption from requiring ethics approval, this should also be detailed in the manuscript (including the reasons for the exemption)." Recommendation: get a written exemption or a "no review required" confirmation from the institution for analysing open, anonymised CC-BY data. Report it under "Ethics approval". Write "Not applicable" under the two consent headings. For review, omit the name of the ethics committee (anonymisation rule above).
- **Significance / public statement:** not required (not mentioned in S1).
- **Demographics:** the Society encourages reporting participant demographics in Methods where they were collected (S7).

## 3. AI policy (verbatim)

**Journal level.** The PB&R submission guidelines contain no AI or LLM section. Searches of S1 for "artificial", "AI", "language model" and "generative" found no hits, and WebFetch confirmed this. No Psychonomic Society AI statement was found on the Society's publication-policies page (S7), in a search of the Society site for "artificial intelligence", or by web search. PB&R therefore defers to the **Springer / Springer Nature publisher-wide policy**. S1 refers authors to Springer's "Authorship Principles", which sit on the same Springer journal-policies page as the AI section (S4).

**Publisher level: Springer journal policies, "Artificial intelligence (AI)" (S4; same text in S6).**
- Framing:
  > "Springer Nature supports the responsible and transparent use of artificial intelligence where it strengthens research quality, upholds editorial independence, and preserves the integrity of the scientific and scholarly record."
  > "AI is treated as a supporting technology. Scholarly judgement, accountability, and responsibility always remain human."
- Core expectations:
  > "Human accountability is non‑transferable
  > Accountability for scholarly content, evaluation, and editorial decisions cannot be delegated to AI systems."
  > "AI may support, but must not replace, scholarly judgement
  > AI can assist clarity, efficiency, and exploration, but must not determine conclusions, evaluations, or decisions."
  > "Transparency creates trust and confidence
  > Transparent declaration of AI builds trust and confidence, and removes ambiguity about how AI might have been used."
- **Green, "Permitted: Assistive AI use (low risk)".** Examples include "Using an LLM to polish or refine the language", "Comparing methodological options", "Stress-testing research questions" and "Data cleaning and deduplication". Compliance: "Permitted. Disclosure enhances trust and transparency and clearly demonstrates human accountability."
- **Amber, "Exercise caution: Evaluative or interpretive AI use".**
  - Expectations: "AI does introduce new intellectual content and requires verification and oversight" and "Human judgement and accountability must be demonstrable".
  - Examples: "Suggesting analytical, experimental or methodological approaches", "Drafting explanatory summaries", "Comparing results to existing literature", "Extensive copy editing or writing support", "Recommending statistical tests or modelling approaches".
  - Compliance: "Permitted with human oversight, verification, and transparency through disclosure. If AI materially influences evaluative judgement, accountability must remain clearly human‑led and defensible."
- **Red, "Not permitted: AI replacing scholarly judgement or lacking transparency".**
  - Expectations: "AI use is opaque or creates non‑verifiable outputs" and "Author, reviewer or editorial responsibility has been delegated to AI".
  - Examples: "Generating hypotheses, analyses or conclusions and presenting them as human-derived", "Fabricating data, citations or results", "Using an LLM to generate core research reasoning without disclosure", "Assigning authorship or accountability to AI systems or tools".
  - Compliance: "Not permitted."
- Authors' responsibilities:
  > "Remain fully accountable for originality, accuracy, and integrity"
  > "Disclose AI use for trust and transparency"

**Publisher level: Springer Nature, "AI use in manuscript preparation" (S5a).** This page is stricter on writing than S4.
> "Springer Nature applies a risk-assessment approach, focusing on how AI is used, rather than whether it is used."

The risk table (cell text as extracted from the page):
- **Amber:** "AI contributes to structuring or shaping written content". Typical uses: "Generating outlines; drafting sections based on author input; suggesting alternative phrasing or framing; reference management support". Considerations: "all AI generated or assisted content must be clearly labelled". Declaration: "Clearly describe use and confirm author accountability".
- **Red (not permitted):** "AI replaces authorship or generates scholarly content without oversight". Typical uses: "Writing results or discussion independently; generating scientific claims or interpretations; producing data or figures as if empirical; listing AI as an author". Declaration: "Not permitted".

Also from S5a:
> "More extensive uses, such as drafting or restructuring content, require greater care. Authors should ensure that: all content is accurate and verified; disciplinary conventions are correctly applied; references are real and have been checked; the intellectual contribution remains their own"

(The four conditions are bullet points on the page.)

> "AI can assist with expression, but the argument, interpretation, and conclusions must be author-led."
> "Declaration does not negatively influence editorial decisions"
> "You remain fully accountable for everything submitted in your name."

For figures:
> "The use of AI to generate, analyse, visualise or enhance visual content may be permitted where authors meet the following requirements: AI use is disclosed appropriately, including model and purpose of use; ... any AI-assisted processing, analysis or code generation has been subject to appropriate human review and validation"

> "Where AI-generated or AI-assisted visual content is published, information about the AI system used, the purpose of its use, and the extent of its contribution should be provided in an AI Declaration in your manuscript. Specific disclosure should be provided within the caption or legend of the visual content."

**Publisher level: Springer Nature, "AI use in research practice" (S5b).**
- Amber, "AI contributes to analytical or interpretive processes". Examples: "Identifying patterns in datasets; supporting statistical modelling; ...". Declaration: "Provide clear methodological description and validation steps and take accountability".
- Red, "AI replaces core scholarly judgement or compromises integrity". Examples: "Generating hypotheses, analyses, or conclusions without human oversight; fabricating data or references; ...". Declaration: "Not permitted".
- Further text:
  > "AI may support your work, but you remain fully accountable for all research decisions, outputs, and conclusions."
  > "In higher-risk contexts, such as data analysis, modelling, or qualitative interpretation, AI may assist but must not replace critical reasoning. Authors should be able to clearly describe how AI was used, what inputs and outputs were involved and how results were validated."
  > "Quantitative research: ... When doing so, authors should be able to clearly describe inputs, outputs and validation steps, ensuring results are reproducible and independently assessable."

**Hub summary (S5c):**
> "AI can improve efficiency and assist with a range of activities across the research and publishing lifecycle, but it must not replace scholarly judgement, accountability, or editorial decision-making."
> "Our editorial policies are guided by four core expectations: human accountability cannot be transferred to AI systems; AI may support but not replace scholarly judgement; transparency about AI use builds trust and confidence; and confidentiality and data protection must be maintained when using AI tools."

**Answers to the specific questions**
- **Can AI be an author? No.** "Assigning authorship or accountability to AI systems or tools" is Red / not permitted (S4). "listing AI as an author" is also Red (S5a).
- **Is AI-generated text or analysis allowed with disclosure? Yes, within limits.** AI drafting "based on author input" and support for analysis or modelling are Amber: permitted with human oversight, verification and disclosure. The following are Red and not permitted: "Writing results or discussion independently; generating scientific claims or interpretations" (S5a), and "Generating hypotheses, analyses, or conclusions without human oversight" (S5b). S4 phrases its Red items in terms of non-disclosure ("presenting them as human-derived", "without disclosure"). S5a and S5b do not attach a disclosure condition to their Red items. They turn on the absence of human oversight or authorship.
- **Where and how to disclose.** The current Springer framework (S4, S5a, S5b) requires disclosure but gives no fixed location for text or analysis use.
  - S5a asks for "an AI Declaration in your manuscript" with the AI system, purpose and extent. For figures, it also asks for disclosure in the caption.
  - S5b asks for a "clear methodological description and validation steps".
  - COPE, which Springer journals follow (S4: "Springer journals will be guided by COPE guidelines"), requires disclosure "in the Materials and Methods (or similar section)" (S9).
  - PB&R's submission form and cover letter have no documented AI question (S1). UNVERIFIED: whether ScholarOne asks an AI question at submission. It cannot be checked without logging in.
  - Recommendation: describe the AI's role in Methods, add an "AI Declaration" under Declarations, and mention it in the cover letter.
- **Restriction on substantially AI-generated manuscripts.** There is no explicit ban on a manuscript being mostly AI-drafted. The combined effect of the rules is restrictive:
  - "the argument, interpretation, and conclusions must be author-led" (S5a)
  - "the intellectual contribution remains their own" (S5a)
  - Red for AI "Writing results or discussion independently" (S5a)
  - "AI ... must not determine conclusions" (S4)

**COPE level (S9).** It agrees with Springer on authorship and states the disclosure location explicitly.
> "COPE joins organisations, such as WAME and the JAMA Network among others, to state that AI tools cannot be listed as an author of a paper."
> "AI tools cannot meet the requirements for authorship as they cannot take responsibility for the submitted work. As non-legal entities, they cannot assert the presence or absence of conflicts of interest nor manage copyright and license agreements."
> "Authors who use AI tools in the writing of a manuscript, production of images or graphical elements of the paper, or in the collection and analysis of data, must be transparent in disclosing in the Materials and Methods (or similar section) of the paper how the AI tool was used and which tool was used. Authors are fully responsible for the content of their manuscript, even those parts produced by an AI tool, and are thus liable for any breach of publication ethics."

**Springer authorship criteria (S4, "Authorship principles").** All authors "made substantial contributions to the conception or design of the work; or the acquisition, analysis, or interpretation of data ...; drafted the work or revised it critically for important intellectual content; approved the version to be published; and agree to be accountable for all aspects of the work".

## 4. APC / open access model

- **Hybrid journal (S2, S3).** Verbatim (S2): "Psychonomic Bulletin & Review is a hybrid journal." Authors choose after acceptance between subscription publishing (no fee) and open access.
- **APC (S2), verbatim:** "The current APC for Psychonomic Bulletin & Review is £2590.00 GBP / $3890.00 USD / €2990.00 EUR." The page adds: "This fee is subject to VAT or local taxes where applicable."
- **Licence for OA articles:** CC BY 4.0 (S2).
- **Institutional deals:** Springer Nature open access agreements may cover the APC (S2: "Springer Nature offers agreements that enable institutions to cover open access publishing costs."). UNVERIFIED: whether Lukas's institution is covered. This was not checked.
- **Subscription route:** copyright is transferred to the Psychonomic Society (S1, affirmation (c)). Articles become free to read after 12 months (S8: "Open access to articles older than 12 months at Springer.com").
- **Other fees:** printed colour figures cost $1,100 per article. Online colour is free (S1).

## 5. Fit: recent PB&R articles (DOIs verified with the Crossref command given in the brief)

- **10.3758/s13423-022-02147-4.** Crossref: title ['Anchoring effect induces false memories'], container ['Psychonomic Bulletin &amp; Review'], published [[2022, 7, 25]]. Authors: Navarre, Didierjean, Thomas. Shows that PB&R publishes anchoring work.
- **10.3758/s13423-023-02331-0.** Crossref: title ['What is the airspeed velocity of an unladen swallow? modeling numerical judgments of realistic stimuli'], container ['Psychonomic Bulletin &amp; Review'], published [[2023, 10, 6]]. Authors: Izydorczyk, Bröder. A computational model of real-world numerical estimation, close to our model-comparison approach.
- **10.3758/s13423-022-02128-7.** Crossref: title ['Trial-by-trial mouse trajectory predicts variance in precision across working memory representations: A critical reanalysis of Hao et al. (2021)'], container ['Psychonomic Bulletin &amp; Review'], published [[2022, 6, 6]]. Authors: Park, Zhang. An example of a reanalysis of existing data published in PB&R.

The article type (Brief Report or Theoretical/Review) of these three papers was not confirmed. The Springer article pages did not return a type label through the text reader.

## 6. Cover letter requirements

- PB&R's guidelines (S1) do not require a cover letter and specify no content for one.
- Springer's journal policies (S4) assign cover-letter content to the corresponding author. Verbatim: "providing transparency on re-use of material and mention any unpublished material (for example manuscripts in press) included in the manuscript in a cover letter to the Editor". S4 also states: "Authors can suggest peer reviewers in the cover letter."
- Conflicts of interest must be disclosed "in a message to the Editor" (S1, affirmation (b)).
- Recommendation: send a cover letter anyway. It should (a) state the article type, Brief Report, and give the word count for Introduction, Results and Discussion; (b) disclose the AI's role in full and state that the human author takes accountability; (c) point to the preregistration and to the anonymised materials link.

## Fit assessment

**Scientific fit is strong.** PB&R names judgment and decision making in scope and says formal (computational/mathematical) models are "particularly welcome". The Brief Report format explicitly accepts "computational model simulations ... or secondary or re-analyses of existing data". Methods are excluded from the 3,000-word limit, which suits the model specifications and the OpAQ inclusion rules. The open data and preregistration map directly onto the mandatory Open Practices Statement. The main scientific risk is the bar of "substantial contributions to theories of cognition" and "broad interest": the paper must lead with the theoretical payoff, i.e. which process model survives, not with the dataset. Keeping Introduction, Results and Discussion to 3,000 words with four models is tight but feasible. Theoretical/Review (no length limit) is a fallback if the model comparison dominates. Double-anonymous review requires anonymised OSF, preregistration and repository links.

**The AI-authorship risk is high.** PB&R has no AI policy of its own, so the Springer / Springer Nature risk framework applies, together with COPE. Claude cannot be listed as an author. The Red items carry qualifiers:
- S4: "presenting them as human-derived" and "without disclosure".
- S5a: the row header reads "generates scholarly content without oversight", and the cell reads "Writing results or discussion independently".
- S5b: "without human oversight".

This manuscript is disclosed and supervised. It therefore sits on the Amber/Red boundary. The deciding question is whether work "designed, run and written by an AI under instruction and supervision of a human researcher" gives demonstrable human oversight, and whether the "argument, interpretation, and conclusions" are "author-led" (S5a). A second constraint applies even with oversight: S4 says AI "must not determine conclusions". Submission is defensible only if:
- Lukas is the sole author and takes documented accountability;
- the disclosure (Methods, AI Declaration, cover letter) describes the supervision and verification steps concretely;
- Lukas can truthfully say the "argument, interpretation, and conclusions" are author-led.

If the manuscript foregrounds the AI as the one who designed and interpreted the study, editors are likely to read it as S5a's Red case ("generating scientific claims or interpretations"). That invites desk rejection or an integrity query, even with full disclosure. A study whose declared purpose is AI-conducted research would likely need either a substantial human interpretive layer, or a venue with an explicit policy for AI-led research.
