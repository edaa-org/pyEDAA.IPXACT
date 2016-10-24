# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python functions:   A DOM based IP-XACT implementation for Python
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
from pyIPXACT.Component import Component


class Catalog(RootElement):
	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description = description
		self._abstractionDefinitions =  []
		self._abstractors =             []
		self._busInterfaces =           []
		self._catalogs =                []
		self._components =              []
		self._designConfigurations =    []
		self._designs =                 []
		self._generatorChains =         []
	                                  
	def AddCatalogItem(self, item):
		if isinstance(item, IpxactFile):
			self._catalogs.append(item)
		elif isinstance(item, Component):
			self._components.append(item)
		else:
			raise ValueError()

	def ToXml(self):
		buffer = dedent("""\
			<?xml xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:catalog
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:{xmlns}="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
				xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
														http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
			{versionedIdentifier}
				<{xmlns}:description>{description}</{xmlns}:description>
			""").format(xmlns=__DEFAULT_NAMESPACE__, versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True), description=self._description)
		
		if self._catalogs:
			buffer += "\t<{xmlns}:catalogs>\n"
			for ipxactFile in self._catalogs:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</{xmlns}:catalogs>\n"
		
		if self._components:
			buffer += "\t<{xmlns}:components>\n"
			for ipxactFile in self._components:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</{xmlns}:components>\n"
		
		buffer += dedent("""\
			</{xmlns}:catalog>
			""")
		
		return buffer.format(xmlns=__DEFAULT_NAMESPACE__)


class IpxactFile:
	def __init__(self, vlnv, name, description):
		self._vlnv = vlnv
		self._name = name
		self._description = description
	
	def ToXml(self, indent):
		_indent = "\t" * indent
		buffer = dedent("""\
			{indent}<{xmlns}:ipxactFile>
			{indent}	{vlnv}
			{indent}	<{xmlns}:name>{path}</{xmlns}:name>
			{indent}	<{xmlns}:description>{description}</{xmlns}:description>
			{indent}</{xmlns}:ipxactFile>
		""").format(indent=_indent, xmlns=__DEFAULT_NAMESPACE__, vlnv=self._vlnv.ToXml(0), path=self._name, description=self._description)
		
		return buffer
