from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmMMI3x3SH_BB() -> gf.Component:
    """Return cnmMMI3x3SH_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI3x3SH_BB")
    c.add_port(name="o1",center=[0,-6.65],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o2",center=[0,0],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o3",center=[0,6.65],width=1.2,orientation=180,cross_section=shallow)
    c.add_port(name="o6",center=[315.26100,-6.65],width=1.2,orientation=0,cross_section=shallow)
    c.add_port(name="o5",center=[315.26100,0],width=1.2,orientation=0,cross_section=shallow)
    c.add_port(name="o4",center=[315.26100,6.65],width=1.2,orientation=0,cross_section=shallow)
    return c

if __name__ == "__main__":
    c = cnmMMI3x3SH_BB()
    c.show()