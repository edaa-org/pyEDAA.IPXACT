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
from textwrap import dedent
from typing   import Optional as Nullable

from pyTooling.Decorators import export

from pyEDAA.IPXACT import RootElement, __DEFAULT_SCHEMA__, VLNV, IpxactSchema


@export
class DesignConfiguration(RootElement):
	"""Represents an IP-XACT design configuration."""

	_description:                  str
	_generatorChainConfiguration:  Nullable["GeneratorChainConfiguration"]
	_interconnectionConfiguration: Nullable["InterconnectionConfiguration"]
	_viewConfiguration:            Nullable["ViewConfiguration"]

	def __init__(self, vlnv: VLNV, description: str):
		super().__init__(vlnv)

		self._description =                  description
		self._generatorChainConfiguration =  None
		self._interconnectionConfiguration = None
		self._viewConfiguration =            None

	def SetItem(self, item):
		if isinstance(item,   GeneratorChainConfiguration):
			self._generatorChainConfiguration =   item
		elif isinstance(item, InterconnectionConfiguration):
			self._interconnectionConfiguration =  item
		elif isinstance(item, ViewConfiguration):
			self._viewConfiguration =             item
		else:
			raise ValueError()

	def ToXml(self, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		xmlns = schema.NamespacePrefix
		buffer = dedent(f"""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:designConfiguration
			\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			\txmlns:{xmlns}="{schema.SchemaUri}"
			\txsi:schemaLocation="{schema.SchemaUri} {schema.SchemaUrl}">
			{self._vlnv.ToXml(schema, isVersionedIdentifier=True)}
			\t<{xmlns}:description>{self._description}</{xmlns}:description>
			""")

		if self._generatorChainConfiguration:
			buffer += f"\t<{xmlns}:componentInstances>\n"
			buffer += self._generatorChainConfiguration.ToXml(2, schema)
			buffer += f"\t</{xmlns}:componentInstances>\n"

		if self._interconnectionConfiguration:
			buffer += f"\t<{xmlns}:interconnectionConfiguration>\n"
			buffer += self._interconnectionConfiguration.ToXml(2, schema)
			buffer += f"\t</{xmlns}:interconnectionConfiguration>\n"

		if self._viewConfiguration:
			buffer += f"\t<{xmlns}:viewConfiguration>\n"
			buffer += self._viewConfiguration.ToXml(2, schema)
			buffer += f"\t</{xmlns}:viewConfiguration>\n"

		buffer += dedent(f"""\
			</{xmlns}:designConfiguration>
			""")

		return buffer


@export
class GeneratorChainConfiguration:
	"""Represents an IP-XACT generator chain configuration."""

	def __init__(self) -> None:
		pass

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""


@export
class InterconnectionConfiguration:
	"""Represents an IP-XACT interconnection configuration."""

	def __init__(self) -> None:
		pass

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""


@export
class ViewConfiguration:
	"""Represents an IP-XACT view configuration."""

	def __init__(self) -> None:
		pass

	def ToXml(self, indent: int = 0, schema: IpxactSchema = __DEFAULT_SCHEMA__) -> str:
		"""Converts the object's data into XML format."""

		return ""
