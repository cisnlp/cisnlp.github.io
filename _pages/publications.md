---
title: "Schütze Lab - Publications"
layout: gridlay
excerpt: "Schütze Lab -- Publications."
sitemap: false
permalink: /publications/
---

# Publications

<div id="publications-container">
  {% assign sorted_pubs = site.data.publist | sort: 'year' | reverse %}
  {% for pub in sorted_pubs %}
  <div markdown='0' class="pub-box" data-index="{{ forloop.index0 }}" onclick="openPdf('{{ pub.url }}')">
    <p><strong>{{ pub.authors }}</strong></p>
    <p><em>{{ pub.title }}</em></p>
    {% if pub.proceedings %}
    <p>{{ pub.proceedings }}</p>
    {% endif %}
    <p>
      {% if pub.url %}<a href="{{ pub.url }}" target="_blank" onclick="event.stopPropagation()">[PDF]</a>{% endif %}
      <!-- {% if pub.bib %}<a href="{{ pub.bib }}" target="_blank" onclick="event.stopPropagation()">[BibTeX]</a>{% endif %} -->
    </p>
  </div>
  {% endfor %}
</div>

<button id="show-more-btn" onclick="showAllPubs()">Show All</button>

<style>
#publications-container {
  display: flex;
  flex-direction: column;
  gap: 1em;
}

.pub-box {
  border: 1px solid #6AA695;
  padding: 1em;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
}

.pub-box:hover {
  background: #f9f9f9;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

#show-more-btn {
  margin-top: 1em;
  padding: 0.5em 1em;
  border: none;
  background: #007ACC;
  color: white;
  border-radius: 6px;
  cursor: pointer;
}

#show-more-btn:hover {
  background: #005A99;
}
</style>

<script>
const maxVisible = 20;

document.addEventListener("DOMContentLoaded", () => {
  const pubs = document.querySelectorAll(".pub-box");
  pubs.forEach((pub, i) => {
    if (i >= maxVisible) pub.style.display = "none";
  });
  if (pubs.length <= maxVisible) {
    document.getElementById("show-more-btn").style.display = "none";
  }
});

function showAllPubs() {
  document.querySelectorAll(".pub-box").forEach(pub => pub.style.display = "block");
  document.getElementById("show-more-btn").style.display = "none";
}

function openPdf(url) {
  window.open(url, "_blank");
}
</script>