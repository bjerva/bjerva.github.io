---
layout: default
title:
description: Professor of Natural Language Processing at Aalborg University, building linguistically grounded and trustworthy language AI across languages, with research spanning semantics, security, and privacy.
body_class: home
---

<section class="hero">
  <div class="shell hero-grid">
    <div class="hero-copy reveal">
      <p class="eyebrow">Professor · Natural Language Processing</p>
      <h1>Linguistically grounded, trustworthy language AI.</h1>
      <p class="hero-lead">Language is increasingly the interface through which AI systems reason, retrieve knowledge, and interact with people. At Aalborg University, I lead <a href="{{ '/group/' | relative_url }}">AAU-NLP</a> and study how linguistic structure and meaning can make these systems more reliable and secure across languages.</p>
      <div class="hero-actions">
        <a class="button primary" href="{{ '/research/' | relative_url }}">Explore my research</a>
        <a class="button text" href="{{ '/publications/' | relative_url }}">Selected publications <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <div class="portrait-wrap reveal delay-1">
      <div class="portrait-frame">
        <img src="{{ '/images/Johannes%20Bjerva_a%20(002).jpg' | relative_url }}" alt="Johannes Bjerva" width="945" height="1417" decoding="async" fetchpriority="high">
      </div>
      <div class="portrait-note">
        <span class="signal-dot" aria-hidden="true"></span>
        Aalborg University · Copenhagen
      </div>
    </div>
  </div>
</section>

<section class="section evidence-section">
  <div class="shell">
    <p class="eyebrow reveal">At a glance</p>
    <div class="evidence-grid">
      <article class="evidence-card reveal">
        <p class="evidence-label">Research funding</p>
        <p class="evidence-value"><span>{{ site.data.site_metrics.funding.prefix }}</span> {{ site.data.site_metrics.funding.total }}</p>
        <p>{{ site.data.site_metrics.funding.summary }}</p>
        <a href="{{ '/research/#projects' | relative_url }}">Funding portfolio <span aria-hidden="true">→</span></a>
      </article>
      <article class="evidence-card reveal delay-1">
        <p class="evidence-label">Research programme</p>
        <ul class="outlet-list" aria-label="Research programme">
          <li>Multilingual language understanding</li>
          <li>Trustworthy and secure language models</li>
          <li>Linguistic analysis of meaning</li>
        </ul>
        <p>Three connected strands, grounded in linguistic structure and evaluated across languages.</p>
        <a href="{{ '/research/' | relative_url }}">Research vision <span aria-hidden="true">→</span></a>
      </article>
      <article class="evidence-card reveal delay-2">
        <p class="evidence-label">Research and public reach</p>
        <p class="evidence-value">{{ site.data.site_metrics.reach.citations }}</p>
        <p>citations · {{ site.data.site_metrics.reach.media }} {{ site.data.site_metrics.reach.media_label }}<br><span class="metric-date">as of {{ site.data.site_metrics.reach.as_of }}</span></p>
        <div class="evidence-links"><a href="https://scholar.google.com/citations?user=F9zlUBcAAAAJ&hl=en">Scholar <span aria-hidden="true">↗</span></a><a href="{{ '/service/' | relative_url }}">Engagement <span aria-hidden="true">→</span></a></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell news-grid">
    <div class="news-heading">
      <p class="eyebrow">Selected highlights</p>
      <h2>Recent work</h2>
      <p>A selective timeline of research and career milestones.</p>
    </div>
    <ol class="timeline">
      {% for item in site.data.highlights %}
        <li class="reveal">
          <time>{{ item.date }}</time>
          <div><h3>{% if item.url %}<a href="{{ item.url }}">{{ item.title | escape }}</a>{% else %}{{ item.title | escape }}{% endif %}</h3><p>{{ item.text | escape }}</p></div>
        </li>
      {% endfor %}
    </ol>
  </div>
</section>

<section class="contact-band">
  <div class="shell contact-band-inner">
    <div><p class="eyebrow">Collaboration</p><h2>For research, media, or policy collaboration.</h2></div>
    <a class="button light" href="mailto:jbjerva@cs.aau.dk">Get in touch</a>
  </div>
</section>
