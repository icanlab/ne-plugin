#!/usr/bin/env python
# -*- coding: utf-8 -*-
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




import sys
from collections import OrderedDict
from ansible.module_utils.network.ne.common_module.ne_base import ConfigBase,GetBase, InputBase
from ansible.module_utils.network.ne.ne import get_nc_config, set_nc_config, ne_argument_spec

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

EXAMPLE = """
---
- name: ietf_network_instance_schema_mount
  hosts: ne_test
  connection: netconf
  gather_facts: no
  vars:
    netconf:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ ansible_user }}"
      password: "{{ ansible_ssh_pass }}"
      transport: netconf

  tasks:

  - name: ietf-network-instance-schema_mount_full
    ietf_network_instance_schema_mount:
      operation_type: config
      network-instances: 
        - network-instance: 
            name: "vrf-red"
            vrf-root: 
              routing: 
                control-plane-protocols: 
                  control-plane-protocol: 
                    ospf: 
                      areas: 
                        area: 
                          interfaces: 
      provider: "{{ netconf }}"


"""
DOCUMENTATION = """
None
"""



xml_head = """<config>"""

xml_tail = """</config>"""

# Keyword list
key_list = ['/network-instances/network-instance/name']

namespaces = [{'/network-instances': ['', '@xmlns="urn:ietf:params:xml:ns:yang:ietf-network-instance"', '/network-instances']}, {'/network-instances/network-instance': ['', '', '/network-instances/network-instance']}, {'/network-instances/network-instance/name': ['vrf-red', '', '/network-instances/network-instance/name']}, {'/network-instances/network-instance/vrf-root': ['', '', '/network-instances/network-instance/vrf-root']}, {'/network-instances/network-instance/vrf-root/routing': ['', '@xmlns="urn:ietf:params:xml:ns:yang:ietf-routing"', '/network-instances/network-instance/vrf-root/routing']}, {'/network-instances/network-instance/vrf-root/routing/router-id': ['192.0.2.1', '', '/network-instances/network-instance/vrf-root/routing/router-id']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/type': ['ospf', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/type']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/name': ['1', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/name']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf': ['', '@xmlns="urn:ietf:params:xml:ns:yang:ietf-ospf"', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/address_family': ['ipv4', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/address_family']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/area-id': ['203.0.113.1', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/area-id']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface': ['', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface/name': ['eth1', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface/name']}, {'/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface/cost': ['10', '', '/network-instances/network-instance/vrf-root/routing/control-plane-protocols/control-plane-protocol/ospf/areas/area/interfaces/interface/cost']}]

business_tag = ['network-instances']

# Passed to the ansible parameter
argument_spec = OrderedDict([('network-instances', {'elements': 'dict', 'type': 'list', 'options': OrderedDict([('network-instance', {'type': 'dict', 'options': OrderedDict([('name', {'type': 'str', 'required': False}), ('vrf-root', {'type': 'dict', 'options': OrderedDict([('routing', {'type': 'dict', 'options': OrderedDict([('control-plane-protocols', {'type': 'dict', 'options': OrderedDict([('control-plane-protocol', {'type': 'dict', 'options': OrderedDict([('ospf', {'type': 'dict', 'options': OrderedDict([('areas', {'type': 'dict', 'options': OrderedDict([('area', {'type': 'dict', 'options': OrderedDict([('interfaces', {'type': 'dict', 'options': OrderedDict()})])})])})])})])})])})])})])})])})])})])

# Operation type
operation_dict = {'operation_type':{'type': 'str', 'required':True, 'choices': ['config','get','get-config','rpc']},
                  'operation_specs': {
                      'elements': 'dict', 'type': 'list','options': {
                          'path': {
                              'type': 'str'}, 'operation': {
                              'choices': ['merge', 'replace', 'create', 'delete', 'remove'],'default':'merge'}}}}

# Parameters passed to check params
leaf_info =  OrderedDict([('network-instances', OrderedDict([('network-instance', OrderedDict([('name', {
                'length': [], 
                'type': 'string', 'key': True, 'default': None, 'required': False, 
                'pattern': []}), 
            ('vrf-root', OrderedDict([('routing', OrderedDict([('control-plane-protocols', OrderedDict([('control-plane-protocol', OrderedDict([('ospf', OrderedDict([('areas', OrderedDict([('area', OrderedDict([('interfaces', OrderedDict([('interface', OrderedDict())]))]))]))]))]))]))]))]))]))]))])


# User check params
class UserCheck(object):
    def __init__(self, params, infos):
        #  user configuration get from AnsibleModule().params
        self.params = params
        # leaf infos from yang files
        self.infos = infos

    # user defined check method need startswith "check_"
    # return 0 if not pass check logic, else 1
    def check_leaf_restrict(self):
        """
            if leaf_1 configured, leaf2 shouble be configured
            and range shouble be in [10, 20]
        """
        return 1   


# Call the ConfigBase base class
def config_base(config_args):
    class_object = ConfigBase(*config_args)
    class_object.run()


# Call the GetBase base class
def get_base(get_args):
    class_object = GetBase(*get_args)
    class_object.run()

def input_base(input_args):
    class_object = InputBase(*input_args)
    class_object.run()


# According to the type of message
def operation(operation_type,args):
    if operation_type == 'config':
        config_base(args)
    elif operation_type == 'get' or operation_type == 'get-config':
        get_base(args)
    else:
        input_base(args)


def filter_check(user_check_obj):
    return (list(
        filter(lambda m: m.startswith("check_"), [i + '()' for i in dir(user_check_obj)])))


def main():
    """Module main"""
    argument_spec.update(ne_argument_spec)
    argument_spec.update(operation_dict)
    args = (argument_spec, leaf_info, namespaces, business_tag, xml_head,xml_tail,key_list)
    module_params = ConfigBase(*args).get_operation_type()
    for check_func in filter_check(UserCheck):
        if not eval('UserCheck(module_params, leaf_info).' + check_func):
            ConfigBase(*args).init_module().fail_json(msg='UserCheck.'+ check_func)
    operation(module_params['operation_type'], args)


if __name__ == '__main__':
    main()