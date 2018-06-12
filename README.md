# resume-generator

Building a resume using nothing but YAML files. A prototype. Inspired by https://github.com/salomonelli/best-resume-ever

## howto

I have provided an `environment.yml` file, which specifies a conda environment that can be used.

To get it running:

```bash
$ conda env create -f environment.yml
```

When done, run the app:

```bash
$ python app.py
```

This will run the app, and will also save it to disk as `index.html`. The app provides a convenient way to preview any changes made. When done, simply exit out of the app (`Ctrl+C`), and push changes up to GitHub.
