# ==================================================================================================================== #
#              _____ ____    _        _      ___ ______  __    _    ____ _____                                         #
#  _ __  _   _| ____|  _ \  / \      / \    |_ _|  _ \ \/ /   / \  / ___|_   _|                                        #
# | '_ \| | | |  _| | | | |/ _ \    / _ \    | || |_) \  /   / _ \| |     | |                                          #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ _ | ||  __//  \  / ___ \ |___  | |                                          #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)___|_|  /_/\_\/_/   \_\____| |_|                                          #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2025 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2016-2016 Patrick Lehmann - Dresden, Germany                                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
from pathlib              import Path
from sys                  import version_info
from textwrap             import dedent
from typing import List, Optional as Nullable, ClassVar, Dict, Union

from lxml.etree           import _Element, QName, _Comment
from pyTooling.Decorators import export, readonly
from pyTooling.Common     import getFullyQualifiedName

from pyEDAA.IPXACT        import __DEFAULT_SCHEMA__, RootElement, VLNV, IPXACTSchema, Element, IPXACTException


@export
class BusInterface(Element):
	"""Represents an IP-XACT bus interface."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	@classmethod
	def FromXml(cls, element: _Element) -> "BusInterface":
		pass

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class IndirectInterface(Element):
	"""Represents an IP-XACT indirect interface."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Channel(Element):
	"""Represents an IP-XACT channel."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class RemapState(Element):
	"""Represents an IP-XACT remap state."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class AddressSpace(Element):
	"""Represents an IP-XACT address space."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class MemoryMap(Element):
	"""Represents an IP-XACT memory map."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Model(Element):
	"""Represents an IP-XACT model."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class ComponentGenerator:
	"""Represents an IP-XACT component generator."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Choice(Element):
	"""Represents an IP-XACT choice."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class File(Element):
	_path: Path

	def __init__(self, path: Path) -> None:
		self._path = Path

	@readonly
	def Path(self) -> Path:
		return self._path

	@classmethod
	def FromXml(cls, fileElement: _Element) -> "FileSet":
		fileName = None
		fileType = None
		for element in fileElement:
			if isinstance(element, _Comment):
				continue

			elementLocalname = QName(element).localname
			if elementLocalname == "name":
				fileName = element.text
			elif elementLocalname == "fileType":
				fileType = element.text
			elif elementLocalname == "isStructural":
				pass
			else:
				raise IPXACTException(f"Unsupported tag '{elementLocalname}' at component → fileSets → fileSet → file.")

		return cls(Path(fileName))

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""

	def __str__(self) -> str:
		return str(self._path)


@export
class FileSet(Element):
	"""Represents an IP-XACT fileset."""

	_name: str
	_files: List[File]

	def __init__(self, name: str, files: List[File]) -> None:
		self._name =  name
		self._files = [file for file in files]

	@readonly
	def Name(self) -> str:
		return self._name

	@readonly
	def Files(self) -> List[File]:
		return self._files

	@readonly
	def FileCount(self) -> int:
		return len(self._files)

	@classmethod
	def FromXml(cls, fileSetElement: _Element) -> "FileSet":
		files = []
		fileSetName = None
		for element in fileSetElement:
			if isinstance(element, _Comment):
				continue

			elementLocalname = QName(element).localname
			if elementLocalname == "name":
				fileSetName = element.text
			elif elementLocalname == "file":
				files.append(File.FromXml(element))
			else:
				raise IPXACTException(f"Unsupported tag '{elementLocalname}' at component → fileSets → fileSet.")

		return cls(fileSetName, files)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""

	def __str__(self) -> str:
		return f"FileSet {self._name} ({len(self._files)})"


@export
class WhiteboxElement(Element):
	"""Represents an IP-XACT whitebos element."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Cpu(Element):
	"""Represents an IP-XACT cpu."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class OtherClockDriver(Element):
	"""Represents an IP-XACT *other* clock driver."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class ResetType(Element):
	"""Represents an IP-XACT reset type."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Parameter(Element):
	"""Represents an IP-XACT parameter.""""""Represents an IP-XACT assertion."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Assertion(Element):
	"""Represents an IP-XACT assertion."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class Component(RootElement):
	"""Represents an IP-XACT components."""

	_rootTagName:         ClassVar[str] = "component"

	_busInterfaces:       List
	_indirectInterfaces:  List
	_channels:            List
	_remapStates:         List
	_addressSpaces:       List
	_memoryMaps:          List
	_model:               Nullable[Model]
	_componentGenerators: List
	_choices:             List
	_fileSets:            Dict[str, FileSet]
	_whiteboxElements:    List
	_cpus:                List
	_otherClockDrivers:   List
	_resetTypes:          List
	_parameters:          List
	_assertions:          List

	def __init__(
		self,
		componentFile: Nullable[Path] = None,
		parse: bool = False,
		vlnv: Nullable[VLNV] = None,
		description: Nullable[str] = None
	):
		self._busInterfaces = []
		self._indirectInterfaces = []
		self._channels = []
		self._remapStates = []
		self._addressSpaces = []
		self._memoryMaps = []
		self._model = None
		self._componentGenerators = []
		self._choices = []
		self._fileSets = {}
		self._whiteboxElements = []
		self._cpus = []
		self._otherClockDrivers = []
		self._resetTypes = []
		self._parameters = []
		self._assertions = []

		super().__init__(componentFile, parse, vlnv, description)

	@readonly
	def FileSets(self) -> Dict[str, FileSet]:
		return self._fileSets

	def Parse(self, element: _Element) -> None:
		elementLocalname = QName(element).localname
		if elementLocalname == "busInterfaces":
			pass
		# for busInterfaceElement in element:
		# 	self.AddItem(BusInterface.FromXml(busInterfaceElement))
		elif elementLocalname == "indirectInterfaces":
			pass
		elif elementLocalname == "channels":
			pass
		elif elementLocalname == "remapStates":
			pass
		elif elementLocalname == "addressSpaces":
			pass
		elif elementLocalname == "memoryMaps":
			pass
		elif elementLocalname == "model":
			pass
		elif elementLocalname == "componentGenerators":
			pass
		elif elementLocalname == "choices":
			pass
		elif elementLocalname == "fileSets":
			for fileSetElement in element:
				if isinstance(fileSetElement, _Comment):
					continue

				self.AddFileSet(FileSet.FromXml(fileSetElement))
		elif elementLocalname == "whiteboxElements":
			pass
		elif elementLocalname == "cpus":
			pass
		elif elementLocalname == "otherClockDrivers":
			pass
		elif elementLocalname == "resetTypes":
			pass
		elif elementLocalname == "parameters":
			pass
		elif elementLocalname == "assertions":
			pass
		else:
			raise IPXACTException(f"Unsupported tag '{elementLocalname}' at root-level.")

	def SetItem(self, item):
		if isinstance(item, Model):
			self._model = item
		else:
			raise ValueError()

	def AddItem(self, item) -> None:
		if isinstance(item, BusInterface):
			self._busInterfaces.append(item)
		elif isinstance(item, IndirectInterface):
			self._indirectInterfaces.append(item)
		elif isinstance(item, Channel):
			self._channels.append(item)
		elif isinstance(item, RemapState):
			self._remapStates.append(item)
		elif isinstance(item, AddressSpace):
			self._addressSpaces.append(item)
		elif isinstance(item, MemoryMap):
			self._memoryMaps.append(item)
		elif isinstance(item, ComponentGenerator):
			self._componentGenerators.append(item)
		elif isinstance(item, Choice):
			self._choices.append(item)
		elif isinstance(item, FileSet):
			self.AddFileSet(item)
		elif isinstance(item, WhiteboxElement):
			self._whiteboxElements.append(item)
		elif isinstance(item, Cpu):
			self._cpus.append(item)
		elif isinstance(item, OtherClockDriver):
			self._otherClockDrivers.append(item)
		elif isinstance(item, ResetType):
			self._resetTypes.append(item)
		elif isinstance(item, Parameter):
			self._parameters.append(item)
		elif isinstance(item, Assertion):
			self._assertions.append(item)
		else:
			ex = TypeError("Parameter 'item' is not a BusInterface, IndirectInterface, Channel, RemapState, AddressSpace, MemoryMap, ComponentGenerator, Choice, FileSet, WhiteboxElement, Cpu, OtherClockDriver, ResetType, Parameter, or Assertion.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(item)}'.")
			raise ex

	def AddFileSet(self, fileset: FileSet):
		if not isinstance(fileset, FileSet):
			ex = TypeError("Parameter 'fileset' is not a FileSet.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(fileset)}'.")
			raise ex

		if fileset._name in self._fileSets:
			raise ValueError(f"Duplicate fileset '{fileset._name}'.")

		self._fileSets[fileset._name] = fileset

	def ToXml(self, schema: IPXACTSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		xmlns = schema.NamespacePrefix
		buffer = dedent(f"""\
			<?xml version="1.0" encoding="UTF-8" ?>
			<{xmlns}:component
			\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			\txmlns:{xmlns}="{schema.SchemaUri}"
			\txsi:schemaLocation="{schema.SchemaUri} {schema.SchemaUrl}">
			{self._vlnv.ToXml(schema, isVersionedIdentifier=True)}
			\t<{xmlns}:description>{self._description}</{xmlns}:description>
			""")

		if self._busInterfaces:
			buffer += f"\t<{xmlns}:busInterfaces>\n"
			for busInterface in self._busInterfaces:
				buffer += busInterface.ToXml(2, schema)
			buffer += f"\t</{xmlns}:busInterfaces>\n"

		if self._indirectInterfaces:
			buffer += f"\t<{xmlns}:indirectInterfaces>\n"
			for indirectInterface in self._indirectInterfaces:
				buffer += indirectInterface.ToXml(2, schema)
			buffer += f"\t</{xmlns}:indirectInterfaces>\n"

		if self._channels:
			buffer += f"\t<{xmlns}:channels>\n"
			for channel in self._channels:
				buffer += channel.ToXml(2, schema)
			buffer += f"\t</{xmlns}:channels>\n"

		if self._remapStates:
			buffer += f"\t<{xmlns}:remapStates>\n"
			for remapState in self._remapStates:
				buffer += remapState.ToXml(2, schema)
			buffer += f"\t</{xmlns}:remapStates>\n"

		if self._addressSpaces:
			buffer += f"\t<{xmlns}:addressSpaces>\n"
			for addressSpace in self._addressSpaces:
				buffer += addressSpace.ToXml(2, schema)
			buffer += f"\t</{xmlns}:addressSpaces>\n"

		if self._memoryMaps:
			buffer += f"\t<{xmlns}:memoryMaps>\n"
			for memoryMap in self._memoryMaps:
				buffer += memoryMap.ToXml(2, schema)
			buffer += f"\t</{xmlns}:memoryMaps>\n"

		if self._model:
			buffer += f"\t<{xmlns}:model>\n"
			buffer += self._model.ToXml(2, schema)
			buffer += f"\t</{xmlns}:model>\n"

		if self._componentGenerators:
			buffer += f"\t<{xmlns}:componentGenerators>\n"
			for componentGenerator in self._componentGenerators:
				buffer += componentGenerator.ToXml(2, schema)
			buffer += f"\t</{xmlns}:componentGenerators>\n"

		if self._choices:
			buffer += f"\t<{xmlns}:choices>\n"
			for choice in self._choices:
				buffer += choice.ToXml(2, schema)
			buffer += f"\t</{xmlns}:choices>\n"

		if self._fileSets:
			buffer += f"\t<{xmlns}:fileSets>\n"
			for fileSet in self._fileSets:
				buffer += fileSet.ToXml(2, schema)
			buffer += f"\t</{xmlns}:fileSets>\n"

		if self._whiteboxElements:
			buffer += f"\t<{xmlns}:whiteboxElements>\n"
			for whiteboxElement in self._whiteboxElements:
				buffer += whiteboxElement.ToXml(2, schema)
			buffer += f"\t</{xmlns}:whiteboxElements>\n"

		if self._cpus:
			buffer += f"\t<{xmlns}:cpus>\n"
			for cpu in self._cpus:
				buffer += cpu.ToXml(2, schema)
			buffer += f"\t</{xmlns}:cpus>\n"

		if self._otherClockDrivers:
			buffer += f"\t<{xmlns}:otherClockDrivers>\n"
			for otherClockDriver in self._otherClockDrivers:
				buffer += otherClockDriver.ToXml(2, schema)
			buffer += f"\t</{xmlns}:otherClockDrivers>\n"

		if self._resetTypes:
			buffer += f"\t<{xmlns}:resetTypes>\n"
			for resetType in self._resetTypes:
				buffer += resetType.ToXml(2, schema)
			buffer += f"\t</{xmlns}:resetTypes>\n"

		if self._parameters:
			buffer += f"\t<{xmlns}:parameters>\n"
			for parameter in self._parameters:
				buffer += parameter.ToXml(2, schema)
			buffer += f"\t</{xmlns}:parameters>\n"

		if self._assertions:
			buffer += f"\t<{xmlns}:assertions>\n"
			for assertion in self._assertions:
				buffer += assertion.ToXml(2, schema)
			buffer += f"\t</{xmlns}:assertions>\n"

		buffer += dedent(f"""\
				</{xmlns}:component>
				""")

		return buffer
