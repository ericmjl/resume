"""Simple flask app to preview resume."""
import yaml
from flask import Flask, Markup, redirect, render_template
from jinja2 import Template
from markdown import markdown as md

app = Flask(__name__)


def read_template(template):
    with open(template, "r+") as f:
        template = f.read()
    t = Template(source=template)
    return t


def write_html(resume, path="index.html"):
    """
    Write the HTML version of the resume to disk.
    """
    t = read_template("templates/resume.html")

    with open(path, "w+") as f:
        f.write(t.render(resume=resume))


def write_markdown(resume):
    """
    Write the Markdown version of the resume to disk.
    """
    t = read_template("templates/resume.md.j2")
    with open("resume.md", "w+") as f:
        f.write(t.render(resume=resume))


def read_resume(markup=True):
    """
    Read the resume from disk.
    """
    with open("resume.yaml", "r+") as f:
        resume = yaml.load(f)

    if markup:
        for exp in resume["experience"]:
            exp["description"] = Markup(md(exp["description"]))
    return resume


def make_html():
    resume = read_resume(markup=True)
    html = render_template("resume.html", resume=resume)
    return html


@app.route("/")
def index():
    return make_html()


@app.route("/markdown")
@app.route("/md")
def markdown():
    resume = read_resume(markup=False)
    write_markdown(resume)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5657)
