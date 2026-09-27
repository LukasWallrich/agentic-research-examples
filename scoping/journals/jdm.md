# Judgment and Decision Making (JDM), Cambridge University Press — ISSN 1930-2975

All pages accessed 2026-09-27. Unless noted, the text was fetched with `curl` and converted to plain text with a local script (`scratch_jdm_extract.py`). Quotes are copied from that text, not paraphrased.

Source pages (JDM pages are under `https://www.cambridge.org/core/journals/judgment-and-decision-making/information/`):
- **[PREP]** Preparing your materials: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/author-instructions/preparing-your-materials
- **[SUBMIT]** Submitting your materials: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/author-instructions/submitting-your-materials
- **[FEES]** Fees and pricing: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/author-instructions/fees-and-pricing
- **[OA]** Open access options: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/journal-policies/open-access-options
- **[ETHICS]** Publishing ethics (JDM): https://www.cambridge.org/core/journals/judgment-and-decision-making/information/journal-policies/publishing-ethics
- **[TRANSP]** Research transparency: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/journal-policies/research-transparency
- **[REVIEW]** Review process: https://www.cambridge.org/core/journals/judgment-and-decision-making/information/peer-review-information/review-process
- **[ABOUT]** About this journal: https://www.cambridge.org/core/journals/judgment-and-decision-making/information
- **[CUP-AUTH]** CUP authorship and contributorship (includes "AI Contributions to Research Content"): https://www.cambridge.org/core/services/authors/publishing-ethics/research-publishing-ethics-guidelines-for-journals/authorship-and-contributorship
- **[SJDM-OLD]** Old JDM site at SJDM (editor notes): https://sjdm.org/journal/

## 1. Article types, length, abstract, reference style

- **Article types** [PREP]: "Empirical Article*", "Review Article*", "Theory Article*", "Registered Report*", "Commentary (invited only)". No research note or brief report type is listed.
- **Best fit:** Empirical Article. The aims and scope explicitly include "analysis of existing data" and "process models (e.g., fast-and-frugal heuristics, coherence-based decision theories)" [PREP]. A Registered Report is not appropriate: JDM RRs need pre-study acceptance before the study is run [PREP].
- **Length** [PREP], verbatim: "JDM does not have article length restrictions. If you have concerns about the length of your manuscript, please contact the Editorial Office."
- **Abstract:** "Abstract (up to 250 words)"; **Keywords:** "Keywords (up to 10)" [PREP, SUBMIT].
- **Reference style** [PREP], verbatim: "Please use APA citation and reference style. (Not the rest of APA style.)" House rules on top of this:
  - "Do not put commas before the last "and" or "&"." (so no serial comma before `&` in references)
  - "Page numbers are required for everything."
  - "Don't use "cf." or "see". It is better to say, in a couple of words, why you are citing something"
  - "Use British style for quotations: all punctuation, including commas and periods, go outside of quotation marks"
  - "Use footnotes, not endnotes."
- **Other house-style rules relevant to this manuscript** [PREP], verbatim:
  - "In a regression model, you do not usually "control" for covariates. You "adjust" for them."
  - "Say "almost significant", not "marginally significant"."
  - "Use "subjects" or "participants" consistently, not both in the same paper."
  - "Be consistent in the way you report statistics. ... Use parentheses, not commas, for statistical tests ... Minimize the number of statistics you include."
- **Statistical guidelines:** [PREP] lists "red flags" to check before submission, including "Statistical control (probably the single most common issue)", "Multiple regression", "Reporting interactions, or drawing conclusions from significant vs. non-significant", and "Showing that your results are generally true of subjects but not looking at items". The last point matters here: anchoring effects vary by item, so item-level random effects or item-level results should be shown. The full guidelines are linked at https://jbaron.org/journal/stat.htm (link taken from [PREP]; page not fetched).
- **Format:** Word or LaTeX. An Overleaf template exists. "Both LaTeX and Word submissions should be accompanied by PDF files" [PREP]. Quarto output as PDF plus .docx or .tex source fits this rule.

## 2. Required sections and statements

**Manuscript order** [PREP], verbatim (line breaks shown as /):
> Manuscripts should be compiled in a single document in the following order: Title page, including: Authors, including Corresponding Author designation, full contact details and affiliations, including country / Abstract (up to 250 words) / Keywords (up to 10) / Main text, including Author names, Table(s) with caption(s) and Figures with caption(s) in place throughout / Acknowledgements / Competing Interests Statement / Data Availability Statement / Financial Support Statement / Supplementary Materials / References

[SUBMIT] gives the same list without "Data Availability Statement". Include one anyway: [PREP] lists it and [TRANSP] encourages it.

