# Meta-Psychology (metapsych)

- Publisher / host: Linnaeus University Press (LnuOpen, OJS). e-ISSN 2003-2714. DOI prefix 10.15626/MP.
- All pages accessed 2026-09-27. Pages fetched with `curl -sL -A "Mozilla/5.0"` and converted to text with a local script. All quotes below come from that text, not from WebFetch.
- Main sources:
  - Submissions / author guidelines: https://open.lnu.se/index.php/metapsychology/about/submissions
  - About the journal (scope, OA, peer review, transparency policy): https://open.lnu.se/index.php/metapsychology/about
  - Editorial board and board policies: https://open.lnu.se/index.php/metapsychology/ored
  - Submission form and preregistration checklist templates (OSF): https://osf.io/t54ph/ (files: https://osf.io/download/muvwh/ submission form; https://osf.io/download/jt9v7/ preregistration checklist; both last modified 2023-05-21)
  - DOAJ record: https://doaj.org/api/search/journals/issn%3A2003-2714 (last updated 2026-09-17)
- `https://open.lnu.se/index.php/metapsychology/about/editorialPolicies` returns 404. The journal has no separate editorial-policies page. The policies sit on the "About" and "Submissions" pages.

## 1. Article types, fit, limits, reference style

Sections listed on the submissions page (source: /about/submissions):

