---
layout: page
title: Algoritmisk fagterminologi
---

<dl>
{% assign sortedwords = site.data.words | sort: 'title' %}
{%- for word in sortedwords %}
<dt><a href="{{site.baseurl}}/words/{{ word.title | slugify: 'latin' }}">{{word.title}}</a>
</dt>
<dd> {{word.definition}}
{%- if word.constructions -%}
{% for construct in word.constructions %}
<b>{{ construct.title|capitalize }}</b>, {{construct.definition}}. 
{%- endfor -%}
{%- endif %}
</dd>
{% endfor %}
</dl>

---

<div class="small center">
<p><a href="https://github.com/missing-semester/missing-semester">Source code</a>.</p>
<p>Licensed under CC BY-NC-SA.</p>
</div>