- **Data / code / materials** [PREP and TRANSP], verbatim: "For empirical work, JDM requires the availability of raw data (with a key to the meaning of variable names, if needed), and stimulus materials such as questionnaire items, for review and for publication (unless this is impossible for some reason). These may be submitted as supplemental files or posted publicly somewhere else. If a submission is not rejected immediately, we will request these documents. Publications should, insofar as possible, include all key information necessary to understand (and replicate) the study and data analysis, including data, as well as stimuli, questionnaires, and code, when these are necessary to understand exactly what was done."
  - [REVIEW]: "We require submission of data (or links to the data) for articles not rejected immediately ... Data will be public when articles are published."
  - For this manuscript: link the OpAQ dataset (CC-BY 4.0), plus the analysis and simulation code and the preregistration.
- **Reproducibility checks:** No formal computational reproducibility check by the journal is stated on any fetched page. [SJDM-OLD] states "We have signed the TOP guidelines." (old site; current CUP pages do not repeat this).
- **Preregistration / badges:** No Open Science badges and no preregistration reporting rule on the fetched pages. Preregistration is mentioned only in the RR section: "A registered report is not the same as pre-registration, although that may be useful for many papers" [PREP].
- **CRediT:** Not required by JDM. The CUP-level page says: "Some journals have adopted contributorship taxonomies such as CReDiT, and/or may publish contributorship statements within manuscripts. Please refer to individual journal information pages for further details." [CUP-AUTH]. JDM pages do not mention CRediT. [ETHICS] says: "Authorship statements should be transparent about who contributed to the work and in what capacity." A contribution statement is optional but useful here to describe the AI and human roles.
- **Competing interests** [PREP], required: "All authors must include a competing interest declaration in their main manuscript file." If there are none: “Competing interests: The author(s) declare none”.
- **Funding** [PREP], required as a separate section. If there is no funding: "This research received no specific grant funding form any funding agency, commercial or not-for-profit sectors." (the typo "form" is in the source)
- **Acknowledgements:** a separate section. Funding must not be listed here [PREP].
- **Ethics statement (secondary data):** JDM has no rule specific to secondary data. The general rule [ETHICS], verbatim: "Research involving human participants, tissue or data should be approved by relevant institutional ethics committee(s) ..." and "In cases where the need for formal ethics committee approval was waived, the name of the ethics committee that granted the waiver should be included in the methods section of the manuscript." Recommended wording: state that the analysis uses only anonymised, openly licensed data. Also obtain an exemption or waiver from the institutional ethics committee, or state why none was needed. An editor may ask for this.
- **Significance / public statement:** none required on any fetched page.
- **Running head:** not mentioned on any fetched page.
- **ORCID:** required for the corresponding author [PREP].
- **Anonymisation / masked review** [REVIEW], verbatim: "This journal uses a single-anonymized model of peer review. ... However, authors who wish to mask their identity during peer review may choose to do so." So no anonymisation is required. The main text includes author names ("Main text, including Author names") [PREP].
- **Accessibility:** alt-text is needed for all figures (WCAG 2.1 AA). Authors may supply it themselves; otherwise it is machine-generated at proof stage [PREP].
- **Desk review:** "All submissions will receive an initial desk review by an Editor ... Usually the review will involve one Consulting Editor and another reviewer." The typical turnaround is "around 2 months" [REVIEW].

## 3. AI policy (verbatim)

### Journal level: JDM "Use of Artificial Intelligence (AI) Tools" [PREP]
Verified by curl and text extraction. The section states that it applies the CUP policy: "In this section we explain how to declare the use of AI tools in an accountable and transparent way, in accordance with the Cambridge University Press Research Publishing Ethics Guidelines."

**Authorship:**
> "We do not consider artificial intelligence (AI) tools to meet the accountability requirements of authorship, and therefore generative AI tools such as ChatGPT should not be listed as authors on any submitted content."

**Credit and citation:**
> "All use of AI-generated content must comply with our plagiarism policy and best practices regarding citation and acknowledgement."
> "You must not present ideas, words, data, or other material originally produced by third parties without appropriate acknowledgement or permission."

**What to declare:**
> "You should always declare and describe your use of an AI tool if you have used it to generate text or images (this includes the translation of sources or of your own work) or to analyse or extract insights from data or other materials."
> "Minimal and non-generative uses of AI tools in manuscript preparation do not require declaration. ... It is important to note that accountability for the use of AI tools, including minimal and non-generative ones, rests with the author. Caution should be used in all cases and it is important to check your article thoroughly for unintended consequences, particularly in relation to the references."
> "If you are unsure about whether a particular use of an AI tool requires declaration, please contact the journal’s editorial office."

