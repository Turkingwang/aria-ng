#
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from aria import dsl_specification
from aria.presentation import Presentation, AsIsPresentation, has_fields, primitive_field, object_field 
from clint.textui import puts

class Description(AsIsPresentation):
    def _dump(self, context):
        puts(context.style.meta(self.value))

@has_fields
@dsl_specification('outputs', 'cloudify-1.0')
@dsl_specification('outputs', 'cloudify-1.1')
@dsl_specification('outputs', 'cloudify-1.2')
@dsl_specification('outputs', 'cloudify-1.3')
class Output(Presentation):
    """
    :code:`outputs` provide a way of exposing global aspects of a deployment. When deployed, a blueprint can expose specific outputs of that deployment - for instance, an endpoint of a server or any other runtime or static information of a specific resource.
    
    See the `Cloudify DSL v1.3 specification <http://docs.getcloudify.org/3.4.0/blueprints/spec-outputs/>`__.
    """
    
    @object_field(Description)
    def description(self):
        """
        An optional description for the output.
        
        :rtype: :class:`Description`
        """

    @primitive_field(required=True)
    def value(self):
        """
        The output value. Can be anything from a simple value (e.g. port) to a complex value (e.g. hash with values). Output values can contain hardcoded values, inputs, properties and attributes.
        """

@has_fields
@dsl_specification('plugins', 'cloudify-1.0')
@dsl_specification('plugins', 'cloudify-1.1')
@dsl_specification('plugins', 'cloudify-1.2')
@dsl_specification('plugins', 'cloudify-1.3')
class Plugin(Presentation):
    """
    By declaring :code:`plugins` we can install python modules and use the installed or preinstalled modules to perform different operations. We can also decide where a specific plugin's operations will be executed.
    
    See the `Cloudify DSL v1.3 specification <http://docs.getcloudify.org/3.4.0/blueprints/spec-plugins/>`__.
    """

    @primitive_field(str, required=True, allowed=('central_deployment_agent', 'host_agent'))
    def executor(self):
        """
        Where to execute the plugin's operations. Valid Values: :code:`central_deployment_agent`, :code:`host_agent`.
        
        :rtype: str
        """

    @primitive_field(str)
    def source(self):
        """
        Where to retrieve the plugin from. Could be either a path relative to the plugins dir inside the blueprint's root dir or a url. If install is false, source is redundant. If install is true, source (or package_name) is mandatory.
        
        :rtype: str
        """

    @primitive_field(str)
    def install_arguments(self):
        """
        Optional arguments passed to the :code:`pip install` command created for the plugin installation.
        
        :rtype: str        
        """

    @primitive_field(bool, default=True)
    def install(self):
        """
        Whether to install the plugin or not as it might already be installed as part of the agent. Defaults to true. (Supported since: :code:`cloudify_dsl_1_1`)
        
        :rtype: bool
        """

    @primitive_field(str)
    def package_name(self):
        """
        Managed plugin package name. (Supported since: :code:`cloudify_dsl_1_2`) If install is false, pacakge_name is redundant. If install is true, package_name (or source) is mandatory.
        
        :rtype: str
        """

    @primitive_field(str)
    def package_version(self):
        """
        Managed plugin package version. (Supported since: :code:`cloudify_dsl_1_2`)
        
        :rtype: :class:`Version`
        """

    @primitive_field(str)
    def supported_platform(self):
        """
        Managed plugin supported platform (e.g. :code:`linux_x86_64`). (Supported since: :code:`cloudify_dsl_1_2`)
        
        :rtype: str
        """

    @primitive_field(str)
    def distribution(self):
        """
        Managed plugin distribution. (Supported since: :code:`cloudify_dsl_1_2`)
        
        :rtype: str
        """

    @primitive_field(str)
    def distribution_version(self):
        """
        Managed plugin distribution version. (Supported since: :code:`cloudify_dsl_1_2`)
        
        :rtype: :class:`Version`
        """

    @primitive_field(str)
    def distribution_release(self):
        """
        Managed plugin distribution release. (Supported since: :code:`cloudify_dsl_1_2`)
        
        :rtype: str
        """