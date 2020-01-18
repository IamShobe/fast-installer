fast-installer
==============

make fast install configurations using config file:

Example:
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


## config file

Base structure:

Key                 | Type        | Is Required |  Comments
:-----------:       |:-----------:|:-----------:|:---------:
options             | list        |    yes      |  list of dictionaries of [option](#option)s


### option
a dictionary with the following keys:

Key          | Type        | Is Required |  Comments
:-----------:|:-----------:|:-----------:|:---------:
description  | string      |    yes      |
key          | string      |    yes      |
steps        | list        |    yes      |  list of dictionaries of [step](#step)


### step
a dictionary with the following keys:

Key            | Type        | Is Required |  Comments
:-----------:  |:-----------:|:-----------:|:---------:
description    | string      |    yes      |
[links](#links)| dictionary  |    no       |   make a soft link


### links
a dictionary where the key is the dest soft link location and value is the source location.

example:
```yaml
links:
  ~/.zshrc.d: assets/zsh/zshrc.d/
```