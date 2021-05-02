"""
Build script for resume HTML version.
"""
import os

from app import write_html, read_resume
import shutil

shutil.rmtree("site/")
os.makedirs("site/", exist_ok=True)

resume = read_resume()
write_html(resume, path="site/index.html")


shutil.copytree("static", "site/static")
