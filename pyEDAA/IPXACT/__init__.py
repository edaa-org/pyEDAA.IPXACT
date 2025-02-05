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
from typing import Union, Dict

from pyTooling.Decorators import export, readonly
from pyTooling.Common     import getResourceFile, getFullyQualifiedName
from pyTooling.Versioning import SemanticVersion, CalendarVersion

from . import Schema


__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2016-2025, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.4.0"


@export
class IpxactSchema:
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


#                           version, xmlns,    URI                                                          URL,                                                              Local Path
_IPXACT_10 =   IpxactSchema("1.0",  "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",       "",                                                              getResourceFile(Schema, "ipxact-1.0/index.xsd"))
_IPXACT_11 =   IpxactSchema("1.1",  "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",       "",                                                              getResourceFile(Schema, "ipxact-1.1/index.xsd"))
_IPXACT_12 =   IpxactSchema("1.2",  "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",       "",                                                              getResourceFile(Schema, "ipxact-1.2/index.xsd"))
_IPXACT_14 =   IpxactSchema("1.4",  "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",       "",                                                              getResourceFile(Schema, "ipxact-1.4/index.xsd"))
_IPXACT_15 =   IpxactSchema("1.5",  "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",       "",                                                              getResourceFile(Schema, "ipxact-1.5/index.xsd"))
_IPXACT_2009 = IpxactSchema("2009", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009", "",                                                              getResourceFile(Schema, "ieee-1685-2009/index.xsd"))
_IPXACT_2014 = IpxactSchema("2014", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",        "http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd", getResourceFile(Schema, "ieee-1685-2014/index.xsd"))
_IPXACT_2022 = IpxactSchema("2022", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",        "http://www.accellera.org/XMLSchema/IPXACT/1685-2022/index.xsd", getResourceFile(Schema, "ieee-1685-2022/index.xsd"))

__VERSION_TABLE__: Dict[str, IpxactSchema] = {
	'1.0':   _IPXACT_10,
	'1.1':   _IPXACT_11,
	'1.4':   _IPXACT_14,
	'1.5':   _IPXACT_15,
	'2009':  _IPXACT_2009,
	'2014':  _IPXACT_2014,
	'2022':  _IPXACT_2022
}          #: Dictionary of all IP-XACT versions mapping to :class:`IpxactSchema` instances.

__URI_MAP__: Dict[str, IpxactSchema] = {value.SchemaUri: value for key, value in __VERSION_TABLE__.items()}  #: Mapping from schema URIs to :class:`IpxactSchema` instances.

__DEFAULT_VERSION__ = "2022"                                  #: IP-XACT default version
__DEFAULT_SCHEMA__ =  __VERSION_TABLE__[__DEFAULT_VERSION__]  #: IP-XACT default Schema


@export
class Vlnv:
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

	def ToXml(self, indent=1, isVersionedIdentifier=False):
		"""Converts the object's data into XML format."""

		if isVersionedIdentifier:
			buffer = dedent("""\
				{indent}<{xmlns}:vendor>{vendor}</{xmlns}:vendor>
				{indent}<{xmlns}:library>{library}</{xmlns}:library>
				{indent}<{xmlns}:name>{name}</{xmlns}:name>
				{indent}<{xmlns}:version>{version}</{xmlns}:version>\
			""")
		else:
			buffer = """{indent}<{xmlns}:vlnv vendor="{vendor}" library="{library}" name="{name}" version="{version}"/>"""

		return buffer.format(indent= "\t" *indent, xmlns=__DEFAULT_SCHEMA__.NamespacePrefix, vendor=self._vendor, library=self._library, name=self._name, version=self._version)


@export
class RootElement:
	"""Base-class for all IP-XACT data classes."""

	_vlnv: Vlnv   #: VLNV unique identifier.

	def __init__(self, vlnv: Vlnv) -> None:
		"""
		Initializes the RootElement with an VLNV field for all derives classes.

		:param vlnv: VLNV unique identifier.
		"""
		self._vlnv =    vlnv

	@classmethod
	def FromFile(cls, file):
		pass


@export
class PyIpxactException(Exception):
	"""Base-exception for all exceptions in this package."""
