# Changelog

## v0.2.0

> Release date: 2021-10-12

### Additions

- The `scripts` directory is now included with an install, and the premade scripts
  can be copied to your local `scripts` folder using `dvnv --install_scripts`.

### Fixes

- Directories are no longer run as scripts

### Scripts

#### Fixes

- `gitignore` now runs

## v0.3.0

> Release date: 2021-10-15

### Additions

- `create_readme.py` added to scripts/all for README creation upon initialization
  of a new directory

- `rich` is added as a dependency for nicer terminal printing

- `dvnv` now includes a "quiet" option, where non-fatal messages will be
  suppressed. Try it with `dvnv -q [<args>]`!

### Fixes

- Warning headers are now printed in orange

## v0.4.0 - dvnv

> Release date: 2021-10-18

As of v0.4.0, `devenv` is renamed to `dvnv'. `dvnv` is quicker to type and wasn't
reserved on PyPi.

### Additions

- `dvnv` now includes an option to list available language folders; try it with
  `dvnv -l|--list`

- `dvnv` ships with a vim directory

- PyPi installation is added! `pip install dvnv`

### Fixes

- Code in dvnv.dvnv is restructured to allow for better coverage, ensuring less
  breakages in the future
