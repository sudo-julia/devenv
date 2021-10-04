# devenv

Automate the creation of development environments

## Installation

### Poetry

```bash
poetry install
poetry run devenv
```

### From Source

```bash
git clone https://github.com/sudo-julia/devenv
cd devenv
python3 setup.py sdist
pip install -U --user .
```

## Usage

Coming soon...

## License

[Apache-2.0](./LICENSE)

scripts dir in ${CONFIG}/devenv/scripts

- All scripts take 2 args: 1st is lang, 2nd is project name
- "all" scripts run first, "lang" scripts run second
