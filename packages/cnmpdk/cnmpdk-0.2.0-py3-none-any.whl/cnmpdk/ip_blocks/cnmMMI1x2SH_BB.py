from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmMMI1x2SH_BB() -> gf.Component:
    """Return cnmMMI1x2SH_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI1x2SH_BB")
    c.add_port(name="o1",center=[0,0],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o3",center=[91.48900,-4.65],width=1.2,orientation=0,cross_section=shallow)
    c.add_port(name="o2",center=[91.48900,4.65],width=1.2,orientation=0,cross_section=shallow)
    return c

if __name__ == "__main__":
    c = cnmMMI1x2SH_BB()
    c.show()