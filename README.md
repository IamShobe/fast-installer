fast-installer
==============

make fast install configurations using config file:

![Image](https://github.com/IamShobe/fast-installer/blob/master/example.PNG?raw=true)

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
fastinstall -a
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
        shell:
          - echo "test"
          - command: ls not_exists
            allow_fail: true
          - command: tail -f /dev/null
            allow_fail: true
            timeout: 1  # 1 seconds           
```

### Structure

Key                 | Type        | Is Required |  Comments
:-----------:       |:-----------:|:-----------:|:---------
options             | list        |    yes      |  list of [option](#option)s


#### option
a dictionary with the following keys:

Key          | Type        | Is Required |  Comments
:-----------:|:-----------:|:-----------:|:---------
description  | string      |    yes      |
key          | string      |    yes      |
steps        | list        |    yes      |  list of [step](#step)s

The steps will be run from the first to the last.

#### step
a dictionary with the following keys:

Key            | Type              | Is Required |  Comments
:-----------:  |:-----------:      |:-----------:|:---------
description    | string            |    yes      |
[links](#links)| dictionary        |    no       |   make a soft link
[shell](#shell)| dictionary/string | no          | execute shell command


#### links
a dictionary where the key is the dest soft link location and value is the source location.

##### Example
```yaml
links:
  ~/.zshrc.d: assets/zsh/zshrc.d/
```

#### shell
execute a shell command.
can be either a string (which is the shell command to be executed).
or a dictionary:

Key            | Type              | Is Required |  Comments
:-----------:  |:-----------:      |:-----------:|:---------
command        | string            |    yes      |   command to be executed
allow_fail     | bool              |    no       |   allow command to fail - default True
timeout        | int               |    no       |   timeout for the command - default 10 seconds

