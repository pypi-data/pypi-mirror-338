from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmD2SBB_1to3() -> gf.Component:
    """Return cnmD2SBB_1to3 fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmD2SBB_1to3")
    c.add_port(name="o1",center=[0,0],orientation=180,cross_section=deep)
    c.add_port(name="o2",center=[83,0],width=3.2,orientation=0,cross_section=shallow)
    return c

if __name__ == "__main__":
    c = cnmD2SBB_1to3()
    c.show()