# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
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

from pyEDAA.IPXACT import RootElement, __DEFAULT_SCHEMA__, Vlnv


class GeneratorChain(RootElement):
	"""Represents an IP-XACT generator chain."""

	def __init__(self, vlnv : Vlnv, displayName : str, description : str, chainGroup):
		"""Constructor"""

		super().__init__(vlnv)
		
		self._displayName =                   displayName
		self._description =                   description
		self._chainGroup =                    chainGroup
		self._generatorChainSelector =        None
		self._interconnectionConfiguration =  None
		self._generator =                     None

	def SetItem(self, item):
		if isinstance(item,   GeneratorChainSelector):      self._generatorChainSelector =      item
		elif isinstance(item, ComponentGeneratorSelector):  self._componentGeneratorSelector =  item
		elif isinstance(item, Generator):                   self._generator =                   item
		else:
			raise ValueError()

	def ToXml(self):
		"""Converts the object's data into XML format."""

		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:generatorChain
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:{xmlns}="{schemaUri}"
				xsi:schemaLocation="{schemaUri} {schemaUrl}">
			{versionedIdentifier}
				<{xmlns}:displayName>{displayName}</{xmlns}:displayName>
				<{xmlns}:description>{description}</{xmlns}:description>
				<{xmlns}:chainGroup>{chainGroup}</{xmlns}:chainGroup>
			""").format(
				xmlns=__DEFAULT_SCHEMA__.NamespacePrefix,
				schemaUri=__DEFAULT_SCHEMA__.SchemaUri,
				schemaUrl=__DEFAULT_SCHEMA__.SchemaUrl,
				versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True),
				displayName=self._displayName,
				description=self._description,
				chainGroup=self._chainGroup
			)
		
		if self._generatorChainSelector:
			buffer += "\t<{xmlns}:generatorChainSelector>\n"
			buffer += self._generatorChainSelector.ToXml(2)
			buffer += "\t</{xmlns}:generatorChainSelector>\n"
		
		if self._componentGeneratorSelector:
			buffer += "\t<{xmlns}:componentGeneratorSelector>\n"
			buffer += self._componentGeneratorSelector.ToXml(2)
			buffer += "\t</{xmlns}:componentGeneratorSelector>\n"
		
		if self._generator:
			buffer += "\t<{xmlns}:generator>\n"
			buffer += self._generator.ToXml(2)
			buffer += "\t</{xmlns}:generator>\n"
		
		buffer += dedent("""\
			</{xmlns}:generatorChain>
			""")
		
		return buffer.format(xmlns=__DEFAULT_SCHEMA__.NamespacePrefix)


class GeneratorChainSelector:
	"""Represents an IP-XACT generator chain selector."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class ComponentGeneratorSelector:
	"""Represents an IP-XACT component generator selector."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""


class Generator:
	"""Represents an IP-XACT generator."""

	def __init__(self):
		pass
	
	def ToXml(self, indent=0):
		"""Converts the object's data into XML format."""

		return ""
