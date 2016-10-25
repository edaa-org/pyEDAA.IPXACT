# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python module:      A DOM based IP-XACT implementation for Python
#
# Description:
# ------------------------------------
#   TODO:
#
# License:
# ==============================================================================
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
from textwrap           import dedent

from pyIPXACT           import RootElement, __DEFAULT_NAMESPACE__


class DesignConfiguration(RootElement):
	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description =             description
		self._generatorChainConfiguration =   None
		self._interconnectionConfiguration =  None
		self._viewConfiguration =             None
                                
	def SetItem(self, item):
		if isinstance(item,   GeneratorChainConfiguration):   self._generatorChainConfiguration =   item
		elif isinstance(item, InterconnectionConfiguration):  self._interconnectionConfiguration =  item
		elif isinstance(item, ViewConfiguration):             self._viewConfiguration =             item
		else:
			raise ValueError()

	def ToXml(self):
		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:designConfiguration
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:{xmlns}="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
				xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
														http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
			{versionedIdentifier}
				<{xmlns}:description>{description}</{xmlns}:description>
			""").format(xmlns=__DEFAULT_NAMESPACE__, versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True), description=self._description)
		
		if self._generatorChainConfiguration:
			buffer += "\t<{xmlns}:componentInstances>\n"
			buffer += self._generatorChainConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:componentInstances>\n"
		
		if self._interconnectionConfiguration:
			buffer += "\t<{xmlns}:interconnectionConfiguration>\n"
			buffer += self._interconnectionConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:interconnectionConfiguration>\n"
		
		if self._viewConfiguration:
			buffer += "\t<{xmlns}:viewConfiguration>\n"
			buffer += self._viewConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:viewConfiguration>\n"
		
		buffer += dedent("""\
			</{xmlns}:designConfiguration>
			""")
		
		return buffer.format(xmlns=__DEFAULT_NAMESPACE__)


class GeneratorChainConfiguration:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class InterconnectionConfiguration:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class ViewConfiguration:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""
