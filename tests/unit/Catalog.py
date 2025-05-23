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
"""Testcase for ``Catalog``."""
from pathlib  import Path
from unittest import TestCase

from pyEDAA.IPXACT         import VLNV
from pyEDAA.IPXACT.Catalog import IpxactFile, Catalog


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Catalogs(TestCase):
	# @mark.xfail(reason="This has a known issue.")
	def test_Catalog(self) -> None:
		vlnv = VLNV("VHDL", "PoC", "PoC", "1.0")

		catalog = Catalog(vlnv=vlnv, description="IP Core Library")
		catalog.AddItem(IpxactFile(VLNV(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.uart.RX", version=vlnv.Version), "uart_RX.xml", "A UART receiver."))
		catalog.AddItem(IpxactFile(VLNV(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.uart.TX", version=vlnv.Version), "uart_TX.xml", "A UART transmitter."))
		catalog.AddItem(IpxactFile(VLNV(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.uart.Wrapper", version=vlnv.Version), "uart_Wrapper.xml", "A UART wrapper."))

		self.assertIs(vlnv, catalog.VLNV)
		self.assertEqual(3, len(catalog.Catalogs))

	# @mark.xfail(reason="This has a known issue.")
	def test_ReadFromFile(self) -> None:
		filePath = Path("tests/Examples/Catalog.xml")
		catalog = Catalog(filePath, parse=True)

		self.assertEqual("VHDL", catalog.VLNV.Vendor)
		self.assertEqual("PoC", catalog.VLNV.Library)
		self.assertEqual("PoC", catalog.VLNV.Name)
		self.assertEqual("1.0", catalog.VLNV.Version)
		self.assertEqual(3, len(catalog.Catalogs))
