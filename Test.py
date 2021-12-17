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
from pathlib import Path

from pyEDAA.IPXACT           import Vlnv
from pyEDAA.IPXACT.Catalog   import Catalog, IpxactFile
from pyEDAA.IPXACT.Component import Component
from pyEDAA.IPXACT.Design    import Design
from pyEDAA.IPXACT.DesignConfiguration import DesignConfiguration


vlnv = Vlnv("VLSI-EDA", "PoC", "PoC", "1.0")

# ==============================================================================
catalog = Catalog(vlnv, "IP Core Library")
catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.RX", version=vlnv.Version), "uart_RX.xml", "A UART receiver."))
catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.TX", version=vlnv.Version), "uart_TX.xml", "A UART transmitter."))
catalog.AddItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.Wrapper", version=vlnv.Version), "uart_RX.xml", "A UART wrapper."))

print(catalog.ToXml())


# ==============================================================================
component = Component(vlnv, "PoC.io.uart.RX")

print(component.ToXml())


# ==============================================================================
design = Design(vlnv, "SoFPGA")

print(design.ToXml())


# ==============================================================================
designConfiguration = DesignConfiguration(vlnv, "SoFPGA Config")

print(designConfiguration.ToXml())


# ==============================================================================
filePath = Path("test/catalog.xml")
catalog = Catalog.FromFile(filePath)
print(catalog.ToXml())
