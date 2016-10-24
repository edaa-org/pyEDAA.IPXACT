# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python functions:   A DOM based IP-XACT implementation for Python
#
# Description:
# ------------------------------------
#		TODO:
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
from textwrap import dedent


__DEFAULT_NAMESPACE__ = "ipxact"


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
				{indent}<{xmlns}:vendor>{vendor}</{xmlns}:vendor>
				{indent}<{xmlns}:library>{library}</{xmlns}:library>
				{indent}<{xmlns}:name>{name}</{xmlns}:name>
				{indent}<{xmlns}:version>{version}</{xmlns}:version>\
			""")
		else:
			buffer = """{indent}<{xmlns}:vlnv vendor="{vendor}" library="{library}" name="{name}" version="{version}"/>"""
		
		return buffer.format(indent= "\t" *indent, xmlns=__DEFAULT_NAMESPACE__, vendor=self.Vendor, library=self.Library, name=self.Name, version=self.Version)
