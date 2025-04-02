import gdsfactory as gf
from cnmpdk.tech import *

@gf.cell
def cnm_die_10x5(
    size = (10000.0, 5000.0),
) -> gf.Component:
    c = gf.Component()

    size = (10000.0, 5000.0)
    dicing_lane_width = 125.0

    die = c << gf.components.rectangle(size=size, layer=LAYER.DICING_LINES)
    # die = c << gf.components.rectangle(size=size, layer=LAYER.DICING_LINES)

    return c


if __name__ == "__main__":
    c = cnm_die_10x5()
    c.show()