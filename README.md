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

### Scripts

- "${CONFIG}": whatever directory `appdirs` finds as `user_config_dir`
- "${lang}": the first argument passed to `devenv` as it's run; `devenv python
  newproj`'s "${lang}" would be `python`, `devenv lua luaproj` would be `lua`, and so on
  and so forth.

`devenv` will automatically run scripts found in "${CONFIG}/devenv/scripts/all" and
"${CONFIG}/devenv/scripts/${lang}" upon being called.

`devenv` ships with some starter scripts I wrote, which will need to be copied from
`devenv`'s install location to the directory I mentioned above.

- All scripts take 2 args: 1st is lang, 2nd is project name
- "all" scripts run first, "lang" scripts run second

## License

[Apache-2.0](./LICENSE)
