from textwrap import dedent

from pyIPXACT.common import RootElement
from pyIPXACT.component import Component


class Catalog(RootElement):
	def __init__(self, vlnv, description):
		super().__init__(vlnv)
		
		self._description = description
		self._abstractionDefinitions =  []
		self._abstractors =             []
		self._busInterfaces =           []
		self._catalogs =                []
		self._components =              []
		self._designConfigurations =    []
		self._designs =                 []
		self._generatorChains =         []
	                                  
	def AddCatalogItem(self, item):
		if isinstance(item, IpxactFile):
			self._catalogs.append(item)
		elif isinstance(item, Component):
			self._components.append(item)
		else:
			raise ValueError()

	def ToXml(self):
		buffer = dedent("""\
			<?xml xml version="1.0" encoding="UTF-8"?>
			<ipxact:catalog
				xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
				xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014/
														http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
			{versionedIdentifier}
				<ipxact:description>{description}</ipxact:description>
			""").format(versionedIdentifier=self._vlnv.ToXml(isVersionedIdentifier=True), description=self._description)
			
		if self._catalogs:
			buffer += "\t<ipxact:catalogs>\n"
			for ipxactFile in self._catalogs:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</ipxact:catalogs>\n"
		
		if self._components:
			buffer += "\t<ipxact:components>\n"
			for ipxactFile in self._components:
				buffer += ipxactFile.ToXml(2)
			buffer += "\t</ipxact:components>\n"
		
		buffer += dedent("""\
			</ipxact:catalog>
			""")
		
		return buffer


class IpxactFile:
	def __init__(self, vlnv, name, description):
		self._vlnv = vlnv
		self._name = name
		self._description = description
	
	def ToXml(self, indent):
		_indent = "\t" * indent
		buffer = dedent("""\
			{indent}<ipxact:ipxactFile>
			{indent}	{vlnv}
			{indent}	<ipxact:name>{path}</ipxact:name>
			{indent}	<ipxact:description>{description}</ipxact:description>
			{indent}</ipxact:ipxactFile>
		""").format(indent=_indent, vlnv=self._vlnv.ToXml(0), path=self._name, description=self._description)
		
		return buffer