**Where to declare:**
> "Use of AI tools should be declared in your manuscript in the same way that you would declare your use of other tools and assistance."
> "If you have used AI tools to generate text within your manuscript, this should be declared in the same way you would declare your use of other language-editing services, for example in a separate acknowledgments section or in a footnote."
> "If you have used AI tools to collect or analyse data, the way you have done this should be described in your methods section or general description of your methodology, in the same way you would describe your use of other software or analysis processes."
> "If you have used AI tools to generate visual content that appears in your manuscript, this should be declared in the captions of any figures that you have generated or modified using AI tools."

**How to declare** (required content):
> "Descriptions of your use of AI tools should include: the name and version of the tool you used / the date(s) you used the tool for the purpose(s) described, to the extent reasonably possible / how the tool can be accessed or used by others, to the extent reasonably possible / a full description of how you used the tool / appropriate citations to any third-party text, datasets or other material used or included in the tool’s output."
> "Additionally, as appropriate, descriptions should include: any proprietary information relevant to the use of the tool / any ways in which you modified the version of the tool that you used (such as training it on your own data) / any competing interests or potential bias that should be considered as a consequence of the tool’s use, including as a result of its ownership or development."

### Publisher level: CUP "AI Contributions to Research Content" [CUP-AUTH]
Verified by curl and text extraction.
> "AI use must be declared and clearly explained in publications such as research papers, just as we expect scholars to do with other software, tools and methodologies."
> "AI does not meet the Cambridge requirements for authorship, given the need for accountability. AI and LLM tools may not be listed as an author on any scholarly work published by Cambridge"
> "Authors are accountable for the accuracy, integrity and originality of their research papers, including for any use of AI."
> "Any use of AI must not breach Cambridge’s plagiarism policy. Scholarly works must be the author’s own, and not present others' ideas, data, words or other material without adequate citation and transparent referencing."
> "Please note, individual journals may have more specific requirements or guidelines for upholding this policy."

### Summary of the two levels
- **Can AI be an author?** No, at both levels. JDM: "should not be listed as authors". CUP: "may not be listed as an author on any scholarly work published by Cambridge".
- **Is AI-generated text or analysis allowed with disclosure?** Yes. No rule at either level forbids or limits a manuscript that is largely AI-generated. The limits are accountability ("rests with the author") and the plagiarism rules.
- **Where to disclose:**
  - AI-generated text goes in the acknowledgements or a footnote.
  - AI-run analysis or data work goes in the Methods section.
  - AI-made figures are disclosed in the figure captions.
  - The pages mention no form field or cover-letter requirement for this disclosure (the submission form itself was not checked).
- **Required content:** the tool name and version, dates of use, how others can access the tool, a full description of how it was used, and citations.
- **Possible conflict for this manuscript:** CUP's policy says "Scholarly works must be the author’s own". JDM's authorship criteria require the listed human authors to have made "Substantial contributions to the conception or design of the work; or the acquisition, analysis, or interpretation of data" and to have given "Final approval of the version to be published; and Agreement to be accountable for all aspects of the work" [ETHICS]. A human who supervised, checked, and approved the work and who accepts accountability meets the criteria as written, because the criteria are joined by "and/or". An editor could still read "the author’s own" narrowly if the AI did the design and writing.
- **COPE:** The JDM and CUP pages use COPE only for authorship disputes and change requests ("this journal will be guided by the relevant COPE flowchart") [ETHICS]. They do not cite COPE's AI position statement. The CUP ICMJE-based authorship criteria are repeated at journal level [ETHICS].

## 4. APC / open-access model

- **Model:** fully Gold OA. "This journal is a wholly open access journal, which means all articles are published Gold Open Access under a Creative Commons licence." [FEES]. "Authors may choose any of the six Creative Commons licences" [OA].
- **APC** [FEES], from the table on the page: **GBP 2610; USD 3655** ("additional taxes may apply"). A search-engine snippet showed an older figure (USD 3450 / GBP 2320). The live page gives the numbers above.
- **Waivers and funding routes** [OA]:
  - Institutional open-access agreements with CUP, checked automatically.
  - The Cambridge Open Equity Initiative for authors in low- and middle-income countries.
  - Research4Life.
  - Grant funding where available.
  - Otherwise: "Any corresponding author of a research article who is not covered by one of the above funding routes can request a discount or full waiver of their APC. Authors will be invited to make their request after editorial acceptance". The journal adds: "Prospective authors should submit with full confidence, knowing that no author will face a financial barrier to publication."
