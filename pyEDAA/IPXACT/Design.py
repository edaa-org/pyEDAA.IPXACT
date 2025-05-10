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
from sys      import version_info
from textwrap import dedent
from typing   import List

from pyTooling.Decorators import export
from pyTooling.Common     import getFullyQualifiedName

from pyEDAA.IPXACT import RootElement, __DEFAULT_SCHEMA__, VLNV, IpxactSchema, Element


@export
class Design(RootElement):
	"""Represents an IP-XACT design."""

	_description:        str
	_componentInstances: List
	_interconnections:   List
	_adHocConnections:   List

	def __init__(self, vlnv: VLNV, description: str):
		"""
		Instantiates a design structure.

		:param vlnv:        A Vendor-Library-Name-Version unique identified.
		:param description: A description text.
		"""
		super().__init__(vlnv)

		if not isinstance(description, str):
			ex = TypeError(f"Parameter 'description' is not a string.")
			if version_info >= (3, 11):  # pragma: no cover
				ex.add_note(f"Got type '{getFullyQualifiedName(description)}'.")
			raise ex
		elif description == "":
			raise ValueError(f"Parameter 'description' is empty.")

		self._description =             description
		self._componentInstances =      []
		self._interconnections =        []
		self._adHocConnections =        []

	def AddItem(self, item) -> None:
		if isinstance(item, ComponentInstance):
			self._componentInstances.append(item)
		elif isinstance(item, Interconnection):
			self._interconnections.append(item)
		elif isinstance(item, AdHocConnection):
			self._adHocConnections.append(item)
		else:
			raise ValueError()

	def ToXml(self, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		xmlns = schema.NamespacePrefix
		buffer = dedent(f"""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:design
			\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			\txmlns:{xmlns}="{schema.SchemaUri}"
			\txsi:schemaLocation="{schema.SchemaUri} {schema.SchemaUrl}">
			{self._vlnv.ToXml(schema, isVersionedIdentifier=True)}
			\t<{xmlns}:description>{self._description}</{xmlns}:description>
			""")

		if self._componentInstances:
			buffer += f"\t<{xmlns}:componentInstances>\n"
			for componentInstance in self._componentInstances:
				buffer += componentInstance.ToXml(2, schema)
			buffer += f"\t</{xmlns}:componentInstances>\n"

		if self._interconnections:
			buffer += f"\t<{xmlns}:interconnections>\n"
			for interconnection in self._interconnections:
				buffer += interconnection.ToXml(2, schema)
			buffer += f"\t</{xmlns}:interconnections>\n"

		if self._adHocConnections:
			buffer += f"\t<{xmlns}:adHocConnections>\n"
			for adHocConnection in self._adHocConnections:
				buffer += adHocConnection.ToXml(2, schema)
			buffer += f"\t</{xmlns}:adHocConnections>\n"

		buffer += dedent(f"""\
			</{xmlns}:design>
			""")

		return buffer


@export
class IpxactFile(Element):
	"""Represents a IP-XACT file."""

	_name:        str    #: Name
	_description: str    #: Description

	def __init__(self, vlnv, name, description):
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

		self._name = name
		self._description = description

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		# WORKAROUND:
		#   Python <=3.11:
		#   {'\t' * indent} is not supported by Python before 3.12 due to a backslash within {...}
		indent = "\t" * indent
		xmlns = schema.NamespacePrefix
		return dedent(f"""\
			{indent}<{xmlns}:ipxactFile>
			{indent}\t{self._vlnv.ToXml(indent)}
			{indent}\t<{xmlns}:name>{self._name}</{xmlns}:name>
			{indent}\t<{xmlns}:description>{self._description}</{xmlns}:description>
			{indent}</{xmlns}:ipxactFile>
		""")


@export
class ComponentInstance(Element):
	"""Represents an IP-XACT component instance."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""


@export
class Interconnection(Element):
	"""Represents an IP-XACT interconnection."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""


@export
class AdHocConnection(Element):
	"""Represents an IP-XACT ad-hoc connection."""

	def __init__(self, vlnv: VLNV) -> None:
		super().__init__(vlnv)

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""
