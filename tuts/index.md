---
layout: page
title: Tutorials
---

Pages I made when I TA'd these courses

<div class="posts-list">
    {%- for blink in site.data.tut-links -%}
        {%- assign link = blink[1] -%}
        <article class="post-preview">
          <a href="/tuts{{ blink[0] | relative_url }}">
          <h2 class="post-title">{{ link.tit }}</h2>
          </a>
          {%- if link.desc -%}
          <div class="post-entry-container">
            <div class="post-entry">
              <a href="/math{{ blink[0] | relative_url }}"> {{ link.desc }} </a>
            </div>
          </div>
          {%- endif -%}
        </article>
    {%- endfor -%}
</div>
