# bjerva.github.io

Personal academic website for Johannes Bjerva, built with Jekyll and hosted on GitHub Pages.

## Updating content

- Edit `_data/projects.yml` to add or update research programmes, staffing, funder logos, and VBN-linked work snapshots. If the represented portfolio changes, update the rounded funding values in `_data/site_metrics.yml`.
- Edit `_data/site_metrics.yml` for the small set of rounded, cross-page indicators. Keep these durable and source them from the detailed pages or linked profiles.
- Edit `_data/highlights.yml` for a small number of current highlights.
- Edit `_data/publications.yml` for the curated publication list, including its venue, one or more themes, and a single factual contribution note.
- Add verified code/data links under a publication's `resources` list. Keep its title link pointed at the matching VBN record.
- Edit `_data/topics.yml` for the shared display labels used by publication filters and project tags.
- Core page copy lives in the corresponding root-level HTML file.

The site intentionally keeps only selected publications and highlights. Selection should balance current research direction, field contribution, and longer-term influence rather than reproduce a chronological bibliography. Google Scholar, ACL Anthology, and the AAU Research Portal remain the sources for complete records.

Only officially confirmed courses and public research descriptions should be included.

Before publishing, verify publication metadata against the ACL Anthology or publisher record and institutional details against current VBN pages and the latest approved CV.

Link individual publications to their matching VBN record, preferring the published or accepted version where available. Apply this across the publication list, homepage highlights, and in-page references. Retain a publisher or repository link only when no matching VBN record can be verified.

Project impact counts are dated snapshots from VBN. Keep the snapshot date on the Research page aligned with the records in `_data/projects.yml`, and express postdoctoral staffing as funded PD-months when that is how the award is specified. Citation/media totals have their own observation date in `_data/site_metrics.yml`; do not relabel either snapshot without rechecking its source. A publication linked to several projects is not several distinct papers.

The sitemap is generated solely by `jekyll-sitemap`. Legacy `/about/` and `/old.html` routes use the redirect layout and are excluded from the sitemap. Store logos locally and document their sources in `assets/images/funders/ATTRIBUTION.md`.


## Reviewing changes

Production is published from `master`; the collaboration page and the September audit updates are already merged. Create a new `review/*` or `audit/*` branch from current `master` for a new review. The `Build review site` workflow runs on both branch patterns, builds with the GitHub Pages Jekyll environment, and checks rendered pages, internal links, fragment targets, and the sitemap. It does not deploy GitHub Pages.

The workflow's `review-preview` artifact is ready for a manual Netlify deployment. Preview preparation disables search indexing and Cloudflare Analytics in the artifact; production source settings are preserved. Download and extract that artifact, then deploy its contents as the Netlify publish directory. Production remains on `master` until the review is approved.

The separate Netlify project `johannes-bjerva-review` hosts previews; it is not the live personal website. For a Git-connected preview, select the current review branch. `netlify.toml` builds and checks the site, then publishes `_preview`; its ignore rule allows only `audit/*` and `review/*`. For an explicit source-archive preview, omit the Git-only ignore rule from the upload copy because archive builds have no branch metadata. This route does not require GitHub Actions to run.

Before deleting old branches, check merge ancestry and open pull requests. Unmerged `agent/*` or `website-*` names alone do not establish that their work is disposable.

The collaboration page links to official programme descriptions rather than listing call deadlines. Review those links and the proposed contributions when preparing a specific proposal.