- **Original articles**: "This section contains original articles on the topic of meta-psychology."
- **Registered Reports** (two-stage, in-principle acceptance; checklist https://osf.io/6bv27/). The journal also accepts reports that went through Peer Community in Registered Reports (source: /about).
- **Tutorials**: "Tutorials on methods relevant for psychology researchers."
- **Commentaries**: includes "Re-analysis of own research".
- **Registered Replication Reports**; **Replication Reports** ("Replications of previous empirical findings on any topic relevant for psychology. Has to be preregistered.").
- **File-Drawer Reports**: "Unlike Original articles, these need not be on the topic of Meta-Psychology but can be on any topic of psychology. They require a complete emptying of a file-drawer on a topic". Requires a fixed transparency statement that the report covers all data from the authors' own projects.
- **Questionable Research Ideas and Other Peculiarities (QRAP)**: "dedicated to absurd commentaries, strange ideas and other odd pieces of meta-science."
- The About page also lists: Replicability Reports (R-index/p-curve style), History of Psychology, Philosophy of Psychology, Cross-disciplinary perspectives.

**Changes announced in the 2023 editorial** (Carlsson, https://doi.org/10.15626/MP.2023.4032), verbatim: "We are retiring peer reviewers being co-authors of the peer review report, the file drawer section, and although we’re leaving peer review open to spontaneous commenting, we won’t spend as much time advertising for it as we have in the past." It also introduces Verification Reports ("essentially, post-publication reproducibility reports") and says reproducibility checks are to begin "already at submission". The submissions page still lists File-Drawer Reports, and a File-Drawer Report was published in Dec 2025 (item 2 in section 5), so the retirement status is unclear. In practice, the social-media open-review round is less central than the /about page suggests; review is mainly by invited, named reviewers.

**Which type fits:** Only **Original article** fits. Replication Report and File-Drawer Report do not fit: the manuscript is not a replication, and it analyses other researchers' data, not the authors' own file drawer. The Original-article section is restricted to "the topic of meta-psychology". A substantive anchoring test would therefore need a meta-scientific framing (see Fit assessment). A Registered Report is not an option: the study is already preregistered and the analyses exist.

**Word limit:** No word limit stated on any journal page. **Abstract limit:** none stated. (Searched /about and /about/submissions.)

**Reference / format style:** APA. Quote (/about/submissions): "Your preprint should follow APA-style except that figures and tables should be embedded in the PDF/manuscript, and placed where they are easy to read. The PDF can be either in the usual APA-manuscript form, or in a reader-friendly form, for example an APA-article-styled PDF." After acceptance, copy-editing is done by the authors in LaTeX/Overleaf: "Writing your manuscript in LaTeX is thus strongly preferred, but not required." (A Quarto manuscript can render to LaTeX/PDF, so this is manageable.)

**Reporting standards** (/about/submissions): "All articles should be checked against and meet the requirements of APA JARS" and "The editor will likely not send your submission out for peer review before it meets these standards."

## 2. Required statements and submission package

**Preregistration (mandatory for this study):** "All studies that collect data (including non-primary data such as in meta-science and literature reviews), or have confirmatory research questions / hypotheses must be preregistered with hypotheses, data collection and analysis plan as a minimum" (/about/submissions). The /about page is inconsistent with this: "We strongly encourage the studies reported in manuscripts to be pre-registered (e.g., OSF or aspredicted.org), but this is not mandatory." The submissions page is the more specific and stricter text. This does not matter here because the study is preregistered. Preregistered papers "should include separate “confirmatory” and “exploratory” results sections" (/about). A preregistration checklist (https://osf.io/download/jt9v7/) must be submitted with the form.

**Open data / code / materials (mandatory):** "All manuscripts should be accompanied by an OSF project page that contains data, the code necessary to reproduce the statistical analysis and the research materials." Also: "Always include a README file." and "A good rule of thumb is that a grad student in your research area should be able to reproduce it without help." Containers suggested for complex environments (/about/submissions). Transparency policy (/about): "All submissions have to be accompanied by open data, well-documented code, and open materials. Exceptions to this rule will only be granted in extraordinary cases".

**Reproducibility check:** "Prior to publication, all statistical analyses are reproduced by our statistical reproduction team, which consists of the Statistical Editor and our editorial assistant. This makes the article eligible for the reproducibility badge." (/about). The board page says the reproducibility check is part of "the initial desk stage (aims and scope, submissions requirements, reproducibility check)" (/ored). The submission form lists "Open Analysis and Reproducibility (this is mandatory for acceptance but not an Open Science Badge)" and asks that "Analysis files clearly explain where the syntax/code for each figure, table and in-text numbers from the manuscript can be found" (https://osf.io/download/muvwh/).

**Open Science badges:** Applied for in the submission form (Open Data, Open Materials, Preregistration(+)). Published articles carry a header block listing Open data / Open materials / Open and reproducible analysis / Open reviews / Preregistration, plus "Edited by", "Reviewed by", "Analysis reproduced by" (seen in https://doi.org/10.15626/MP.2024.4137).

**Preprint (mandatory):** "Upload (or update) a preprint on PsyArXiv. Other preprint services are allowed if they provide a DOI. Tag it with meta-psychology." The first page must carry this exact statement (/about/submissions):
> "Submitted to Meta-Psychology. Participate in open peer review by sending an email to open.peer.reviewer@gmail.com. The full editorial process of all articles under review at Meta-Psychology can be found following this link: https://tinyurl.com/mp-submissions You will find this preprint by searching for the first author's name."

**Timing:** "during July each year our editors have a well-deserved break. We will not process new submission until august." (/about/submissions)

**What is uploaded to OJS:** only the submission form (plus preregistration checklist). "Authors should refrain from uploading any additional files with the submission." Supplementary material lives on OSF.

**COI, funding, CRediT** (/about/submissions): "At the end of the article the following sections should be included: Conflict of Interest and Funding. Declare any conflict of interest or state that there is none. Declare any funding or state that there was none. Author Contributions. Author contributions should follow CRediT". The tenzing app is recommended. Published examples also include an "Open Science Practices" section at the end.

**Ethics statement:** No explicit ethics-statement requirement found on the journal pages. The privacy notice says only "The authors published in this journal are responsible for the human subject data that figures in the research reported here." For secondary open data, a short statement on data source, licence (OpAQ, CC-BY 4.0) and absence of new participants is advisable but not stated as required.

**Significance / public statement, keywords, running head:** None required on the journal pages. (Not found on /about, /about/submissions, or the submission form.)

**Anonymisation / masked review:** None. Review is fully open. "The journal aims for complete transparency throughout the entire publication process. There is no blinding of either authors or reviewers." (/about). "All manuscripts are subject to rigorous open non-anonymous peer review by several expert peers." Manuscripts are also "posted on social media in a round of open peer review". The editor publishes a curated "Peer-review Report" with its own DOI. "From the moment of submission, the entire work-flow (decisions, reviews , etc.) is available online through the Open Science Framework." For rejected manuscripts, "this will be documented and linked to in editorials." (/about)

**Post-publication duty:** "Authors are required to co-operate with replicators or peers making critical commentary on their work. Failure to do so in good faith can be grounds for retracting the article." (/about)

## 3. AI / LLM policy

**No formal AI/LLM policy exists on the journal's author guidelines or policy pages. The only statement found is one sentence in a 2023 editorial by the Editor-in-Chief.**

Editorial statement, verbatim (Carlsson, R. (2023). Meta-Reflections on Meta-Psychology. *Meta-Psychology*, 7. https://doi.org/10.15626/MP.2023.4032 ; Crossref-verified: `['Meta-Reflections on Meta-Psychology'] ['Meta-Psychology'] [[2023, 9, 27]]`; text from the article PDF https://open.lnu.se/index.php/metapsychology/article/download/4032/3490):
> "Finally, an editorial in 2023 is not complete without discussion of AI and plagiarism. Unsurprisingly, our take is that AI innovations in science, and scientific publication are welcome, but that it should be used in an open and transparent manner."

This is a stance, not a procedure. It says nothing on AI authorship, on where to disclose, or on limits for AI-generated manuscripts.

Searched for a formal policy:

- /about, /about/submissions, /ored (editorial board and policies), /about/contact, /announcement, journal index page: no occurrence of "artificial", "AI", "LLM", "language model", "generative", "ChatGPT", or "COPE" (text grep of fetched pages).
- /about/editorialPolicies: 404.
- Submission form and preregistration checklist templates on OSF (https://osf.io/t54ph/, versions of 2023-05-21): no AI item or AI disclosure field.
- Journal full-text search (https://open.lnu.se/index.php/metapsychology/search/search?query=...) for "artificial intelligence", "ChatGPT", "LLM", "generative AI": no results. "language model" returned one unrelated 2022 article.
- Crossref titles of all 93 Meta-Psychology items published since 2023: none on AI/LLMs by title (titles only screened). Editorials read in full: the 2017 inaugural editorial (https://doi.org/10.15626/MP2017.1001; no mention of AI or COPE), the 2023 editorial quoted above (the only AI mention), and the 2026 inaugural QRAP editorial (https://doi.org/10.15626/MP.2026.4892; no mention of AI).
- Linnaeus University Press / LnuOpen pages (https://www.lnu.se/en/research/published-research/linnaeus-university-press/ ; https://lnu.se/en/medarbetare/researcher/researcher5/publish-with-lnu-press/ ; https://lnu.se/en/medarbetare/researcher/researcher5/publish-with-lnu-press/lnuopen/ ; https://open.lnu.se/): no AI policy and no publication-ethics policy.
- Web searches for a Meta-Psychology or Linnaeus University Press AI policy: nothing found.

**COPE:** The journal does not mention COPE on any of its pages or in the three editorials read. The DOAJ record lists no ethics-body affiliation. The journal therefore does **not** defer to COPE, and there is no publisher-level policy to defer to. COPE membership status: UNVERIFIED. The COPE member directory (https://publicationethics.org/members?title=Meta-Psychology and ?title=Linnaeus) returned a Cloudflare block to curl; a web search found no listing.

**Consequences for this manuscript:**
- **AI as author:** not addressed. No rule allows or forbids it. The only authorship rule is that contributions "should follow CRediT" and that papers include "an explanation of the contributions made by each author" (/about).
- **AI-generated text/analysis with disclosure:** not addressed. No required location for disclosure. The natural places are the Methods, the Author Contributions (CRediT) section, and the "Letter to Editor" field in the submission form, which is public: "Please note that the cover letter is public and will be read by the reviewers." (/about/submissions)
- **Restrictions on substantially AI-generated manuscripts:** none found. The editorial's condition is openness and transparency, which a fully disclosed AI-conducted study meets.
- **Advice from the journal itself:** "If you are unsure about the suitability of your manuscript for the journal, we encourage you to contact us before submission." (/about/submissions). Given no policy, a pre-submission email to the Editor-in-Chief (Rickard Carlsson) about the AI-authorship question is advisable.

## 4. APC / open access model

Diamond open access, no APC. Quote (/about): "Diamond Open Access - No Processing Fees. Meta-Psychology is a completely free Open Access journal. There is no fee for publishing, and the articles are available free online." Licence: "All articles are published under a CC-BY license." Authors keep copyright. DOAJ confirms `has_apc: false`, `has_other_charges: false`. The trade-off: "Meta-Psychology only provides minimal copy-editing and authors are thus required to format their articles before they are published online." Funding: "Supported by a grant from the Swedish Research Council." Indexed in DOAJ; TOP Factor 27 (/about).

## 5. Fit: recent related articles (DOIs verified with Crossref)

Both returned by the Crossref check on 2026-09-27 (title, container-title, published date as returned):

1. `['Measurements of Susceptibility to Anchoring are Unreliable'] ['Meta-Psychology'] [[2024, 12, 20]]` — https://doi.org/10.15626/mp.2022.3236. Röseler, Weber, Helgerth, Stich, Günther, Tegethoff, Wagner, Schütz. Article type: Original Article. Meta-analysis of more than 50,000 anchored estimates. The data set "is available as part of the Open Anchoring Quest (OpAQ; https://metaanalyses.shinyapps.io/OpAQ)" (article PDF). This is the same data source as our manuscript.
2. `['Falsifying the Insufficient Adjustment Model: No Evidence for Unidirectional Adjustment From Anchors'] ['Meta-Psychology'] [[2025, 12, 30]]` — https://doi.org/10.15626/mp.2024.4137. Röseler, Incerti, Rebholz, Seida, Papenmeier. Article type: File-Drawer Report. Formalises the insufficient-adjustment process model of anchoring and tests it in four preregistered studies; "Data from Studies 1, 2, and 4 are included in the Open Anchoring Quest data" (article PDF). This is a process-model test of anchoring, directly adjacent to our model comparison.

Also relevant as a methods reference: `['Preregistration of secondary data analysis: A template and tutorial'] ['Meta-Psychology'] [[2021, 11, 9]]` — https://doi.org/10.15626/mp.2020.2625 (Van den Akker et al.).

## 6. Cover letter

Required, but in the form of the journal's **submission form** (https://osf.io/download/muvwh/): "This form serves as the cover letter, application for OSF open badges, and includes a link to the preprint." Fields: authors, title, date, preprint link (DOI), "Letter to Editor", and the badge checklist with OSF/DOI links. Content rules: explain any data/code/materials that cannot be shared ("If you have technical or ethical problems with sharing data, analysis or materials, please carefully explain this in the cover letter"). The cover letter is **public** and uploaded to the submission's open OSF project; confidential matters go to the Editor-in-Chief by email before submission (/about/submissions).

## Fit assessment

**Topic fit is strong; section fit is the risk.** Meta-Psychology has published two OpAQ-based anchoring papers by the OpAQ team (Röseler et al., 2024; 2025), one of which formalises and falsifies an adjustment process model. Our manuscript builds directly on both. The journal's requirements (preregistration of secondary analyses, open OSF project, statistical reproduction before publication, preprint) match what the project already produces. It is diamond OA with no fee. However, the Original-article section is for "original articles on the topic of meta-psychology", and papers that do "not match the scope" are desk-rejected. The Röseler 2025 process-model paper appeared as a File-Drawer Report (the one section open to "any topic of psychology"), which is not available to us. The 2024 paper was framed meta-scientifically (measurement reliability). A purely substantive anchoring-extremity/model-comparison paper therefore risks desk rejection on scope. It fits much better if framed meta-scientifically: for example, as a case study of AI-conducted, preregistered secondary analysis of open multi-study data, with the anchoring result as the worked example, or with emphasis on what open cumulative data sets like OpAQ allow for theory testing. A pre-submission enquiry to the editor is explicitly invited.

**AI-authorship risk:** No formal AI policy exists. The only statement is the EiC's 2023 line that AI in science and publication is "welcome, but that it should be used in an open and transparent manner". Nothing forbids the design, and the journal's culture (open review, reproducibility checks, QRAP section for unusual meta-science, advisory board of meta-scientists) makes an AI-conducted study a plausible meta-scientific object. But there is also no rule to rely on: acceptance of an AI system as author, or of a substantially AI-written manuscript, is at the editor's discretion. The open review means the AI question will be debated publicly and the record stays online even after rejection ("For rejected manuscripts, this will be documented and linked to in editorials"). Likely reviewers include the OpAQ team (Röseler), whose data and models the paper tests. Recommendation: email the Editor-in-Chief before submission. Describe the AI's role, the planned authorship line (human author with AI disclosure in Methods and CRediT), and the meta-scientific framing.
