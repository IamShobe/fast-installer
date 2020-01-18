fast-installer
==============

make fast install configurations using config file:


## Install
```bash
pip3 install fast-installer
```


## Usage

cli:
```bash
fastinstall  # this will run current directory config.yaml file.
```

to install all steps:
```bash
fastisntall -a
```

for more:
```bash
fastinstall -h
```


## config file

### Example
```yaml
options:
  - description: "Zsh configurations"
    key: zsh
    steps:
      - description: "Linking files"
        links:
          ~/.zshrc.d: assets/zsh/zshrc.d/
          ~/.zshrc: assets/zsh/zshrc
```

### Structure

Key                 | Type        | Is Required |  Comments
:-----------:       |:-----------:|:-----------:|:---------:
options             | list        |    yes      |  list of [option](#option)s


#### option
a dictionary with the following keys:

Key          | Type        | Is Required |  Comments
:-----------:|:-----------:|:-----------:|:---------:
description  | string      |    yes      |
key          | string      |    yes      |
steps        | list        |    yes      |  list of [step](#step)s

The steps will be run from the first to the last.

#### step
a dictionary with the following keys:

Key            | Type        | Is Required |  Comments
:-----------:  |:-----------:|:-----------:|:---------:
description    | string      |    yes      |
[links](#links)| dictionary  |    no       |   make a soft link


#### links
a dictionary where the key is the dest soft link location and value is the source location.

##### Example
```yaml
links:
  ~/.zshrc.d: assets/zsh/zshrc.d/
```
