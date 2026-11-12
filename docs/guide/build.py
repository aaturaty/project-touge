#!/usr/bin/env python3
"""Builds the branded user guide page (index.html) from README.md (English) and README.fi.md (Finnish).

    python docs/guide/build.py

The page works offline: fonts, images and styles are in this folder, nothing is loaded from the network.
Edit the Markdown files, then run this script again. The same folder can be shipped inside Project Touge."""
import html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BANDS = {'3': 'band-build', '5': 'band-tune', '6': 'band-time'}


def slug(t):
    t = re.sub(r'[^\w\s-]', '', t.lower(), flags=re.U)
    return re.sub(r'\s+', '-', t.strip())


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', s)
    def link(m):
        t, u = m.group(1), m.group(2)
        if u.endswith('.md') or u == 'index.html':
            return ''          # language links are replaced by the switch in the header
        ext = u.startswith('http')
        return f'<a href="{u}"' + (' target="_blank" rel="noopener"' if ext else '') + f'>{t}</a>'
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = s.replace('◐', '<span class="mk">◐</span>')
    return s


def convert(md, lang):
    out, toc, i, L = [], [], 0, md.splitlines()
    open_sec = False
    while i < len(L):
        r = L[i]
        if not r.strip() or r.strip() == '---':
            i += 1; continue
        m = re.match(r'(#{1,4}) (.*)', r)
        if m:
            n, t = len(m.group(1)), m.group(2)
            if n == 1:
                i += 1; continue      # title comes from the header
            if n == 2:
                if open_sec: out.append('</section>')
                num = t.split('.')[0]
                band = BANDS.get(num)
                out.append(f'<section class="ch" id="{lang}-{slug(t)}">')
                if band:
                    out.append(f'<div class="band" style="background-image:url(assets/{band}.webp)" aria-hidden="true"></div>')
                out.append(f'<h2><span class="no">{html.escape(num.zfill(2))}</span>{inline(t.split(". ", 1)[-1])}</h2>')
                toc.append((f'{lang}-{slug(t)}', num.zfill(2), t.split('. ', 1)[-1]))
                open_sec = True
            else:
                out.append(f'<h{n} id="{lang}-{slug(t)}">{inline(t)}</h{n}>')
            i += 1; continue
        if r.startswith('|'):
            rows = []
            while i < len(L) and L[i].startswith('|'):
                rows.append([c.strip() for c in L[i].strip().strip('|').split('|')]); i += 1
            head, body = rows[0], [x for x in rows[1:] if not all(re.fullmatch(r':?-+:?', c) for c in x)]
            out.append('<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>'
                       + ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row) + '</tr>' for row in body) + '</tbody></table></div>')
            continue
        if re.match(r'(\d+\.|-) ', r):
            ordered = r[0].isdigit()
            items = []
            while i < len(L) and re.match(r'(\d+\.|-) ', L[i]):
                items.append(re.sub(r'^(\d+\.|-) ', '', L[i])); i += 1
                while i < len(L) and L[i].startswith('   ') and L[i].strip():
                    items[-1] += ' ' + L[i].strip(); i += 1
            tag = 'ol' if ordered else 'ul'
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')
            continue
        if r.startswith('!['):
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', r)
            out.append(f'<figure><a href="{m.group(2)}" target="_blank" rel="noopener"><img src="{m.group(2)}" alt="{html.escape(m.group(1))}" loading="lazy"></a>'
                       f'<figcaption>{html.escape(m.group(1))}</figcaption></figure>')
            i += 1; continue
        para = [r]
        i += 1
        while i < len(L) and L[i].strip() and not re.match(r'(#|\||!\[|\d+\. |- |---)', L[i]):
            para.append(L[i]); i += 1
        txt = inline(' '.join(para))
        if re.sub(r'[\s·]', '', txt) and '<b>Build, tune' not in txt:      # the tagline is in the header
            fine = 'unofficial fan-made' in txt or 'epävirallinen' in txt
            out.append(f'<p class="fine">{txt}</p>' if fine else f'<p>{txt}</p>')
    if open_sec: out.append('</section>')
    # drop the Markdown contents list, the sidebar replaces it
    body = '\n'.join(out)
    body = re.sub(r'<p>(Contents|Sisältö)</p>\s*<ol>.*?</ol>', '', body, count=1, flags=re.S)
    return body, toc


def page():
    parts = {}
    for lang, f in (('en', 'README.md'), ('fi', 'README.fi.md')):
        parts[lang] = convert(open(os.path.join(HERE, f), encoding='utf-8').read(), lang)
    def nav(lang):
        return ''.join(f'<li><a href="#{a}"><span>{n}</span>{html.escape(t)}</a></li>' for a, n, t in parts[lang][1])
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    return (tpl.replace('{{NAV_EN}}', nav('en')).replace('{{NAV_FI}}', nav('fi'))
               .replace('{{BODY_EN}}', parts['en'][0]).replace('{{BODY_FI}}', parts['fi'][0]))


if __name__ == '__main__':
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(page())
    print('wrote', os.path.join(HERE, 'index.html'))
