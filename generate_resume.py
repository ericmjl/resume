import yaml
from flask import Flask, Markup, render_template, redirect
from jinja2 import Template

from markdown import markdown as md


def read_template(template):
    with open(template, 'r+') as f:
        template = f.read()
    t = Template(source=template)
    return t


def write_html(resume):
    """
    Write the HTML version of the resume to disk.
    """
    t = read_template('templates/resume.html')

    with open('index.html', 'w+') as f:
        f.write(t.render(resume=resume))


def read_resume(markup=True):
    """
    Read the resume from disk.
    """
    with open('resume.yaml', 'r+') as f:
        resume = yaml.load(f)

    if markup:
        for exp in resume['experience']:
            exp['description'] = Markup(md(exp['description']))
    return resume


def index():
    resume = read_resume(markup=True)
    write_html(resume)



if __name__ == "__main__":
    index()
