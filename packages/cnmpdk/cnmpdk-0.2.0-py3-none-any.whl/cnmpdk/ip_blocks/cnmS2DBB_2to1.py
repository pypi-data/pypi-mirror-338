from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmS2DBB_2to1() -> gf.Component:
    """Return cnmS2DBB_2to1 fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmS2DBB_2to1")
    c.add_port(name="o1",center=[0,0],width=2.2,orientation=180,cross_section=shallow)
    c.add_port(name="o2",center=[73,0],width=1.2,orientation=0,cross_section=deep)
    return c

if __name__ == "__main__":
    c = cnmS2DBB_2to1()
    c.show()