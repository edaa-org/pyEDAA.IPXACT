# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python functions:   A DOM based IP-XACT implementation for Python
#
# Description:
# ------------------------------------
#		TODO:
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

from pyIPXACT           import RootElement


class Component(RootElement):
	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description =         description
		self._busInterfaces =       []
		self._indirectInterfaces =  []
		self._channels =            []
		self._remapStates =         []
		self._addressSpaces =       []
		self._memoryMaps =          []
		self._model =               []
		self._componentGenerators = []
		self._choices =             []
		self._fileSets =            []
		self._whiteboxElements =    []
		self._cpus =                []
		self._otherClockDrivers =   []
		self._resetTypes =          []
		self._parameters =          []
		self._assertions =          []

	def ToXml(self):
		buffer = dedent("""\
			<?xml xml version="1.0" encoding="UTF-8"?>
			<ipxact:component
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
				xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
														http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
			{versionedIdentifier}
				<ipxact:description>{description}</ipxact:description>
			""").format(versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True), description=self._description)
		
		if self._busInterfaces:
			buffer += "\t<ipxact:busInterfaces>\n"
			for busInterface in self._busInterfaces:
				buffer += busInterface.ToXml(2)
			buffer += "\t</ipxact:busInterfaces>\n"
		
		if self._indirectInterfaces:
			buffer += "\t<ipxact:indirectInterfaces>\n"
			for indirectInterface in self._indirectInterfaces:
				buffer += indirectInterface.ToXml(2)
			buffer += "\t</ipxact:indirectInterfaces>\n"
		
		if self._channels:
			buffer += "\t<ipxact:channels>\n"
			for channel in self._channels:
				buffer += channel.ToXml(2)
			buffer += "\t</ipxact:channels>\n"
		
		if self._remapStates:
			buffer += "\t<ipxact:remapStates>\n"
			for remapState in self._remapStates:
				buffer += remapState.ToXml(2)
			buffer += "\t</ipxact:remapStates>\n"
		
		if self._addressSpaces:
			buffer += "\t<ipxact:addressSpaces>\n"
			for addressSpace in self._addressSpaces:
				buffer += addressSpace.ToXml(2)
			buffer += "\t</ipxact:addressSpaces>\n"
		
		if self._memoryMaps:
			buffer += "\t<ipxact:memoryMaps>\n"
			for memoryMap in self._memoryMaps:
				buffer += memoryMap.ToXml(2)
			buffer += "\t</ipxact:memoryMaps>\n"
		
		if self._model:
			buffer += "\t<ipxact:model>\n"
			buffer += self._model.ToXml(2)
			buffer += "\t</ipxact:model>\n"
		
		if self._componentGenerators:
			buffer += "\t<ipxact:componentGenerators>\n"
			for componentGenerator in self._componentGenerators:
				buffer += componentGenerator.ToXml(2)
			buffer += "\t</ipxact:componentGenerators>\n"
		
		if self._choices:
			buffer += "\t<ipxact:choices>\n"
			for choice in self._choices:
				buffer += choice.ToXml(2)
			buffer += "\t</ipxact:choices>\n"
		
		if self._fileSets:
			buffer += "\t<ipxact:fileSets>\n"
			for fileSet in self._fileSets:
				buffer += fileSet.ToXml(2)
			buffer += "\t</ipxact:fileSets>\n"
		
		if self._whiteboxElements:
			buffer += "\t<ipxact:whiteboxElements>\n"
			for whiteboxElement in self._whiteboxElements:
				buffer += whiteboxElement.ToXml(2)
			buffer += "\t</ipxact:whiteboxElements>\n"
		
		if self._cpus:
			buffer += "\t<ipxact:cpus>\n"
			for cpu in self._cpus:
				buffer += cpu.ToXml(2)
			buffer += "\t</ipxact:cpus>\n"
		
		if self._otherClockDrivers:
			buffer += "\t<ipxact:otherClockDrivers>\n"
			for otherClockDriver in self._otherClockDrivers:
				buffer += otherClockDriver.ToXml(2)
			buffer += "\t</ipxact:otherClockDrivers>\n"
		
		if self._resetTypes:
			buffer += "\t<ipxact:resetTypes>\n"
			for resetType in self._resetTypes:
				buffer += resetType.ToXml(2)
			buffer += "\t</ipxact:resetTypes>\n"
		
		if self._parameters:
			buffer += "\t<ipxact:parameters>\n"
			for parameter in self._parameters:
				buffer += parameter.ToXml(2)
			buffer += "\t</ipxact:parameters>\n"
			
		if self._assertions:
			buffer += "\t<ipxact:assertions>\n"
			for assertion in self._assertions:
				buffer += assertion.ToXml(2)
			buffer += "\t</ipxact:assertions>\n"
		
		buffer += dedent("""\
			</ipxact:component>
			""")
		
		return buffer
