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


class Component(RootElement):
	"""Represents an IP-XACT components."""

	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description =         description
		self._busInterfaces =       []
		self._indirectInterfaces =  []
		self._channels =            []
		self._remapStates =         []
		self._addressSpaces =       []
		self._memoryMaps =          []
		self._model =               None
		self._componentGenerators = []
		self._choices =             []
		self._fileSets =            []
		self._whiteboxElements =    []
		self._cpus =                []
		self._otherClockDrivers =   []
		self._resetTypes =          []
		self._parameters =          []
		self._assertions =          []

	def Settem(self, item):
		if isinstance(item, Model):                 self._model = item
		else:
			raise ValueError()

	def AddItem(self, item):
		if isinstance(item, BusInterface):          self._busInterfaces.append(item)
		elif isinstance(item, IndirectInterface):   self._indirectInterfaces.append(item)
		elif isinstance(item, Channel):             self._channels.append(item)
		elif isinstance(item, RemapState):          self._remapStates.append(item)
		elif isinstance(item, AddressSpace):        self._addressSpaces.append(item)
		elif isinstance(item, MemoryMap):           self._memoryMaps.append(item)
		elif isinstance(item, ComponentGenerator):  self._componentGenerators.append(item)
		elif isinstance(item, Choice):              self._choices.append(item)
		elif isinstance(item, FileSet):             self._fileSets.append(item)
		elif isinstance(item, WhiteboxElement):     self._whiteboxElements.append(item)
		elif isinstance(item, Cpu):                 self._cpus.append(item)
		elif isinstance(item, OtherClockDriver):    self._otherClockDrivers.append(item)
		elif isinstance(item, ResetType):           self._resetTypes.append(item)
		elif isinstance(item, Parameter):           self._parameters.append(item)
		elif isinstance(item, Assertion):           self._assertions.append(item)
		else:
			raise ValueError()
	
	def ToXml(self):
		"""Converts the object's data into XML format."""

		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:component
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
		
		if self._busInterfaces:
			buffer += "\t<{xmlns}:busInterfaces>\n"
			for busInterface in self._busInterfaces:
				buffer += busInterface.ToXml(2)
			buffer += "\t</{xmlns}:busInterfaces>\n"
	
		if self._indirectInterfaces:
			buffer += "\t<{xmlns}:indirectInterfaces>\n"
			for indirectInterface in self._indirectInterfaces:
				buffer += indirectInterface.ToXml(2)
			buffer += "\t</{xmlns}:indirectInterfaces>\n"
		
		if self._channels:
			buffer += "\t<{xmlns}:channels>\n"
			for channel in self._channels:
				buffer += channel.ToXml(2)
			buffer += "\t</{xmlns}:channels>\n"
		
		if self._remapStates:
			buffer += "\t<{xmlns}:remapStates>\n"
			for remapState in self._remapStates:
				buffer += remapState.ToXml(2)
			buffer += "\t</{xmlns}:remapStates>\n"
		
		if self._addressSpaces:
			buffer += "\t<{xmlns}:addressSpaces>\n"
			for addressSpace in self._addressSpaces:
				buffer += addressSpace.ToXml(2)
			buffer += "\t</{xmlns}:addressSpaces>\n"
		
		if self._memoryMaps:
			buffer += "\t<{xmlns}:memoryMaps>\n"
			for memoryMap in self._memoryMaps:
				buffer += memoryMap.ToXml(2)
			buffer += "\t</{xmlns}:memoryMaps>\n"
		
		if self._model:
			buffer += "\t<{xmlns}:model>\n"
			buffer += self._model.ToXml(2)
			buffer += "\t</{xmlns}:model>\n"
		
		if self._componentGenerators:
			buffer += "\t<{xmlns}:componentGenerators>\n"
			for componentGenerator in self._componentGenerators:
				buffer += componentGenerator.ToXml(2)
			buffer += "\t</{xmlns}:componentGenerators>\n"
		
		if self._choices:
			buffer += "\t<{xmlns}:choices>\n"
			for choice in self._choices:
				buffer += choice.ToXml(2)
			buffer += "\t</{xmlns}:choices>\n"
		
		if self._fileSets:
			buffer += "\t<{xmlns}:fileSets>\n"
			for fileSet in self._fileSets:
				buffer += fileSet.ToXml(2)
			buffer += "\t</{xmlns}:fileSets>\n"
		
		if self._whiteboxElements:
			buffer += "\t<{xmlns}:whiteboxElements>\n"
			for whiteboxElement in self._whiteboxElements:
				buffer += whiteboxElement.ToXml(2)
			buffer += "\t</{xmlns}:whiteboxElements>\n"
		
		if self._cpus:
			buffer += "\t<{xmlns}:cpus>\n"
			for cpu in self._cpus:
				buffer += cpu.ToXml(2)
			buffer += "\t</{xmlns}:cpus>\n"
		
		if self._otherClockDrivers:
			buffer += "\t<{xmlns}:otherClockDrivers>\n"
			for otherClockDriver in self._otherClockDrivers:
				buffer += otherClockDriver.ToXml(2)
			buffer += "\t</{xmlns}:otherClockDrivers>\n"
		
		if self._resetTypes:
			buffer += "\t<{xmlns}:resetTypes>\n"
			for resetType in self._resetTypes:
				buffer += resetType.ToXml(2)
			buffer += "\t</{xmlns}:resetTypes>\n"
		
		if self._parameters:
			buffer += "\t<{xmlns}:parameters>\n"
			for parameter in self._parameters:
				buffer += parameter.ToXml(2)
			buffer += "\t</{xmlns}:parameters>\n"
		
		if self._assertions:
			buffer += "\t<{xmlns}:assertions>\n"
			for assertion in self._assertions:
				buffer += assertion.ToXml(2)
			buffer += "\t</{xmlns}:assertions>\n"
		
		buffer += dedent("""\
				</{xmlns}:component>
				""")
		
		return buffer.format(xmlns=__DEFAULT_SCHEMA__.NamespacePrefix)


class BusInterface:
	"""Represents an IP-XACT bus interface."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""

class IndirectInterface:
	"""Represents an IP-XACT indirect interface."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Channel:
	"""Represents an IP-XACT channel."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class RemapState:
	"""Represents an IP-XACT remap state."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class AddressSpace:
	"""Represents an IP-XACT address space."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class MemoryMap:
	"""Represents an IP-XACT memory map."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Model:
	"""Represents an IP-XACT model."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class ComponentGenerator:
	"""Represents an IP-XACT component generator."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Choice:
	"""Represents an IP-XACT choice."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class FileSet:
	"""Represents an IP-XACT fileset."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class WhiteboxElement:
	"""Represents an IP-XACT whitebos element."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Cpu:
	"""Represents an IP-XACT cpu."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class OtherClockDriver:
	"""Represents an IP-XACT *other* clock driver."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class ResetType:
	"""Represents an IP-XACT reset type."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Parameter:
	"""Represents an IP-XACT parameter."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Assertion:
	"""Represents an IP-XACT assertion."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""
