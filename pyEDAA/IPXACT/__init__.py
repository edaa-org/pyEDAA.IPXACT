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
"""A DOM based IP-XACT implementation for Python."""
from pathlib  import Path
from sys      import version_info
from textwrap import dedent
from typing   import Union, Dict, Tuple, Optional as Nullable, ClassVar

from lxml.etree            import XMLParser, XML, XMLSchema, ElementTree, QName, _Element, _Comment
from pyTooling.Decorators  import export, readonly
from pyTooling.MetaClasses import ExtendedType, abstractmethod
from pyTooling.Common      import getFullyQualifiedName
from pyTooling.Versioning  import SemanticVersion, CalendarVersion

from .       import Schema
from .Schema import *

__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2016-2025, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.6.1"


@export
class IPXACTException(Exception):
	"""Base-exception for all exceptions in this package."""


@export
class IPXACTSchema(metaclass=ExtendedType, slots=True):
	"""Schema descriptor made of version, namespace prefix, URI, URL and local path."""

	_version:         Union[SemanticVersion, CalendarVersion]  #: Schema version
	_namespacePrefix: str                                      #: XML namespace prefix
	_schemaUri:       str                                      #: Schema URI
	_schemaUrl:       str                                      #: Schema URL
	_localPath:       Path                                     #: Local path

	def __init__(
		self,
		version: Union[str, SemanticVersion, CalendarVersion],
		xmlNamespacePrefix: str,
		schemaUri: str,
		schemaUrl: str,
		localPath: Path
	) -> None:
		"""
		Initializes an IP-XACT Schema description.

		:param version:            Version of the IP-XACT Schema.
		:param xmlNamespacePrefix: XML namespace prefix (``<prefix:element>``)
		:param schemaUri:          IP-XACT schema URI
		:param schemaUrl:          URL the IP-XACT schema definition file (XSD).
		:param localPath:          Path to the local XSD file.
		"""
		# TODO: add raises ... lines
		if version is None:
			raise ValueError(f"Parameter 'version' is None.")
		elif isinstance(version, str):
			if version.startswith("20"):
				self._version = CalendarVersion.Parse(version)
			else:
				self._version = SemanticVersion.Parse(version)
		elif isinstance(version, (SemanticVersion, CalendarVersion)):
			self._version = version
		else:
			ex = TypeError(f"Parameter 'version' is neither a 'SemanticVersion', a 'CalendarVersion' nor a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(version)}'.")
			raise ex

		if xmlNamespacePrefix is None:
			raise ValueError(f"Parameter 'namespacePrefix' is None.")
		elif not isinstance(xmlNamespacePrefix, str):
			ex = TypeError(f"Parameter 'namespacePrefix' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(version)}'.")
			raise ex

		if schemaUri is None:
			raise ValueError(f"Parameter 'schemaUri' is None.")
		elif not isinstance(schemaUri, str):
			ex = TypeError(f"Parameter 'schemaUri' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(schemaUri)}'.")
			raise ex

		if schemaUrl is None:
			raise ValueError(f"Parameter 'schemaUrl' is None.")
		elif not isinstance(schemaUrl, str):
			ex = TypeError(f"Parameter 'schemaUrl' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(schemaUrl)}'.")
			raise ex

		if localPath is None:
			raise ValueError(f"Parameter 'localPath' is None.")
		elif not isinstance(localPath, Path):
			ex = TypeError(f"Parameter 'localPath' is not a Path.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(localPath)}'.")
			raise ex

		self._namespacePrefix = xmlNamespacePrefix
		self._schemaUri =       schemaUri
		self._schemaUrl =       schemaUrl
		self._localPath =       localPath

	@readonly
	def Version(self) -> Union[SemanticVersion, CalendarVersion]:
		return self._version

	@readonly
	def NamespacePrefix(self) -> str:
		return self._namespacePrefix

	@readonly
	def SchemaUri(self) -> str:
		return self._schemaUri

	@readonly
	def SchemaUrl(self) -> str:
		return self._schemaUrl

	@readonly
	def LocalPath(self) -> Path:
		return self._localPath

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} IP-XACT {self._version} {self._schemaUri} - {self._localPath}>"

	def __str__(self) -> str:
		return f"IP-XACT {self._version}"


