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
"""Testcases for parsing IP-XACT example files."""
from pathlib   import Path
from unittest  import TestCase

from pyEDAA.IPXACT.Catalog   import Catalog
from pyEDAA.IPXACT.Component import Component
from pyEDAA.IPXACT.Design    import Design

if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Tudortimi(TestCase):
	def test_SampleCatalog(self) -> None:
		ipxactFile = Path("tests/Examples/tudortimi-ipxact/SampleCatalog.xml")
		catalog = Catalog(ipxactFile, parse=True)

	def test_SampleComponent(self) -> None:
		ipxactFile = Path("tests/Examples/tudortimi-ipxact/SampleComponent.xml")
		component = Component(ipxactFile, parse=True)

		self.assertEqual(2, len(component.FileSets))
		for fs in component.FileSets.values():
			self.assertEqual(1, len(fs.Files))

	def test_SampleDesign(self) -> None:
		ipxactFile = Path("tests/Examples/tudortimi-ipxact/SampleDesign.xml")
		design = Design(ipxactFile, parse=True)
