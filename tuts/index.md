---
layout: page
title: Tutorials
---

Pages I made when I TA'd for these courses. For some of these courses, I have been a TA multiple times. However, there is now only one page for each course, having the materials sorted by year. Hopefully this is more useful for the future students who can find all the content in one place.

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
              <a href="/tuts{{ blink[0] | relative_url }}"> {{ link.desc }} </a>
            </div>
          </div>
          {%- endif -%}
        </article>
    {%- endfor -%}
</div>

Note that MA 105 was discontinued after 2019. Instead, it has been split into two courses: MA 109 and MA 111. If you're looking for content related to these two, then the MA 105 webpage would also be helpful.