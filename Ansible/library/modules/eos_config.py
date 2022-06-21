#
# Copyright 2015 Peter Sprygada <psprygada@ansible.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
author: Peter Sprygada (@privateip)
description:
- Arista EOS configurations use a simple block indent file syntax for segmenting configuration
  into sections.  This module provides an implementation for working with EOS configuration
  sections in a deterministic way.  This module works with either CLI or eAPI transports.
extends_documentation_fragment: eos
module: eos_config
notes:
- Tested against EOS 4.15
- Abbreviated commands are NOT idempotent, see L(Network FAQ,../network/user_guide/faq.html#why-do-the-config-modules-always-return-changed-true-with-abbreviated-commands).
options:
  after:
    description:
    - The ordered set of commands to append to the end of the command stack if a change
      needs to be made.  Just like with I(before) this allows the playbook designer
      to append a set of commands to be executed after the command set.
  backup:
    default: 'no'
    description:
    - This argument will cause the module to create a full backup of the current C(running-config)
      from the remote device before any changes are made. If the C(backup_options)
      value is not given, the backup file is written to the C(backup) folder in the
      playbook root directory or role root directory, if playbook is part of an ansible
      role. If the directory does not exist, it is created.
    type: bool
    version_added: '2.2'
  backup_options:
    description:
    - This is a dict object containing configurable options related to backup file
      path. The value of this option is read only when C(backup) is set to I(yes),
      if C(backup) is set to I(no) this option will be silently ignored.
    suboptions:
      dir_path:
        description:
        - This option provides the path ending with directory name in which the backup
          configuration file will be stored. If the directory does not exist it will
          be first created and the filename is either the value of C(filename) or
          default filename as described in C(filename) options description. If the
          path value is not given in that case a I(backup) directory will be created
          in the current working directory and backup configuration will be copied
          in C(filename) within I(backup) directory.
        type: path
      filename:
        description:
        - The filename to be used to store the backup configuration. If the the filename
          is not given it will be generated based on the hostname, current time and
          date in format defined by _config.@
    type: dict
    version_added: '2.8'
  before:
    description:
    - The ordered set of commands to push on to the command stack if a change needs
      to be made.  This allows the playbook designer the opportunity to perform configuration
      commands prior to pushing any changes without affecting how the set of commands
      are matched against the system.
  defaults:
    default: 'no'
    description:
    - The I(defaults) argument will influence how the running-config is collected
      from the device.  When the value is set to true, the command used to collect
      the running-config is append with the all keyword.  When the value is set to
      false, the command is issued without the all keyword
    type: bool
    version_added: '2.2'
  diff_against:
    choices:
    - startup
    - running
    - intended
    - session
    default: session
    description:
    - When using the C(ansible-playbook --diff) command line argument the module can
      generate diffs against different sources.
    - When this option is configure as I(startup), the module will return the diff
      of the running-config against the startup-config.
    - When this option is configured as I(intended), the module will return the diff
      of the running-config against the configuration provided in the C(intended_config)
      argument.
    - When this option is configured as I(running), the module will return the before
      and after diff of the running-config with respect to any changes made to the
      device configuration.
    - When this option is configured as C(session), the diff returned will be based
      on the configuration session.
    version_added: '2.4'
  diff_ignore_lines:
    description:
    - Use this argument to specify one or more lines that should be ignored during
      the diff.  This is used for lines in the configuration that are automatically
      updated by the system.  This argument takes a list of regular expressions or
      exact line matches.
    version_added: '2.4'
  intended_config:
    description:
    - The C(intended_config) provides the master configuration that the node should
      conform to and is used to check the final running-config against.   This argument
      will not modify any settings on the remote device and is strictly used to check
      the compliance of the current device's configuration against.  When specifying
      this argument, the task should also modify the C(diff_against) value and set
      it to I(intended).
    type: str
    version_added: '2.4'
  lines:
    aliases:
    - commands
    description:
    - The ordered set of commands that should be configured in the section.  The commands
      must be the exact same commands as found in the device running-config.  Be sure
      to note the configuration command syntax as some commands are automatically
      modified by the device config parser.
  match:
    choices:
    - line
    - strict
    - exact
    - none
    default: line
    description:
    - Instructs the module on the way to perform the matching of the set of commands
      against the current device config.  If match is set to I(line), commands are
      matched line by line.  If match is set to I(strict), command lines are matched
      with respect to position.  If match is set to I(exact), command lines must be
      an equal match.  Finally, if match is set to I(none), the module will not attempt
      to compare the source configuration with the running configuration on the remote
      device.
  parents:
    description:
    - The ordered set of parents that uniquely identify the section or hierarchy the
      commands should be checked against.  If the parents argument is omitted, the
      commands are checked against the set of top level or global commands.
  replace:
    choices:
    - line
    - block
    - config
    default: line
    description:
    - Instructs the module on the way to perform the configuration on the device.  If
      the replace argument is set to I(line) then the modified lines are pushed to
      the device in configuration mode.  If the replace argument is set to I(block)
      then the entire command block is pushed to the device in configuration mode
      if any line is not correct.
  running_config:
    aliases:
    - config
    description:
    - The module, by default, will connect to the remote device and retrieve the current
      running-config to use as a base for comparing against the contents of source.  There
      are times when it is not desirable to have the task get the current running-config
      for every task in a playbook.  The I(running_config) argument allows the implementer
      to pass in the configuration to use as the base config for this module.
    type: str
    version_added: '2.4'
  save_when:
    choices:
    - always
    - never
    - modified
    - changed
    default: never
    description:
    - When changes are made to the device running-configuration, the changes are not
      copied to non-volatile storage by default.  Using this argument will change
      that before.  If the argument is set to I(always), then the running-config will
      always be copied to the startup-config and the I(modified) flag will always
      be set to True.  If the argument is set to I(modified), then the running-config
      will only be copied to the startup-config if it has changed since the last save
      to startup-config.  If the argument is set to I(never), the running-config will
      never be copied to the startup-config. If the argument is set to I(changed),
      then the running-config will only be copied to the startup-config if the task
      has made a change. I(changed) was added in Ansible 2.5.
    version_added: '2.4'
  src:
    description:
    - The I(src) argument provides a path to the configuration file to load into the
      remote system.  The path can either be a full system path to the configuration
      file if the value starts with / or relative to the root of the implemented role
      or playbook. This argument is mutually exclusive with the I(lines) and I(parents)
      arguments. It can be a Jinja2 template as well. src file must have same indentation
      as a live switch config. Arista EOS device config has 3 spaces indentation.
    version_added: '2.2'
short_description: Manage Arista EOS configuration sections
version_added: '2.1'
"""

EXAMPLES = """
- name: configure top level settings
  eos_config:
    lines: hostname {{ inventory_hostname }}

- name: load an acl into the device
  eos_config:
    lines:
      - 10 permit ip host 192.0.2.1 any log
      - 20 permit ip host 192.0.2.2 any log
      - 30 permit ip host 192.0.2.3 any log
      - 40 permit ip host 192.0.2.4 any log
    parents: ip access-list test
    before: no ip access-list test
    replace: block

- name: load configuration from file
  eos_config:
    src: eos.cfg

- name: render a Jinja2 template onto an Arista switch
  eos_config:
    backup: yes
    src: eos_template.j2

- name: diff the running config against a master config
  eos_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- name: for idempotency, use full-form commands
  eos_config:
    lines:
      # - shut
      - shutdown
    # parents: int eth1
    parents: interface Ethernet1

- name: configurable backup path
  eos_config:
    src: eos_template.j2
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import re
import time
import glob

from ansible.plugins.action.eos import ActionModule as _ActionModule
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlsplit
from ansible.utils.vars import merge_hash


PRIVATE_KEYS_RE = re.compile('__.+__')


class ActionModule(_ActionModule):

    def run(self, tmp=None, task_vars=None):

        if self._task.args.get('src'):
            try:
                self._handle_template()
            except ValueError as exc:
                return dict(failed=True, msg=to_text(exc))

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if self._task.args.get('backup') and result.get('__backup__'):
            # User requested backup and no error occurred in module.
            # NOTE: If there is a parameter error, _backup key may not be in results.
            filepath = self._write_backup(task_vars['inventory_hostname'],
                                          result['__backup__'])

            result['backup_path'] = filepath

        # strip out any keys that have two leading and two trailing
        # underscore characters
        for key in list(result.keys()):
            if PRIVATE_KEYS_RE.match(key):
                del result[key]

        return result

    def _get_working_path(self):
        cwd = self._loader.get_basedir()
        if self._task._role is not None:
            cwd = self._task._role._role_path
        return cwd

    def _write_backup(self, host, contents):
        backup_path = self._get_working_path() + '/backup'
        if not os.path.exists(backup_path):
            os.mkdir(backup_path)
        for fn in glob.glob('%s/%s*' % (backup_path, host)):
            os.remove(fn)
        tstamp = time.strftime("%Y-%m-%d@%H:%M:%S", time.localtime(time.time()))
        filename = '%s/%s_config.%s' % (backup_path, host, tstamp)
        open(filename, 'w').write(contents)
        return filename

    def _handle_template(self):
        src = self._task.args.get('src')
        working_path = self._get_working_path()

        if os.path.isabs(src) or urlsplit('src').scheme:
            source = src
        else:
            source = self._loader.path_dwim_relative(working_path, 'templates', src)
            if not source:
                source = self._loader.path_dwim_relative(working_path, src)

        if not os.path.exists(source):
            raise ValueError('path specified in src not found')

        try:
            with open(source, 'r') as f:
                template_data = to_text(f.read())
        except IOError:
            return dict(failed=True, msg='unable to load src file')

        # Create a template search path in the following order:
        # [working_path, self_role_path, dependent_role_paths, dirname(source)]
        searchpath = [working_path]
        if self._task._role is not None:
            searchpath.append(self._task._role._role_path)
            if hasattr(self._task, "_block:"):
                dep_chain = self._task._block.get_dep_chain()
                if dep_chain is not None:
                    for role in dep_chain:
                        searchpath.append(role._role_path)
        searchpath.append(os.path.dirname(source))
        self._templar.environment.loader.searchpath = searchpath
