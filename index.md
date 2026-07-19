---
layout: default
title:
description: Professor of Natural Language Processing at Aalborg University, leading research on multilingual NLP, language-model security, and linguistically grounded AI safety.
body_class: home
---

<section class="hero">
  <div class="shell hero-grid">
    <div class="hero-copy reveal">
      <p class="eyebrow">Professor · Natural Language Processing</p>
      <h1>Language, meaning, and security in modern AI systems.</h1>
      <p class="hero-lead">I lead <a href="{{ '/group/' | relative_url }}">AAU-NLP</a> at Aalborg University. My research brings linguistics and machine learning together to build language technologies that are multilingual, secure, and worthy of trust.</p>
      <div class="hero-actions">
        <a class="button primary" href="{{ '/research/' | relative_url }}">Explore my research</a>
        <a class="button text" href="https://scholar.google.com/citations?user=F9zlUBcAAAAJ&hl=en">View publications <span aria-hidden="true">↗</span></a>
      </div>
      <ul class="role-list" aria-label="Current roles">
        <li>Professor of NLP, Aalborg University</li>
        <li>Head of the Copenhagen Section, Department of Computer Science</li>
        <li>Member of the Young Academy of Denmark</li>
      </ul>
    </div>
    <div class="portrait-wrap reveal delay-1">
      <div class="portrait-frame">
        <img src="{{ '/images/Johannes%20Bjerva_a%20(002).jpg' | relative_url }}" alt="Johannes Bjerva" width="800" height="960">
      </div>
      <div class="portrait-note">
        <span class="signal-dot" aria-hidden="true"></span>
        Aalborg University · Copenhagen
      </div>
    </div>
  </div>
</section>

<section class="section research-intro">
  <div class="shell">
    <div class="section-heading reveal">
      <p class="eyebrow">Research</p>
      <h2>Understanding language is central to making AI work safely across people, systems, and languages.</h2>
    </div>
    <div class="pillar-grid">
      <article class="pillar reveal">
        <span class="pillar-index">01</span>
        <h3>Language-model security</h3>
        <p>I study how language models leak, manipulate, and misrepresent information—and how linguistic evidence can make these failures easier to detect and prevent.</p>
        <a href="{{ '/research/#security' | relative_url }}">Security research <span aria-hidden="true">→</span></a>
      </article>
      <article class="pillar reveal delay-1">
        <span class="pillar-index">02</span>
        <h3>Multilingual NLP</h3>
        <p>I develop linguistically informed methods and evaluations that work beyond a small set of high-resource languages, drawing especially on linguistic typology.</p>
        <a href="{{ '/research/#multilingual' | relative_url }}">Multilingual research <span aria-hidden="true">→</span></a>
      </article>
      <article class="pillar reveal delay-2">
        <span class="pillar-index">03</span>
        <h3>Linguistic structure and meaning</h3>
        <p>I study how linguistic structure and formal meaning representations can help us analyse what language models learn, infer, and communicate.</p>
        <a href="{{ '/research/#semantics' | relative_url }}">Semantics research <span aria-hidden="true">→</span></a>
      </article>
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="shell split-heading">
    <div>
      <p class="eyebrow">Current programmes</p>
      <h2>Research at scale</h2>
    </div>
    <p>I lead interdisciplinary programmes supported by the Novo Nordisk Foundation, Independent Research Fund Denmark, the Carlsberg Foundation, and Aalborg University.</p>
  </div>
  <div class="shell project-preview">
    {% for project in site.data.projects limit: 4 %}
      <a class="project-card reveal" href="{{ project.url }}">
        <div class="project-topline"><span>{{ project.period }}</span><span>{{ project.role }}</span></div>
        <h3>{{ project.title | escape }}</h3>
        <p class="project-subtitle">{{ project.subtitle | escape }}</p>
        <p>{{ project.description | escape }}</p>
        <div class="project-meta"><span>{{ project.funder | escape }}</span><span aria-hidden="true">↗</span></div>
      </a>
    {% endfor %}
  </div>
  <div class="shell section-link"><a class="button outline" href="{{ '/research/' | relative_url }}">All research programmes</a></div>
</section>

<section class="section">
  <div class="shell news-grid">
    <div class="news-heading">
      <p class="eyebrow">Selected highlights</p>
      <h2>Recent work</h2>
      <p>A selective record of developments, rather than a running activity log.</p>
    </div>
    <ol class="timeline">
      {% for item in site.data.highlights %}
        <li class="reveal">
          <time>{{ item.date }}</time>
          <div><h3>{{ item.title | escape }}</h3><p>{{ item.text | escape }}</p></div>
        </li>
      {% endfor %}
    </ol>
  </div>
</section>

<section class="contact-band">
  <div class="shell contact-band-inner">
    <div><p class="eyebrow">Collaboration</p><h2>Interested in secure, multilingual, or meaning-aware AI?</h2></div>
    <a class="button light" href="mailto:jbjerva@cs.aau.dk">Get in touch</a>
  </div>
</section>
