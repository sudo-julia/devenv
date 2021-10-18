# dvnv

Automate the creation of development environments

[![Build Status](https://scrutinizer-ci.com/g/sudo-julia/dvnv/badges/build.png?b=main)](https://scrutinizer-ci.com/g/sudo-julia/dvnv/build-status/main)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/sudo-julia/dvnv/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/sudo-julia/dvnv/?branch=main)
[![Code Coverage](https://scrutinizer-ci.com/g/sudo-julia/dvnv/badges/coverage.png?b=main)](https://scrutinizer-ci.com/g/sudo-julia/dvnv/?branch=main)
![License](https://img.shields.io/github/license/sudo-julia/dvnv)

In the past, I managed multiple bash functions to create new directories for programming
projects. It worked fine, but I found myself repeating a lot of code. This
problem led to the creation of `dvnv`, a script manager for initializing new
development environments.

## Installation

```bash
git clone https://github.com/sudo-julia/dvnv
cd dvnv
pip install -U --user .
```

## Usage

`dvnv` takes two positional arguments - the first is the language of the new project,
and the second is the name. Upon calling `dvnv` with these two arguments,
scripts are run from two directories. The first is "all" (defaults to
`${XDG_CONFIG_HOME}/dvnv/scripts/all`). "all" scripts are run on the
initialization of any new project, regardless of the language. The second
directory searched is "lang" (defaults to `${XDG_CONFIG_HOME}/dvnv/${lang}`),
where "lang" is the first argument provided to `dvnv`. "lang" scripts are
only called for a project of a given language.

### Examples

- `dvnv python dvnv` calls upon scripts in `${XDG_CONFIG_HOME}/dvnv/scripts/all`
  as well as `${XDG_CONFIG_HOME}/dvnv/scripts/python`, providing all scripts with
  "python" as the first arg and "dvnv" as the second.

- `dvnv lua neovim` calls upon scripts in `${XDG_CONFIG_HOME}/dvnv/scripts/all`
  as well as `${XDG_CONFIG_HOME}/dvnv/scripts/lua`, providing all scripts with
  "lua" as the first arg and "neovim" as the second.

### Scripts

Scripts can be written in any language, as long as the file containing it is:

- Executable
- The first line is a _shebang_ in the case of an interpreted script (such as sh
  or python)

All scripts run by dvnv take two arguments, even if they're not used. This way,
scripts run by "all" can implement minor flow control with the language name. Scripts
can also use the new project name to create directories based on the new project.

"all" scripts are run before "lang" scripts. Found scripts are run in
alphabetical order.

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

As it's generally language-agnostic, a script such as the one above would be
best placed in the "all" folder. However, the script below would do best in
the "python" folder:

```bash
#!/bin/sh

poetry new "$2"
```

More example scripts can be found in [the scripts folder](./scripts). The
builtin scripts are installed on the first run. A reinstall can be forced by
running `dvnv` with the `--install_scripts` flag.
Most scripts that ship with `dvnv` are ports from my [~/bin](https://github.com/sudo-julia/bin)
directory and aim to be OS-Independent.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md)

## License

[Apache-2.0](./LICENSE)

## TODO

- [x] Update this README
- [ ] Option to show all language directories
- [ ] Ensure all scripts work
- [ ] rmtree before copying in copy_scripts
- [ ] Test scripts
