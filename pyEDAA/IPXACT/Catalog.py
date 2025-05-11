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
from pathlib  import Path
from sys      import version_info
from textwrap import dedent
from typing   import List, Dict

from lxml.etree              import XMLParser, XML, XMLSchema, ElementTree, QName

from pyTooling.Decorators    import export, readonly
from pyTooling.Common        import getFullyQualifiedName

from pyEDAA.IPXACT           import RootElement, VLNV, IPXACTException, __URI_MAP__, __DEFAULT_SCHEMA__, IPXACTSchema, Element
from pyEDAA.IPXACT.Component import Component


@export
class IpxactFile(Element):
	"""Represents a IP-XACT file."""

	_name:        str    #: Name
	_description: str    #: Description

	def __init__(self, vlnv: VLNV, name: str, description: str):
		"""
		Instantiates an ipxactFile structure.

		:param vlnv:        A Vendor-Library-Name-Version unique identified.
		:param name:        Name of the IP-XACT file.
		:param description: A description text.
		:raises TypeError:  If parameter vlnv is not a VLNV.
		:raises TypeError:  If parameter name is not a string.
		:raises ValueError: If parameter name is empty.
		:raises TypeError:  If parameter description is not a string.
		:raises ValueError: If parameter description is empty.
		"""
		super().__init__(vlnv)

		if not isinstance(name, str):
			ex = TypeError(f"Parameter 'name' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(name)}'.")
			raise ex
		elif name == "":
			raise ValueError(f"Parameter 'name' is empty.")

		if not isinstance(description, str):
			ex = TypeError(f"Parameter 'description' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(description)}'.")
			raise ex
		elif description == "":
			raise ValueError(f"Parameter 'description' is empty.")

		self._vlnv = vlnv
		self._name = name
		self._description = description

	@classmethod
	def FromXml(cls, ipxactFileElement):
		"""Constructs an instance of ``IpxactFile`` from an lxml element."""

		elementTag = QName(ipxactFileElement.tag)
		if elementTag.localname != "ipxactFile":
			raise IPXACTException("Expected tag 'ipxactFile'.")

		vlnv = None
		name = None
		description = None
		for subElement in ipxactFileElement:
			element = QName(subElement)
			if element.localname == "vlnv":
				vendor =  subElement.get("vendor")
				library = subElement.get("library")
				name2 =   subElement.get("name")
				version = subElement.get("version")

				vlnv = VLNV(vendor, library, name2, version)
			elif element.localname == "name":
				name = subElement.text
			elif element.localname == "description":
				description = subElement.text
			else:
				raise IPXACTException(f"Unsupported tag '{ipxactFileElement.localname}' in node 'ipxactFile'.")

		ipxactFile = cls(vlnv, name, description)
		return ipxactFile

	def ToXml(self, indent: int = 0, schema: IPXACTSchema = __DEFAULT_SCHEMA__):
		"""Converts the object's data into XML format."""
		# WORKAROUND:
		#   Python <=3.11:
		#   {'\t' * indent} is not supported by Python before 3.12 due to a backslash within {...}
		indent = "\t" * indent
		xmlns = schema.NamespacePrefix
		return dedent(f"""\
			{indent}<{xmlns}:ipxactFile>
			{indent}\t{self._vlnv.ToXml(0, schema)}
			{indent}\t<{xmlns}:name>{self._name}</{xmlns}:name>
			{indent}\t<{xmlns}:description>{self._description}</{xmlns}:description>
			{indent}</{xmlns}:ipxactFile>
		""")


