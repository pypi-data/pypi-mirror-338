from __future__ import annotations

import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk, constants


from cnmpdk import pcells
from cnmpdk import ip_blocks

from cnmpdk.config import PATH
from cnmpdk.tech import LAYER, cnm_cross_sections, get_layer_stack_cnmpdk
from cnmpdk.tech import deep, trench, heater, shallow
from functools import partial
from gdsfactory.technology import LayerView, LayerViews
from cnmpdk.materials import cnm_materials_index

cells = get_cells([pcells,ip_blocks])

PDK = Pdk(
    name="cnmpdk",
    cells=cells,
    cross_sections= cnm_cross_sections,
    layers=LAYER,
    layer_stack=get_layer_stack_cnmpdk(),
    # materials_index = cnm_materials_index,
    constants=constants,
)

PDK.activate()

if __name__ == "__main__":
    print(PDK.name)