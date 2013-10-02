import json
import maya.cmds as cmds

filename = cmds.fileDialog2(fileMode=1, caption="Import Hmap", fileFilter="*.hmap")
hmap_file = open(filename[0])
hmap = json.load( hmap_file )

imsize = ( len(hmap), len(hmap[0]) )


grid = (100,100)
depth = 50 # Height for when input data has height 1

pixsize = ( imsize[0]/grid[0] , imsize[1]/grid[1] )

for x in range( grid[0] ):
	px = x*pixsize[0]
	for y in range( grid[1] ):
		py = y*pixsize[1]
		z = hmap[ px ][ py ]*depth
	
		c = cmds.polyCube()
		heightScale = max( 1, z )
		cmds.setAttr( c[0]+".t", x, heightScale/2, y)
		cmds.setAttr( c[0]+".sy", heightScale )