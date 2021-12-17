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
from typing import List

from lxml               import etree
from os                 import chdir as os_chdir
from textwrap           import dedent

from pathlib            import Path

from pyEDAA.IPXACT           import RootElement, Vlnv, PyIpxactException, __URI_MAP__, __DEFAULT_SCHEMA__
from pyEDAA.IPXACT.Component import Component


class IpxactFile:
	"""Represents a IP-XACT file."""

	_vlnv : Vlnv =        None    #: VLNV unique identifier
	_name : str =         None    #: Name
	_description : str =  None    #: Description

	def __init__(self, vlnv : Vlnv, name : str, description : str):
		"""Constructor"""
		self._vlnv = vlnv
		self._name = name
		self._description = description
	
	@classmethod
	def FromXml(cls, element):
		"""Constructs an instance of ``IpxactFile`` from an lxml element."""

		elementTag = etree.QName(element.tag)
		if (elementTag.localname != "ipxactFile"):
			raise PyIpxactException("Expected tag 'ipxactFile'.")
		
		for element2 in element:
			element3 = etree.QName(element2)
			if (element3.localname == "vlnv"):
				vendor =  element2.get("vendor")
				library = element2.get("library")
				name2 =   element2.get("name")
				version = element2.get("version")
				
				vlnv = Vlnv(vendor, library, name2, version)
			elif (element3.localname == "name"):
				name = element2.text
			elif (element3.localname == "description"):
				description = element2.text
			else:
				raise PyIpxactException("Unsupported tag '{0}' in node 'ipxactFile'.".format(element.localname))
		
		ipxactFile = cls(vlnv, name, description)
		return ipxactFile
	
	def ToXml(self, indent):
		"""Converts the object's data into XML format."""

		_indent = "\t" * indent
		buffer = dedent("""\
			{indent}<{xmlns}:ipxactFile>
			{indent}	{vlnv}
			{indent}	<{xmlns}:name>{path}</{xmlns}:name>
			{indent}	<{xmlns}:description>{description}</{xmlns}:description>
			{indent}</{xmlns}:ipxactFile>
		""").format(indent=_indent, xmlns=__DEFAULT_SCHEMA__.NamespacePrefix, vlnv=self._vlnv.ToXml(0), path=self._name, description=self._description)
		
		return buffer


class Catalog(RootElement):
	"""Represents an IP-XACT catalog."""

	_description :            str =   None
	_abstractionDefinitions : List =  None
	_abstractors :            List =  None
	_busInterfaces :          List =  None
	_catalogs :               List =  None
	_components :             List =  None
	_designConfigurations :   List =  None
	_designs :                List =  None
	_generatorChains :        List =  None

	def __init__(self, vlnv : Vlnv, description : str):
		super().__init__(vlnv)
		
		self._description =             description
		self._abstractionDefinitions =  []
		self._abstractors =             []
		self._busInterfaces =           []
		self._catalogs =                []
		self._components =              []
		self._designConfigurations =    []
		self._designs =                 []
		self._generatorChains =         []

	@classmethod
	def FromFile(cls, filePath : Path):
		"""Constructs an instance of ``Catalog`` from a file."""

		if (not filePath.exists()): raise PyIpxactException("File '{0!s}' not found.".format(filePath)) from FileNotFoundError(str(filePath))
		
		try:
			with filePath.open(encoding="utf-8") as fileHandle:
				content = fileHandle.read()
				content = bytes(bytearray(content, encoding='utf-8'))
		except OSError as ex:
			raise PyIpxactException("Couldn't open '{0!s}'.".format(filePath)) from ex
		
		os_chdir("lib/schema")
		
		schemaPath = Path("index.xsd")
		try:
			with schemaPath.open(encoding="utf-8") as fileHandle:
				schema = fileHandle.read()
				schema = bytes(bytearray(schema, encoding='utf-8'))
		except OSError as ex:
			raise PyIpxactException("Couldn't open '{0!s}'.".format(schemaPath)) from ex
		
		xmlParser = etree.XMLParser(remove_blank_text=True, encoding="utf-8")
		
		schemaRoot =  etree.XML(schema, xmlParser)
		schemaTree =  etree.ElementTree(schemaRoot)
		xmlschema =   etree.XMLSchema(schemaTree)
		root =        etree.XML(content, xmlParser)
		rootTag =     etree.QName(root.tag)
		
		if (not xmlschema.validate(root)):
			raise PyIpxactException("The input IP-XACT file is not valid.")
		
		if (rootTag.namespace not in __URI_MAP__):
			raise PyIpxactException("The input IP-XACT file uses an unsupported namespace: '{0}'.".format(rootTag.namespace))
		
		if (rootTag.localname != "catalog"):
			raise PyIpxactException("The input IP-XACT file is not a catalog file.")
		
		print("==" * 20)
		
		items = []
		for rootElements in root:
			element = etree.QName(rootElements)
			if (element.localname == "vendor"):
				vendor = rootElements.text
			elif (element.localname == "library"):
				library = rootElements.text
			elif (element.localname == "name"):
				name = rootElements.text
			elif (element.localname == "version"):
				version = rootElements.text
			elif (element.localname == "description"):
				description = rootElements.text
			elif (element.localname == "catalogs"):
				for ipxactFileElement in rootElements:
					items.append(IpxactFile.FromXml(ipxactFileElement))
			else:
				raise PyIpxactException("Unsupported tag '{0}' at root-level.".format(element.localname))
			
		print("==" * 20)
		
		vlnv =    Vlnv(vendor=vendor, library=library, name=name, version=version)
		catalog = cls(vlnv, description=description)
		for item in items:
			catalog.AddItem(item)
			
		return catalog

	def AddItem(self, item):
		if isinstance(item, IpxactFile):          self._catalogs.append(item)
		elif isinstance(item, Component):         self._components.append(item)
		else:
			raise ValueError()
		

	def ToXml(self):
		"""Converts the object's data into XML format."""

		buffer = dedent("""\
			<?xml version="1.0" encoding="UTF-8"?>
			<{xmlns}:catalog
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
		
		if self._catalogs:
			buffer += "\t<{xmlns}:catalogs>\n"
			for ipxactFile in self._catalogs:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</{xmlns}:catalogs>\n"
		
		if self._components:
			buffer += "\t<{xmlns}:components>\n"
			for ipxactFile in self._components:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</{xmlns}:components>\n"
		
		buffer += dedent("""\
			</{xmlns}:catalog>
			""")
		
		return buffer.format(xmlns=__DEFAULT_SCHEMA__.NamespacePrefix)
