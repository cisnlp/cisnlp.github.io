---
title: "News"
layout: textlay
excerpt: "Schütze Lab at LMU Munich."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
