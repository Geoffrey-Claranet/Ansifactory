#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

def test_gitlab_runner_version(host):
    host.run_expect([0], "gitlab-runner -v")

def test_svc(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
      svc = host.service("gitlab-runner")
    else:
      svc = host.service("gitlab-runner")
    assert svc.is_running
    assert svc.is_enabled

def test_config_toml(host):
    config_toml = host.file("/etc/gitlab-runner/config.toml").content_string
    assert 'name = "super_description"' in config_toml
    assert 'environment = ["DOCKER_TLS_CERTDIR=/certs", "DOCKER_DRIVER=overlay2"]' in config_toml
    assert 'extra_hosts = ["localhost:172.17.0.1"]' in config_toml

def test_shell(host):
    command = host.run("sh --version")
    assert command.rc == 0
