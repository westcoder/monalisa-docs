import os
from glob import glob

from invoke import task

DOCS_PORT = os.environ.get("DOCS_PORT", 8100)


@task
def clean(c):
    """Remove artifacts and binary files."""
    # c.run("python setup.py clean --all")
    patterns = ["build", "dist"]
    patterns.extend(glob("*.egg*"))
    patterns.append("_build")
    patterns.append("**/*.pyc")
    for pattern in patterns:
        c.run(f"rm -rf {pattern}")


@task(pre=[clean])
def docbuild(c):
    """Build documentation."""
    build_dir = os.environ.get("BUILD_DIR", "_build/html")
    c.run("python -msphinx -W -b html -d _build/doctrees . %s" % build_dir)


@task
def doclang(c):
    c.run("make gettext")
    c.run("sphinx-intl update -p _build/gettext -l de -l fr -l it -l es -l hu -l nl -l fi -l sv -l sl")


@task(docbuild)
def docserve(c):
    """Serve docs at http://localhost:$DOCS_PORT/ (default port is 8100)."""
    from livereload import Server

    server = Server()
    server.watch("conf.py", lambda: docbuild(c))
    server.watch("*.rst", lambda: docbuild(c))
    server.serve(port=DOCS_PORT, root="_build/html")
