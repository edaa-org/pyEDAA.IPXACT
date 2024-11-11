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
# Copyright 2017-2024 Patrick Lehmann - Bötzingen, Germany                                                             #
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
from textwrap import dedent

from pyTooling.Decorators import export

__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2016-2024, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.3.2"


@export
class IpxactSchemaStruct:
	"""Schema descriptor made of version, namespace prefix, URI, URL and local path."""

	Version: str             #: Schema version
	NamespacePrefix: str     #: XML namespace prefix
	SchemaUri: str           #: Schema URI
	SchemaUrl: str           #: Schema URL
	LocalPath: Path          #: Local path

	def __init__(self, version: str, namespacePrefix: str, schemaUri: str, schemaUrl: str, localPath: Path):
		"""Constructor"""
		self.Version =         version
		self.NamespacePrefix = namespacePrefix
		self.SchemaUri =       schemaUri
		self.SchemaUrl =       schemaUrl
		self.LocalPath =       localPath


_SCHEMA_PATH =  Path("lib/schema")  #version, xmlns, URI                                                            URL,                                                              Local Path
_IPXACT_10 =    IpxactSchemaStruct("1.0", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",         "",                                                               _SCHEMA_PATH / "1.0")
_IPXACT_11 =    IpxactSchemaStruct("1.1", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",         "",                                                               _SCHEMA_PATH / "1.1")
_IPXACT_14 =    IpxactSchemaStruct("1.4", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",         "",                                                               _SCHEMA_PATH / "1.4")
_IPXACT_15 =    IpxactSchemaStruct("1.5", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",         "",                                                               _SCHEMA_PATH / "1.5")
_IPXACT_2009 =  IpxactSchemaStruct("2009", "spirit", "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",  "",                                                               _SCHEMA_PATH / "2009")
_IPXACT_2014 =  IpxactSchemaStruct("2014", "ipxact", "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",         "http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd",  _SCHEMA_PATH / "2014")

__VERSION_TABLE__ = {
	'1.0':   _IPXACT_10,
	'1.1':   _IPXACT_11,
	'1.4':   _IPXACT_14,
	'1.5':   _IPXACT_15,
	'2009':  _IPXACT_2009,
	'2014':  _IPXACT_2014
}          #: Dictionary of all IP-XACT versions mapping to :class:`IpxactSchemaStruct` instances.

__URI_MAP__ = {value.SchemaUri: value for key, value in __VERSION_TABLE__.items()}  #: Mapping from schema URIs to :class:`IpxactSchemaStruct` instances.


__DEFAULT_VERSION__ = "2014"                                  #: IP-XACT default version
__DEFAULT_SCHEMA__ =  __VERSION_TABLE__[__DEFAULT_VERSION__]  #: IP-XACT default Schema


@export
class Vlnv:
	"""VLNV data structure (Vendor, Library, Name, Version) as a unique identifier in IP-XACT."""

	Vendor:  str    #: Vendor name in a VLNV unique identifier
	Library: str    #: Library name in a VLNV unique identifier
	Name:    str    #: Component name in a VLNV unique identifier
	Version: str    #: Version in a VLNV unique identifier

	def __init__(self, vendor, library, name, version):
		"""Constructor"""
		self.Vendor =   vendor
		self.Library =  library
		self.Name =     name
		self.Version =  version

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

		return buffer.format(indent= "\t" *indent, xmlns=__DEFAULT_SCHEMA__.NamespacePrefix, vendor=self.Vendor, library=self.Library, name=self.Name, version=self.Version)


@export
class RootElement:
	"""Base-class for all IP-XACT data classes."""

	_vlnv: Vlnv   #: VLNV unique identifier.

	def __init__(self, vlnv):
		"""Base-constructor to set a VLNV field for all derives classes."""
		self._vlnv =    vlnv

	@classmethod
	def FromFile(cls, file):
		pass


@export
class PyIpxactException(Exception):
	"""Base-exception for all exceptions in this package."""
