from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmMMI2x2SH_BB() -> gf.Component:
    """Return cnmMMI2x2SH_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI2x2SH_BB")
    c.add_port(name="o1",center=[0,-4.6],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o2",center=[0,4.6],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o4",center=[214.50600,-4.6],width=1.2,orientation=0,cross_section=shallow)
    c.add_port(name="o3",center=[214.50600,4.6],width=1.2,orientation=0,cross_section=shallow)
    return c

if __name__ == "__main__":
    c = cnmMMI2x2SH_BB()
    c.show()