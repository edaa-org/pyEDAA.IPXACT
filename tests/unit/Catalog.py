# ==================================================================================================================== #
#             _____           _ _               ____ _     ___    _    _         _                  _   _              #
#  _ __  _   |_   _|__   ___ | (_)_ __   __ _  / ___| |   |_ _|  / \  | |__  ___| |_ _ __ __ _  ___| |_(_) ___  _ __   #
# | '_ \| | | || |/ _ \ / _ \| | | '_ \ / _` || |   | |    | |  / _ \ | '_ \/ __| __| '__/ _` |/ __| __| |/ _ \| '_ \  #
# | |_) | |_| || | (_) | (_) | | | | | | (_| || |___| |___ | | / ___ \| |_) \__ \ |_| | | (_| | (__| |_| | (_) | | | | #
# | .__/ \__, ||_|\___/ \___/|_|_|_| |_|\__, (_)____|_____|___/_/   \_\_.__/|___/\__|_|  \__,_|\___|\__|_|\___/|_| |_| #
# |_|    |___/                          |___/                                                                          #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2022 Patrick Lehmann - Bötzingen, Germany                                                             #
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
from pathlib import Path
from unittest     import TestCase

from pyEDAA.IPXACT import Vlnv
from pyEDAA.IPXACT.Catalog import Catalog
from pyEDAA.IPXACT.Design import IpxactFile


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Catalogs(TestCase):
	def test_Catalog(self):
		vlnv = Vlnv("VLSI-EDA", "PoC", "PoC", "1.0")

		catalog = Catalog(vlnv, "IP Core Library")
		catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.RX", version=vlnv.Version), "uart_RX.xml", "A UART receiver."))
		catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.TX", version=vlnv.Version), "uart_TX.xml", "A UART transmitter."))
		catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.Wrapper", version=vlnv.Version), "uart_RX.xml", "A UART wrapper."))

	def test_ReadFromFile(self):
		filePath = Path("catalog.xml")
		catalog = Catalog.FromFile(filePath)