@export
class Catalog(RootElement):
	"""Represents an IP-XACT catalog."""

	_description:            str
	_abstractionDefinitions: List
	_abstractors:            List
	_busInterfaces:          List
	_catalogs:               Dict[VLNV, IpxactFile]
	_components:             List
	_designConfigurations:   List
	_designs:                List
	_generatorChains:        List

	def __init__(self, vlnv: VLNV, description: str):
		super().__init__(vlnv)

		self._description =             description
		self._abstractionDefinitions =  []
		self._abstractors =             []
		self._busInterfaces =           []
		self._catalogs =                {}
		self._components =              []
		self._designConfigurations =    []
		self._designs =                 []
		self._generatorChains =         []

	@classmethod
	def FromFile(cls, filePath : Path):
		"""Constructs an instance of ``Catalog`` from a file."""

		if not filePath.exists():
			raise IPXACTException(f"IPXACT file '{filePath}' not found.") from FileNotFoundError(str(filePath))

		try:
			with filePath.open("rb") as fileHandle:
				content = fileHandle.read()
		except OSError as ex:
			raise IPXACTException(f"Couldn't open '{filePath}'.") from ex

		xmlParser = XMLParser(remove_blank_text=True, encoding="utf-8")
		root =      XML(content, parser=xmlParser, base_url=filePath.resolve().as_uri())  # - relative paths are not supported
		rootTag =   QName(root.tag)

		if rootTag.localname != "catalog":
			raise IPXACTException("The input IP-XACT file is not a catalog file.")

		namespacePrefix = root.prefix
		namespaceURI = root.nsmap[namespacePrefix]
		if namespaceURI in __URI_MAP__:
			ipxactSchema = __URI_MAP__[namespaceURI]
		else:
			raise IPXACTException(f"The input IP-XACT file uses an unsupported namespace: '{namespaceURI}'.")

		try:
			with ipxactSchema.LocalPath.open("rb") as fileHandle:
				schema = fileHandle.read()
		except OSError as ex:
			raise IPXACTException(f"Couldn't open IP-XACT schema '{ipxactSchema.LocalPath}' for {namespacePrefix} ({namespaceURI}).") from ex

		schemaRoot = XML(schema, parser=xmlParser, base_url=ipxactSchema.LocalPath.as_uri())
		schemaTree =  ElementTree(schemaRoot)
		xmlSchema =   XMLSchema(schemaTree)

		try:
			xmlSchema.assertValid(root)
		except Exception as ex:
			raise IPXACTException("The input IP-XACT file is not valid.") from ex

		items = []
		for rootElements in root:
			element = QName(rootElements)
			if element.localname == "vendor":
				vendor = rootElements.text
			elif element.localname == "library":
				library = rootElements.text
			elif element.localname == "name":
				name = rootElements.text
			elif element.localname == "version":
				version = rootElements.text
			elif element.localname == "description":
				description = rootElements.text
			elif element.localname == "catalogs":
				for ipxactFileElement in rootElements:
					items.append(IpxactFile.FromXml(ipxactFileElement))
			else:
				raise IPXACTException(f"Unsupported tag '{element.localname}' at root-level.")

		vlnv = VLNV(vendor=vendor, library=library, name=name, version=version)
		catalog = cls(vlnv, description=description)
		for item in items:
			catalog.AddItem(item)

		return catalog

	def AddItem(self, item) -> None:
		if isinstance(item, IpxactFile):
			self._catalogs[item.VLNV] = item
		elif isinstance(item, Component):
			self._components.append(item)
		else:
			ex = TypeError(f"Parameter 'item' is neither a 'IpxactFile' nor a 'Component'.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(item)}'.")
			raise ex

	def ToXml(self, schema: IPXACTSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		xmlns = schema.NamespacePrefix
		buffer = dedent(f"""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:catalog
			\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			\txmlns:{xmlns}="{schema.SchemaUri}"
			\txsi:schemaLocation="{schema.SchemaUri} {schema.SchemaUrl}">
			{self._vlnv.ToXml(schema, isVersionedIdentifier=True)}
			\t<{xmlns}:description>{self._description}</{xmlns}:description>
			""")

		if self._catalogs:
			buffer += f"\t<{xmlns}:catalogs>\n"
			for ipxactFile in self._catalogs:
				buffer += ipxactFile.ToXml(2, schema)
			buffer += f"\t</{xmlns}:catalogs>\n"

		if self._components:
			buffer += f"\t<{xmlns}:components>\n"
			for ipxactFile in self._components:
				buffer += ipxactFile.ToXml(2, schema)
			buffer += f"\t</{xmlns}:components>\n"

		buffer += dedent(f"""\
			</{xmlns}:catalog>
			""")

		return buffer

	@readonly
	def Catalogs(self) -> Dict[VLNV, IpxactFile]:
		return self._catalogs
