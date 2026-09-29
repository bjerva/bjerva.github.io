# External-feedback review - 27 September 2026

Base: `master` at `053554e`. Review branch: `review/external-feedback-september-2026`.

## Decisions

| Feedback | Decision |
| --- | --- |
| Replace EMNLP highlight prose | Preserve the exact warmly personal copy approved on 22 August. Add individual VBN links identifying the three authors in full. |
| CCS in outlets and highlights | Add both; also feature CCS alongside ACL embedding inversion in the security strand. |
| Align metric dates | Do not relabel observations. August citation/media totals and 5 September project-record counts are different datasets; clarify the latter label. |
| Recent work heading | Change to Highlights. |
| Research lead repeats homepage | Replace with a concise explanation of the programme's methods. |
| Support Next frontier | Link Capable yet Parsimonious, explicitly a preprint. Update project cards whose forthcoming-output claim is stale. |
| Replace semantics paper | Retain the previously selected PMB and discourse examples; clarify the strand includes compositional representations and discourse context, and link the funded programme. |
| Fifth education strand | Keep the four-strand structure; add a concrete educational application under multilingual NLP and link Digital Twins and SEFL. |
| Raw project tags | Centralise the five display labels used by publication filters and project cards. |
| Approximation notation | Standardise to ≈ DKK. |
| IFD funding share | Leave unset. A sole named PI does not establish a 100% financial share. |
| Digital Twins status and co-lead | VBN confirms active through 31 December 2026, co-led with Euan Lindsay. Add both. |
| Co-funded image-embeddings paper | State the verified multiple VBN project associations. Do not infer a financial allocation or assert co-funding from associations alone. |
| ALIPES hotlink | Store the exact official PNG locally and record its source. |
| Peer-reviewed work before preprints | Preserve curated order. The leading preprint is clearly labelled and directly supports the emerging research direction. |
| Add Accepted to EMNLP | Preserve the previous explicit decision to use EMNLP 2026 without a suffix. Retain the separately requested CCS acceptance label. |
| Venue years | Remove the redundant arXiv year. Retain conference edition years and journal names alongside the publication-year column. |
| CCS summary | Shorten and use British spelling. Keep the published title unchanged. |
| Code/data resources | Add verified links for HiFi-KPI, MultiHal, CreoleVal and SubjQA. |
| Duplicate publication arrow | Render as a decorative, aria-hidden span; the paper title remains the link. |
| Group heading | Retain the heading chosen in the previous editorial pass. |
| Name group achievements | Leave anonymised claims untouched. Identities/consent for these attributions were not established. The group people page remains directly linked. |
| Teaching years and MSc course | Add dates from the public VBN teaching portfolio, including Copenhagen MSc NLP in 2018/2019; link the August 2026 PhD course. |
| PhD students | Link the AAU-NLP people page. |
| Service lines and heading | Split Area Chair roles; attach 2025 to the Spanish call; use Research policy and funding. |
| CV roles | Add existing editorial/Area Chair/AI:SECURITY roles and align Team Lead with Service. |
| Shared-award CV wording | Preserve the previously approved qualifier, including total award and 50% share. |
| Google award | Add CREOLE, dated 2023 according to Google's official awardee list. |
| PDF CV | Removed on 29 September at the user’s request, including the download link, PDF asset and generator. |
| Education partner | Name SEFL and Digital Twins in Collaborate. |
| Funding routes | Link the MSCA heading and add Cluster 3 with a specific-call qualification. |
| Legacy stubs | Replace with immediate meta-refresh redirects plus canonical and accessible fallback link, compatible with GitHub Pages. |
| Sitemap | Remove the handwritten file; retain jekyll-sitemap as the sole generator. |
| Footer and structured data | Add AAU Research Portal, Person image, worksFor and public institutional email. |
| README | Document current production/review workflow, data ownership, dated snapshots. |
| Branch pruning | No remote branches deleted. audit/september-2026, website-clean-base-2026 and website-refresh-2026 are fully merged; five agent/website branches contain commits outside master and need individual review before deletion. |

## Factual sources

- [Digital Twins status, dates and co-PIs](https://vbn.aau.dk/en/projects/digital-twins-for-abundant-feedback-novel-feedback-paradigms-via-/)
- [Capable yet Parsimonious and project associations](https://vbn.aau.dk/en/publications/capable-yet-parsimonious-extracting-and-characterizing-hidden-cha/)
- [Image-embeddings paper and project associations](https://vbn.aau.dk/en/publications/few-shot-semantic-recovery-attacks-on-image-embeddings/)
- [CCS paper and acceptance](https://vbn.aau.dk/en/publications/when-topology-betrays-privacy-lattice-based-reconstruction-attack/)
- [Google CREOLE award year](https://research.google/programs-and-events/society-centered-ai/google-society-centered-ai-research-awardees/)
- [Public teaching portfolio](https://vbn.aau.dk/ws/portalfiles/portal/cv/ad3c43ce-a6a9-4de3-820f-60e79b131702?locale=en_GB)
- [August 2026 PhD course](https://phd.moodle.aau.dk/blocks/vitrina/detail.php?id=2926)
- [HiFi-KPI](https://github.com/aaunlp/HiFi-KPI), [dataset](https://huggingface.co/datasets/AAU-NLP/HiFi-KPI)
- [MultiHal](https://github.com/ernlavr/multihal), [dataset](https://huggingface.co/datasets/ernlavr/multihal)
- [CreoleVal](https://github.com/hclent/CreoleVal), [SubjQA](https://github.com/megagonlabs/SubjQA)
- [Horizon Europe Cluster 3](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-3-civil-security-society_en), [MSCA](https://marie-sklodowska-curie-actions.ec.europa.eu/actions)

## Validation

- GitHub Pages-compatible Jekyll build succeeded locally using github-pages 232.
- Rendered-site checks passed: 11 HTML pages, 9 sitemap URLs, zero internal-link/fragment errors.
- Structured Person JSON-LD, redirect sitemap exclusions, all 35 publications, code/data groups and the CV download link checked.
- Desktop preview inspected in the browser; Security & Privacy filter returned the intended papers, and All restored 35 entries. A nested-list CSS issue in homepage paper links was found and corrected.
- Both PDF pages rendered and visually inspected, including typography, role/funding text, page breaks and links.
- Mobile CSS reviewed, including the resource-link grid row; a dedicated mobile-browser rendering was unavailable because the local browser download failed. No mobile visual pass is claimed.
- Review hosting uses the separate `johannes-bjerva-review` Netlify project with noindex/nofollow and analytics removed; production remains on unchanged master.

## Follow-up - 29 September 2026

- Removed the downloadable CV, its generator and README instructions at the user’s request. The HTML CV remains.
- Added Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects as NeurIPS 2026 · Accepted, with Security & Privacy and its VBN link. Acceptance is confirmed directly by the user; VBN still lists the preprint. Title, author order and contribution summary were checked against the VBN record.
- Added NeurIPS to selected outlets and the acceptance to highlights and the relevant (LM)²-SEC project description. Dated record-count snapshots remain unchanged.