- **Editors' note on the old SJDM site** [SJDM-OLD]: "do not be discouraged by the (somewhat incomplete) section on waivers of processing charges. We expect very few authors to be subject to these, regardless of read-and-publish agreements."
- **SJDM/EADM member waiver:** none found on the CUP pages or on sjdm.org. Treat as UNVERIFIED / likely not a separate route. Checked: [FEES], [OA], https://sjdm.org/, and https://sjdm.org/journal/.
- **Practical note:** Lukas's institution may have a CUP read-and-publish agreement. Check with the eligibility checker linked from [OA].
- **Preprints:** "This journal allows preprints to be posted anywhere at any time, including before submission to the journal." [OA]

## 5. Fit: recent related articles (DOIs verified with the Crossref API)

| DOI | Title (as returned by Crossref) | Journal | Published | Relevance |
|---|---|---|---|---|
| https://doi.org/10.1017/s1930297500008330 | Anchoring without scale distortion | Judgment and Decision Making | [[2021, 1]] | An anchoring mechanism paper by Bahník. It tests the scale-distortion account, so it is a direct theoretical neighbour to the four process models. |
| https://doi.org/10.1017/jdm.2023.39 | A normative model for Bayesian combination of subjective probability estimates | Judgment and Decision Making | [[2023]] | A formal/computational model of judgment (Trick, Rothkopf, Jäkel). It shows JDM publishes model-based work. |

Additional context (verified with Crossref; not a fit example): https://doi.org/10.1017/jdm.2025.7, "Artificial intelligence and dichotomania", Judgment and Decision Making, [[2025]] (McShane, Gal, Duhachek). It reports that ChatGPT, Gemini, and Claude show "dichotomania" when they interpret p-values. Some reviewers may therefore look closely at how the AI system interpreted statistical results.

Older JDM anchoring papers also exist, for example "Variations on anchoring: Sequential anchoring revisited" (10.1017/s1930297500005428, 2019). The Crossref searches restricted to ISSN 1930-2975 from 2021 onward found no other anchoring-specific articles. I found no clear 2021+ JDM example of a secondary analysis of multi-lab open data.

## 6. Cover letter

- None of the fetched JDM or CUP pages sets a requirement or required content for a cover letter. The only mention is that a thesis-based manuscript must say so in the cover letter [ETHICS].
- The Registered Report route needs "a separate explanation of why you are doing the study and why you want acceptance in advance" [PREP]. This does not apply here.
- The ScholarOne submission form (https://mc.manuscriptcentral.com/jdm) may have a cover-letter field. UNVERIFIED: the form needs a login.
- Recommendation:
  - Write a short cover letter anyway. Use it to explain the AI-conducted workflow and the human accountability arrangement at the start.
  - Point to the Methods and Acknowledgements disclosures.
  - Confirm that the data, code, and preregistration are public.
  - The policy invites contact before submission: "If you are unsure about whether a particular use of an AI tool requires declaration, please contact the journal’s editorial office." A pre-submission email to journal@sjdm.org ([SJDM-OLD]) about AI-conducted research is an option.

## Fit assessment

- **Topic fit:** strong. The anchoring mechanism, the process models, and the use of existing data are all named in the JDM aims and scope ("heuristics & biases", "process models", "analysis of existing data").
- **Format fit:** strong.
  - There is no length limit, so the simulations and multi-study analyses can stay in the main text.
  - Single-anonymised review means no masking is needed.
  - The open-data requirement is met with no extra work because OpAQ is CC-BY.
  - JDM uses APA references with house changes (no serial comma before "&"; page numbers required). It has idiosyncratic style rules ("adjust" not "control"; British quotation punctuation; footnotes only). A Quarto CSL/template tweak is needed.
- **AI-authorship risk:**
  - JDM and CUP forbid listing Claude as an author. Lukas must be the sole author and accountable party. Claude's role must be described in Methods (analysis) and in the acknowledgements or a footnote (text), including model name and version, dates, access, and "a full description of how you used the tool".
  - No rule forbids a substantially AI-generated manuscript.
  - The risk is editorial, not a policy bar. CUP's phrase "Scholarly works must be the author’s own" and the ICMJE-style criteria leave room for a desk editor to object if the human role reads as supervision only. Frame Lukas's contributions (conception, preregistration approval, verification, interpretation, final approval, accountability) concretely against the four criteria.
  - JDM recently published a paper documenting LLM statistical-interpretation errors (10.1017/jdm.2025.7). Expect reviewers to scrutinise the inferential language. Follow the journal's statistical "red flags" list closely, especially the item-level generality check and the rule against conclusions drawn from significant vs. non-significant contrasts.
- **Cost risk:** the APC is USD 3655 / GBP 2610 if no agreement or waiver applies. Waivers are granted after acceptance by CUP, and the editors state that few authors pay.