#                           version, xmlns,    URI                                                          URL,                                                              Local Path
_IPXACT_10 =   IPXACTSchema("1.0", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0", "", _IPXACT_10_INDEX)
_IPXACT_11 =   IPXACTSchema("1.1", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1", "", _IPXACT_11_INDEX)
_IPXACT_12 =   IPXACTSchema("1.2", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2", "", _IPXACT_12_INDEX)
_IPXACT_14 =   IPXACTSchema("1.4", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4", "", _IPXACT_14_INDEX)
_IPXACT_15 =   IPXACTSchema("1.5", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5", "", _IPXACT_15_INDEX)
_IPXACT_2009 = IPXACTSchema("2009", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009", "", _IPXACT_2009_INDEX)
_IPXACT_2014 = IPXACTSchema("2014", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2014", "http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd", _IPXACT_2014_INDEX)
_IPXACT_2022 = IPXACTSchema("2022", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2022", "http://www.accellera.org/XMLSchema/IPXACT/1685-2022/index.xsd", _IPXACT_2022_INDEX)

__VERSION_TABLE__: Dict[str, IPXACTSchema] = {
	'1.0':   _IPXACT_10,
	'1.1':   _IPXACT_11,
	'1.4':   _IPXACT_14,
	'1.5':   _IPXACT_15,
	'2009':  _IPXACT_2009,
	'2014':  _IPXACT_2014,
	'2022':  _IPXACT_2022
}          #: Dictionary of all IP-XACT versions mapping to :class:`IpxactSchema` instances.

__URI_MAP__: Dict[str, IPXACTSchema] = {value.SchemaUri: value for key, value in __VERSION_TABLE__.items()}  #: Mapping from schema URIs to :class:`IpxactSchema` instances.

__DEFAULT_VERSION__ = "2022"                                  #: IP-XACT default version
__DEFAULT_SCHEMA__ =  __VERSION_TABLE__[__DEFAULT_VERSION__]  #: IP-XACT default Schema


@export
class VLNV(metaclass=ExtendedType, slots=True):
	"""VLNV data structure (Vendor, Library, Name, Version) as a unique identifier in IP-XACT."""

	_vendor:  str              #: Vendor name in a VLNV unique identifier
	_library: str              #: Library name in a VLNV unique identifier
	_name:    str              #: Component name in a VLNV unique identifier
	_version: SemanticVersion  #: Version in a VLNV unique identifier

	def __init__(self, vendor: str, library: str, name: str, version: Union[str, SemanticVersion]) -> None:
		"""
		Initializes the VLNV data structure.

		:param vendor:  Vendor name in a VLNV unique identifier
		:param library: Library name in a VLNV unique identifier
		:param name:    Component name in a VLNV unique identifier
		:param version: Version in a VLNV unique identifier
		"""

		if vendor is None:
			raise ValueError(f"Parameter 'vendor' is None.")
		elif not isinstance(vendor, str):
			ex = TypeError(f"Parameter 'vendor' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(vendor)}'.")
			raise ex

		if library is None:
			raise ValueError(f"Parameter 'library' is None.")
		elif not isinstance(library, str):
			ex = TypeError(f"Parameter 'library' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(library)}'.")
			raise ex

		if name is None:
			raise ValueError(f"Parameter 'name' is None.")
		elif not isinstance(name, str):
			ex = TypeError(f"Parameter 'name' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(name)}'.")
			raise ex

		if version is None:
			raise ValueError(f"Parameter 'version' is None.")
		elif isinstance(version, str):
			self._version = SemanticVersion.Parse(version)
		elif isinstance(version, SemanticVersion):
			self._version = version
		else:
			ex = TypeError(f"Parameter 'version' is neither a 'SemanticVersion' nor a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(version)}'.")
			raise ex

		self._vendor =   vendor
		self._library =  library
		self._name =     name

	@readonly
	def Vendor(self) -> str:
		return self._vendor

	@readonly
	def Library(self) -> str:
		return self._library

	@readonly
	def Name(self) -> str:
		return self._name

	@readonly
	def Version(self) -> SemanticVersion:
		return self._version

	def ToXml(self, indent=1, schema: IPXACTSchema = __DEFAULT_SCHEMA__, isVersionedIdentifier=False) -> str:
		"""
		Converts the object's data into XML format.

		:param indent:                Level of indentations.
		:param schema:                XML schema.
		:param isVersionedIdentifier: If true, generate 4 individual tags (``<vendor>``, ``<library>``, ``<name>``,
		                              ``<version>``), otherwise a single ``<vlnv>``-tag with attributes.
		:return:
		"""

		# WORKAROUND:
		#   Python <=3.11:
		#   {'\t' * indent} is not supported by Python before 3.12 due to a backslash within {...}
		indent = "\t" * indent
		xmlns = schema.NamespacePrefix

		if isVersionedIdentifier:
			return dedent(f"""\
				{indent}<{xmlns}:vendor>{self._vendor}</{xmlns}:vendor>
				{indent}<{xmlns}:library>{self._library}</{xmlns}:library>
				{indent}<{xmlns}:name>{self._name}</{xmlns}:name>
				{indent}<{xmlns}:version>{self._version}</{xmlns}:version>
			""")
		else:
			return f"""{indent}<{xmlns}:vlnv vendor="{self._vendor}" library="{self._library}" name="{self._name}" version="{self._version}"/>"""


@export
class Element(metaclass=ExtendedType, slots=True):
	"""Base-class for all IP-XACT elements."""

	def __init__(self, vlnv: VLNV) -> None:
		"""
		Initializes the Element class.
		"""


@export
class NamedElement(Element):
	"""Base-class for all IP-XACT elements with a VLNV."""

	_vlnv: VLNV   #: VLNV unique identifier.

	def __init__(self, vlnv: VLNV) -> None:
		"""
		Initializes the NameElement with an VLNV field for all derives classes.

		:param vlnv:       VLNV unique identifier.
		:raises TypeError: If parameter vlnv is not a VLNV.
		"""
		if not isinstance(vlnv, VLNV):
			ex = TypeError(f"Parameter 'vlnv' is not a VLNV.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(vlnv)}'.")
			raise ex

		self._vlnv =    vlnv

	@readonly
	def VLNV(self) -> VLNV:
		return self._vlnv


@export
class RootElement(NamedElement):
	"""Base-class for all IP-XACT root elements."""

	_file:        Nullable[Path]
	_rootTagName: ClassVar[str] = ""
	_xmlRoot:     Nullable[_Element]
	_xmlSchema:   Nullable[_Element]

	_description: str

	def __init__(self, file: Nullable[Path] = None, parse: bool = False, vlnv: Nullable[VLNV] = None, description: Nullable[str] = None) -> None:
		self._description = description

		if file is None:
			super().__init__(vlnv)
			self._file = None
		elif isinstance(file, Path):
			self._file = file
			vlnv = None
			if parse:
				self.OpenAndValidate()
				vlnv, self._description = self.ParseVLNVAndDescription()

			super().__init__(vlnv)
		else:
			ex = TypeError(f"Parameter 'file' is not a Path.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(file)}'.")
			raise ex

	def OpenAndValidate(self) -> None:
		if not self._file.exists():
			raise IPXACTException(f"IPXACT file '{self._file}' not found.") from FileNotFoundError(str(self._file))

		try:
			with self._file.open("rb") as fileHandle:
				content = fileHandle.read()
		except OSError as ex:
			raise IPXACTException(f"Couldn't open '{self._file}'.") from ex

		xmlParser =     XMLParser(remove_blank_text=True, encoding="utf-8")
		self._xmlRoot = XML(content, parser=xmlParser, base_url=self._file.resolve().as_uri())  # - relative paths are not supported
		rootTag =       QName(self._xmlRoot.tag)

		if rootTag.localname != self._rootTagName:
			raise IPXACTException(f"The input IP-XACT file is not a {self._rootTagName} file.")

		namespacePrefix = self._xmlRoot.prefix
		namespaceURI =    self._xmlRoot.nsmap[namespacePrefix]
		if namespaceURI in __URI_MAP__:
			ipxactSchema = __URI_MAP__[namespaceURI]
		else:
			raise IPXACTException(f"The input IP-XACT file uses an unsupported namespace: '{namespaceURI}'.")

		try:
			with ipxactSchema.LocalPath.open("rb") as fileHandle:
				schema = fileHandle.read()
		except OSError as ex:
			raise IPXACTException(f"Couldn't open IP-XACT schema '{ipxactSchema.LocalPath}' for {namespacePrefix} ({namespaceURI}).") from ex

		schemaRoot =      XML(schema, parser=xmlParser, base_url=ipxactSchema.LocalPath.as_uri())
		schemaTree =      ElementTree(schemaRoot)
		self._xmlSchema = XMLSchema(schemaTree)

		try:
			self._xmlSchema.assertValid(self._xmlRoot)
		except Exception as ex:
			raise IPXACTException(f"The input IP-XACT file is not valid according to XML schema {namespaceURI}.") from ex

	def ParseVLNVAndDescription(self) -> Tuple[VLNV, str]:
		vendor = None
		library = None
		name = None
		version = None
		description = None

		found = 0
		i = iter(self._xmlRoot)
		for element in i:
			if isinstance(element, _Comment):
				continue

			elementLocalname = QName(element).localname
			if elementLocalname == "vendor":
				found |= 1
				vendor = element.text
			elif elementLocalname == "library":
				found |= 2
				library = element.text
			elif elementLocalname == "name":
				found |= 4
				name = element.text
			elif elementLocalname == "version":
				found |= 8
				version = element.text
			elif elementLocalname == "description":
				found |= 16
				description = element.text
			else:
				self.Parse(element)

			if found == 31:
				break

		for element in i:
			if isinstance(element, _Comment):
				continue

			self.Parse(element)

		vlnv = VLNV(vendor=vendor, library=library, name=name, version=version)
		return vlnv, description

	@abstractmethod
	def Parse(self, element: _Element) -> None:
		pass
