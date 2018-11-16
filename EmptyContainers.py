#
#Filter by Ed0
#v1.0
#Any bug or idea contact me via https://twitter.com/el_Ed0_
#

import mcplatform
from pymclevel.materials import alphaMaterials
from pymclevel import TAG_Short
from pymclevel import TAG_List
from pymclevel import TileEntity

displayName = "Empty containers"


chestId = 54
trappedId = 146
hopperId = 154
dropperId = 158
dispenserId = 23
furnaceId = 61
litFurnaceId = 62
beaconId = 138
shulkerId = 219

chestCartId = 'MinecartChest'
hopperCartId = 'MinecartHopper'

inputs = (
	("Chests", True),
	("Trapped chests", True),
	("Hoppers", True),
	("Droppers", True),
	("Dispensers", True),
	("Furnaces", True),
	("Shulker box", True),
	("Minecart with Chest", False),
	("Minecart with Hopper", False),
)
	
def perform(level, box, options):
	chest = options["Chests"]
	trapped = options["Trapped chests"]
	hopper = options["Hoppers"]
	dropper = options["Droppers"]
	dispenser = options["Dispensers"]
	furnace = options["Furnaces"]
	shulker = options["Shulker box"]
	chestCart = options["Minecart with Chest"]
	hopperCart = options["Minecart with Hopper"]
	
	ids = []
	eids = []
	
	if chest:
		ids.append(chestId)
	if trapped:
		ids.append(trappedId)
	if hopper:
		ids.append(hopperId)
	if dropper:
		ids.append(dropperId)
	if dispenser:
		ids.append(dispenserId)
	if furnace:
		ids.append(furnaceId)
		ids.append(litFurnaceId)
	if shulker:
		ids.append(shulkerId)
		
	if chestCart:
		eids.append(chestCartId)
	if hopperCart:
		eids.append(hopperCartId)
	
	for (chunk, slices, point) in level.getChunkSlices(box):
		
		#TileEntities
		if chest or trapped or hopper or dropper or dispenser or furnace or shulker:
			for tile in chunk.TileEntities:
				x = int(tile["x"].value)
				y = int(tile["y"].value)
				z = int(tile["z"].value)

				if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				
					block = level.blockAt(x,y,z)
				
					if block in ids:
						del tile["Items"]

					chunk.dirty = True
		
		#Entities
		if chestCart or hopperCart:
			for e in chunk.Entities:
				x = e["Pos"][0].value
				y = e["Pos"][1].value
				z = e["Pos"][2].value

				if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				
					id = e["id"].value
				
					if id in eids:
						del e["Items"]
					
					chunk.dirty = True