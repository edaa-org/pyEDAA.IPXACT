from pyIPXACT.catalog import Catalog, IpxactFile
from pyIPXACT.common import Vlnv


vlnv = Vlnv("VLSI-EDA", "PoC", "PoC", "1.0")

cat = Catalog(vlnv, "IP Core Library")
cat.AddCatalogItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.RX", version=vlnv.Version), "uart_RX.xml", "A UART receiver."))
cat.AddCatalogItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.TX", version=vlnv.Version), "uart_TX.xml", "A UART transmitter."))
cat.AddCatalogItem(IpxactFile(Vlnv(vendor=vlnv.Vendor, library=vlnv.Library, name="PoC.io.aurt.Wrapper", version=vlnv.Version), "uart_RX.xml", "A UART wrapper."))

print(cat.ToXml())
