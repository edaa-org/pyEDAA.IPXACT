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

from pyIPXACT           import RootElement, __DEFAULT_SCHEMA__


class Design(RootElement):
	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description =             description
		self._componentInstances =      []
		self._interconnections =        []
		self._adHocConnections =        []

	def AddItem(self, item):
		if isinstance(item, ComponentInstance):   self._componentInstances.append(item)
		elif isinstance(item, Interconnection):   self._interconnections.append(item)
		elif isinstance(item, AdHocConnection):   self._adHocConnections.append(item)
		else:
			raise ValueError()

	def ToXml(self):
		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:design
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:{xmlns}="{schemaUri}"
				xsi:schemaLocation="{schemaUri} {schemaUrl}">
			{versionedIdentifier}
				<{xmlns}:description>{description}</{xmlns}:description>
			""").format(
				xmlns=__DEFAULT_SCHEMA__.NamespacePrefix,
				schemaUri=__DEFAULT_SCHEMA__.SchemaUri,
				schemaUrl=__DEFAULT_SCHEMA__.SchemaUrl,
				versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True),
				description=self._description
			)
		
		if self._componentInstances:
			buffer += "\t<{xmlns}:componentInstances>\n"
			for componentInstance in self._componentInstances:
				buffer += componentInstance.ToXml(2)
			buffer += "\t</{xmlns}:componentInstances>\n"
		
		if self._interconnections:
			buffer += "\t<{xmlns}:interconnections>\n"
			for interconnection in self._interconnections:
				buffer += interconnection.ToXml(2)
			buffer += "\t</{xmlns}:interconnections>\n"
		
		if self._adHocConnections:
			buffer += "\t<{xmlns}:adHocConnections>\n"
			for adHocConnection in self._adHocConnections:
				buffer += adHocConnection.ToXml(2)
			buffer += "\t</{xmlns}:adHocConnections>\n"
		
		buffer += dedent("""\
			</{xmlns}:design>
			""")
		
		return buffer.format(xmlns=__DEFAULT_SCHEMA__.NamespacePrefix)


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
		""").format(indent=_indent, xmlns=__DEFAULT_SCHEMA__.NamespacePrefix, vlnv=self._vlnv.ToXml(0), path=self._name, description=self._description)
		
		return buffer


class ComponentInstance:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class Interconnection:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""


class AdHocConnection:
	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		return ""
