import yaml
from flask import Flask, render_template, Markup
from markdown import markdown as md
from jinja2 import Template


app = Flask(__name__)
with open('resume.yaml', 'r+') as f:
    resume = yaml.load(f)

for exp in resume['experience']:
    exp['description'] = Markup(md(exp['description']))

with open('templates/resume.html.j2', 'r+') as f:
    template = f.read()

t = Template(source=template)

with open('index.html', 'w+') as f:
    f.write(t.render(resume=resume))


@app.route('/')
def view_resume():
    return render_template('resume.html.j2', resume=resume)


if __name__ == '__main__':
    app.run(debug=True)
