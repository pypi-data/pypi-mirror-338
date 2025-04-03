# module QC data tools v1.1.3

This project contains the modules needed to write/read the data files used in
the module QC flow. This project is to be added as a submodule in other
projects.

## Installation

Note that please use the latest python version. Python3.7 is the minimum
requirement for developers.

### via clone

First clone the project:

```
git clone https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-data-tools.git
```

Upon a successful checkout, `cd` to the new `module-qc-data-tools` directory and
run the following to install the necessary software:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install -e .
```

### via pip

```bash
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -U pip module-qc-data-tools==1.1.3
```

## Developer

### versioning

In case you need to tag the version of the code, you need to have either `hatch`
or `pipx` installed.

1. Activate python environment, e.g. `source venv/bin/activate`.
2. Run `python -m pip install hatch` or `python -m pip install pipx`.

You can bump the version via:

```bash
$ pipx run hatch run tag x.y.z
# or
$ hatch run tag x.y.z
```

where `x.y.z` is the new version to use. This should be run from the default
branch (`main` / `master`) as this will create a commit and tag, and push for
you. So make sure you have the ability to push directly to the default branch.

Release candidates can be bumped as e.g.:

```bash
$ hatch run tag x.y.zrc0
```

### pre-commit

Install pre-commit to avoid CI failure. Once pre-commit is installed, a git hook
script will be run to identify simple issues before submission to code review.

Instruction for installing pre-commit in a python environment:

1. Activate python environment, e.g. `source venv/bin/activate`.
2. Run `python -m pip install pre-commit`.
3. Run `pre-commit install` to install the hooks in `.pre-commit-config.yaml`.

After installing pre-commit, `.pre-commit-config.yaml` will be run every time
`git commit` is done. Redo `git add` and `git commit`, if the pre-commit script
changes any files.
