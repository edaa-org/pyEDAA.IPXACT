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


class GeneratorChain(RootElement):
	def __init__(self, vlnv, displayName, description, chainGroup):
		super().__init__(vlnv)
		
		self._displayName =                   displayName
		self._description =                   description
		self._chainGroup =                    chainGroup
		self._generatorChainSelector =        None
		self._interconnectionConfiguration =  None
		self._generator =                     None
                                
	def SetItem(self, item):
		if isinstance(item,   GeneratorChainSelector):      self._generatorChainSelector =      item
		elif isinstance(item, ComponentGeneratorSelector):  self._componentGeneratorSelector =  item
		elif isinstance(item, Generator):                   self._generator =                   item
		else:
			raise ValueError()

	def ToXml(self):
		buffer = dedent("""\
			<?xml xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:generatorChain
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:{xmlns}="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
				xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
														http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
			{versionedIdentifier}
				<{xmlns}:displayName>{displayName}</{xmlns}:displayName>
				<{xmlns}:description>{description}</{xmlns}:description>
				<{xmlns}:chainGroup>{chainGroup}</{xmlns}:chainGroup>
			""").format(xmlns=__DEFAULT_NAMESPACE__, versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True), displayName=self._displayName, description=self._description, chainGroup=self._chainGroup)
		
		if self._generatorChainSelector:
			buffer += "\t<{xmlns}:generatorChainSelector>\n"
			buffer += self._generatorChainSelector.ToXml(2)
			buffer += "\t</{xmlns}:generatorChainSelector>\n"
		
		if self._componentGeneratorSelector:
			buffer += "\t<{xmlns}:componentGeneratorSelector>\n"
			buffer += self._componentGeneratorSelector.ToXml(2)
			buffer += "\t</{xmlns}:componentGeneratorSelector>\n"
		
		if self._generator:
			buffer += "\t<{xmlns}:generator>\n"
			buffer += self._generator.ToXml(2)
			buffer += "\t</{xmlns}:generator>\n"
		
		buffer += dedent("""\
			</{xmlns}:generatorChain>
			""")
		
		return buffer.format(xmlns=__DEFAULT_NAMESPACE__)


class GeneratorChainSelector:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class ComponentGeneratorSelector:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class Generator:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


