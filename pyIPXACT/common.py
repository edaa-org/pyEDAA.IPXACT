from textwrap import dedent


class RootElement:
	def __init__(self, vlnv):
		self._vlnv =    vlnv


class Vlnv:
	def __init__(self, vendor, library, name, version):
		self.Vendor =   vendor
		self.Library =  library
		self.Name =     name
		self.Version =  version
	
	def ToXml(self, indent=1, isVersionedIdentifier=False):
		if isVersionedIdentifier:
			buffer = dedent("""\
				{indent}<ipxact:vendor>{vendor}</ipxact:vendor>
				{indent}<ipxact:library>{library}</ipxact:library>
				{indent}<ipxact:name>{name}</ipxact:name>
				{indent}<ipxact:version>{version}</ipxact:version>\
			""")
		else:
			buffer = """{indent}<ipxact:vlnv vendor="{vendor}" library="{library}" name="{name}" version="{version}"/>"""
		
		return buffer.format(indent="\t"*indent, vendor=self.Vendor, library=self.Library, name=self.Name, version=self.Version)

