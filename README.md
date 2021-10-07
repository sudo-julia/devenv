# devenv

Automate the creation of development environments

[![Build Status](https://scrutinizer-ci.com/g/sudo-julia/devenv/badges/build.png?b=main)](https://scrutinizer-ci.com/g/sudo-julia/devenv/build-status/main)
![Code quality](https://img.shields.io/scrutinizer/quality/g/sudo-julia/devenv)
![License](https://img.shields.io/github/license/sudo-julia/devenv)

In the past, I managed multiple bash functions to create new directories for programming
projects. It worked fine, but I found myself repeating a lot of code. This problem led
to the creation of `devenv`, a script manager for initializing new development
environments.

## Installation

```bash
git clone https://github.com/sudo-julia/devenv
cd devenv
pip install -U --user .
```

## Usage

`devenv` takes two positional arguments - the first is the language of the new project,
and the second is the name. Upon calling `devenv` with these two arguments, scripts are run from two
directories. The first is "all" (defaults to `${XDG_CONFIG_HOME}/devenv/scripts/all`). "all"
scripts are run on the initialization of any new project, regardless of the language.
The second directory searched is "lang" (defaults to `${XDG_CONFIG_HOME}/devenv/${lang}`),
where "lang" is the first argument provided to `devenv`. "lang" scripts are only called for a
project of a given language.

### Examples

- `devenv python devenv` calls upon scripts in `${XDG_CONFIG_HOME}/devenv/scripts/all`
  as well as `${XDG_CONFIG_HOME}/devenv/scripts/python`, providing all scripts with
  "python" as the first arg and "devenv" as the second.

- `devenv lua neovim` calls upon scripts in `${XDG_CONFIG_HOME}/devenv/scripts/all`
  as well as `${XDG_CONFIG_HOME}/devenv/scripts/lua`, providing all scripts with
  "lua" as the first arg and "neovim" as the second.

### Scripts

> Note: builtin scripts are not currently in a working state, so use at your own risk.
> `devenv` itself should work fine, though.

All scripts run by devenv take two arguments, even if they're not used. This way,
scripts run by "all" can implement minor flow control with the language name. Scripts
can also use the new project name to create directories based on the new project.

"all" scripts are run before "lang" scripts. Found scripts are run in alphabetical order.

#### Example Scripts

The following script utilizes both `$1` and `$2`:

```bash
#!/bin/sh

# create a new directory with the new project's name
mkdir -p -- "$2"

# if the language is python, create a second directory with the same name
# otherwise, create a "src" directory
if [ "$1" = python ]; then
  mkdir -- "${2}/${2}"
else
  mkdir -- "${2}/src"
fi
```

As it's generally language-agnostic, a script such as the one above would be best placed
in the "all" folder. However, the script below would do best in the "python" folder:

```bash
#!/bin/sh

poetry new "$2"
```

More example scripts can be found in [the scripts folder](./scripts). The builtin scripts
are installed on the first run. A reinstall can be forced by running `devenv` with the
`--install_scripts` flag. As of now (v0.1.1), not all the scripts work/have tests, so be
careful running them! Most scripts that ship with `devenv` are ports from my [~/bin](https://github.com/sudo-julia/bin) directory and
aim to be OS-Independent.

## License

[Apache-2.0](./LICENSE)

## TODO

- [x] Update this README
- [ ] Ensure all scripts work
- [ ] Test scripts
