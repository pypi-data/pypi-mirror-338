from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import LAYER
from cnmpdk.tech import *

@gf.cell
def cnmMMI2x2DE_BB() -> gf.Component:
    """Return cnmMMI2x2DE_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI2x2DE_BB")
    c.add_port(name="o1",center=[0,-4.5],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o2",center=[0,4.5],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o4",center=[205.42000,-4.5],width=1.2,orientation=0,cross_section=deep)
    c.add_port(name="o3",center=[205.42000,4.5],width=1.2,orientation=0,cross_section=deep)
    return c

if __name__ == "__main__":
    c = cnmMMI2x2DE_BB()
    c.show()