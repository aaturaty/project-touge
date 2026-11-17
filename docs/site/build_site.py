#!/usr/bin/env python3
"""Builds the Project Touge GitHub Pages site from the docs folder.

    pip install markdown
    python docs/site/build_site.py _site

Output:
    _site/index.html            landing page with the three guides
    _site/guide/                user guide (docs/guide, index.html rebuilt with build.py)
    _site/sharing/              sharing walkthrough (docs/sharing)
    _site/tuning-bible/         choriso's Tuning Bible, every .md rendered to .html (fi/ in Finnish)

Edit the Markdown in docs/, not the output. The GitHub Actions workflow .github/workflows/pages.yml runs this on every push
to main that touches docs/ and publishes the result."""
import html
import os
import re
import shutil
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
GUIDE = os.path.join(DOCS, 'guide')
SHARING = os.path.join(DOCS, 'sharing')
BIBLE = os.path.join(DOCS, 'tuning-guide')


def page(title, body, rel, lang='en', desc=''):
    """Site shell: fonts from the user guide's assets (copied to _site/assets), top bar with the three guides."""
    tpl = open(os.path.join(HERE, 'shell.html'), encoding='utf-8').read()
    return (tpl.replace('{{title}}', html.escape(title)).replace('{{desc}}', html.escape(desc))
            .replace('{{lang}}', lang).replace('{{rel}}', rel).replace('{{body}}', body))


def md_links(s):
    """Point links between Markdown files at the rendered pages. External links and other files stay as they are."""
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r'^[a-z]+:', url) or url.startswith('#'):
            return m.group(0)
        path, _, frag = url.partition('#')
        if path.endswith('.md'):
            path = re.sub(r'(^|/)README\.md$', r'\1index.html', path)
            path = re.sub(r'\.md$', '.html', path)
            url = path + ('#' + frag if frag else '')
        return f'{attr}="{url}"'
    return re.sub(r'(href)="([^"]+)"', fix, s)


def render_bible(out):
    md = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists', 'attr_list'])
    for root, _, files in os.walk(BIBLE):
        sub = os.path.relpath(root, BIBLE)
        dest = os.path.join(out, 'tuning-bible', '' if sub == '.' else sub)
        os.makedirs(dest, exist_ok=True)
        depth = 0 if sub == '.' else sub.count(os.sep) + 1
        rel = '../' * (depth + 1)
        lang = 'fi' if sub.split(os.sep)[0] == 'fi' else 'en'
        for f in files:
            src = os.path.join(root, f)
            if not f.endswith('.md'):
                shutil.copy2(src, os.path.join(dest, f))
                continue
            text = open(src, encoding='utf-8').read()
            md.reset()
            body = md_links(md.convert(text))
            m = re.search(r'^# (.+)$', text, re.M)
            name = m.group(1).strip() if m else 'Tuning Bible'
            title = "choriso's Tuning Bible" if f == 'README.md' else f"{name} · choriso's Tuning Bible"
            body = f'<main class="doc bible">{body}</main>'
            name_out = 'index.html' if f == 'README.md' else f[:-3] + '.html'
            with open(os.path.join(dest, name_out), 'w', encoding='utf-8') as o:
                o.write(page(title, body, rel, lang, 'How CarX Street calculates the car and what each setting really does.'))


def main(out):
    out = os.path.abspath(out)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    # user guide: rebuild index.html from the Markdown so the site never lags behind it
    subprocess.run([sys.executable, os.path.join(GUIDE, 'build.py')], check=True)
    shutil.copytree(GUIDE, os.path.join(out, 'guide'), ignore=shutil.ignore_patterns('*.py', 'template.html', '*.md'))
    shutil.copytree(SHARING, os.path.join(out, 'sharing'))
    shutil.copytree(os.path.join(GUIDE, 'assets'), os.path.join(out, 'assets'))
    render_bible(out)
    shutil.copy2(os.path.join(BIBLE, 'banner.png'), os.path.join(out, 'assets', 'bible-banner.png'))
    landing = open(os.path.join(HERE, 'index.html'), encoding='utf-8').read()
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as o:
        o.write(page('Project Touge guides', landing, '', 'en', 'User guide, sharing walkthrough and Tuning Bible for Project Touge.'))
    open(os.path.join(out, '.nojekyll'), 'w').close()
    print('site:', out)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '_site')
