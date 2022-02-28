# ==================================================================================================================== #
#              ___ ______  __    _    ____ _____
#  _ __  _   _|_ _|  _ \ \/ /   / \  / ___|_   _|
# | '_ \| | | || || |_) \  /   / _ \| |     | |
# | |_) | |_| || ||  __//  \  / ___ \ |___  | |
# | .__/ \__, |___|_|  /_/\_\/_/   \_\____| |_|
# |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python module:      A DOM based IP-XACT implementation for Python
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

from pyTooling.Decorators import export

from pyEDAA.IPXACT import RootElement, __DEFAULT_SCHEMA__, Vlnv


@export
class DesignConfiguration(RootElement):
	"""Represents an IP-XACT design configuration."""

	def __init__(self, vlnv : Vlnv, description : str):
		super().__init__(vlnv)

		self._description =             description
		self._generatorChainConfiguration =   None
		self._interconnectionConfiguration =  None
		self._viewConfiguration =             None

	def SetItem(self, item):
		if isinstance(item,   GeneratorChainConfiguration):   self._generatorChainConfiguration =   item
		elif isinstance(item, InterconnectionConfiguration):  self._interconnectionConfiguration =  item
		elif isinstance(item, ViewConfiguration):             self._viewConfiguration =             item
		else:
			raise ValueError()

	def ToXml(self):
		"""Converts the object's data into XML format."""

		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:designConfiguration
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

		if self._generatorChainConfiguration:
			buffer += "\t<{xmlns}:componentInstances>\n"
			buffer += self._generatorChainConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:componentInstances>\n"

		if self._interconnectionConfiguration:
			buffer += "\t<{xmlns}:interconnectionConfiguration>\n"
			buffer += self._interconnectionConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:interconnectionConfiguration>\n"

		if self._viewConfiguration:
			buffer += "\t<{xmlns}:viewConfiguration>\n"
			buffer += self._viewConfiguration.ToXml(2)
			buffer += "\t</{xmlns}:viewConfiguration>\n"

		buffer += dedent("""\
			</{xmlns}:designConfiguration>
			""")

		return buffer.format(xmlns=__DEFAULT_SCHEMA__.NamespacePrefix)


@export
class GeneratorChainConfiguration:
	"""Represents an IP-XACT generator chain configuration."""

	def __init__(self):
		pass

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class InterconnectionConfiguration:
	"""Represents an IP-XACT interconnection configuration."""

	def __init__(self):
		pass

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


@export
class ViewConfiguration:
	"""Represents an IP-XACT view configuration."""

	def __init__(self):
		pass

	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""
