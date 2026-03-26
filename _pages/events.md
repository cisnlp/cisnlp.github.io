---
title: "Schütze Lab - Events"
layout: textlay
excerpt: "Schütze Lab -- Events"
sitemap: false
permalink: /events/
---

## Events

{% for event in site.data.events %}

<div markdown="0" class="event-header">
  <img
    src="{{ site.url }}{{ site.baseurl }}/images/visitorpic/{{ event.photo }}"
    alt="{{ event.speaker }}"
    class="event-photo {% unless event.round_photo == false %}round{% endunless %}"
    width="150"
  />

  <div>
    <h3>{{ event.title }}</h3>
    <strong>{{ event.speaker }}</strong><br>
    📅 {{ event.date }}<br>
    📍 {{ event.location }}
  </div>
</div>


<strong>Abstract</strong>

{{ event.abstract }}

<strong>Bio</strong>

{{ event.bio }}


---

{% endfor %}