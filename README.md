# Ansible role - gitlab-runner
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-gitlab-runner?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-gitlab-runner?style=flat-square)](https://github.com/claranet/ansible-role-gitlab-runner/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-gitlab-runner/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-gitlab-runner/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/gitlab-runner)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure a Gitlab runner using Docker.

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.gitlab_runner
```

## :gear: Role variables

Variable | Default value | Description
---------|---------------|------------
null     | **null**      | null       

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - claranet.gitlab_runner


.
├── CONTRIBUTING.md
├── defaults
│   └── main.yml
├── HARDENING.md
├── LICENSE
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── converge.yml
│       ├── Dockerfile.j2
│       ├── molecule.yml
│       └── tests
│           └── test_default.py
├── README.md
├── tasks
│   ├── debian.yml
│   ├── main.yml
│   ├── redhat.yml
│   └── ubuntu.yml
└── vars
    ├── amazon.yml
    ├── debian-family.yml
    ├── main.yml
    └── redhat-family.yml
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
