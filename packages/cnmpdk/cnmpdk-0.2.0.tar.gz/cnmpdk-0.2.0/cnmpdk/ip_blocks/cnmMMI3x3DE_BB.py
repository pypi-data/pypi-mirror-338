from __future__ import annotations
import gdsfactory as gf
from cnmpdk.config import PATH
from cnmpdk.tech import *

@gf.cell
def cnmMMI3x3DE_BB() -> gf.Component:
    """Return cnmMMI3x3DE_BB fixed cell."""
    c = gf.Component()
    c = gf.import_gds(PATH.library_path, "cnmMMI3x3DE_BB")
    c.add_port(name="o1",center=[0,-5.65],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o2",center=[0,0],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o3",center=[0,5.65],width=1.2,orientation=180,cross_section=deep)
    c.add_port(name="o6",center=[210.47700,-5.65],width=1.2,orientation=0,cross_section=deep)
    c.add_port(name="o5",center=[210.47700,0],width=1.2,orientation=0,cross_section=deep)
    c.add_port(name="o4",center=[210.47700,5.65],width=1.2,orientation=0,cross_section=deep)
    return c

if __name__ == "__main__":
    c = cnmMMI3x3DE_BB()
    c.show()