# Changelog

## v0.2.0

> Release date: 2021-10-12

### Additions

- The `scripts` directory is now included with an install, and the premade scripts
  can be copied to your local `scripts` folder using `devenv --install_scripts`.

### Fixes

- Directories are no longer run as scripts

### Scripts

#### Fixes

- `gitignore` now runs

## v0.3.0

> Release date: 2021-10-15

### Additions

- `create_readme.py` added to scripts/all for README creation upon initialzation
  of a new directory

- `rich` is added as a dependency for nicer terminal printing

- `devenv` now includes a "quiet" option, where non-fatal messages will be
  supressed. Try it with `devenv -q [<args>]`!

### Fixes

- Warning headers are now printed in orange
