from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmMMI8515_BB() -> gf.Component:
    """Return cnmMMI8515_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI8515_BB")
    c.add_port(name="o1",center=[0,-3.9],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o2",center=[0,3.9],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o4",center=[119.67400,-3.9],width=1.2,orientation=0,cross_section=deep)
    c.add_port(name="o3",center=[119.67400,3.9],width=1.2,orientation=0,cross_section=deep)
    return c

if __name__ == "__main__":
    c = cnmMMI8515_BB()
    c.show()