import sys
import json
from PIL import Image
def main():
	""" Convert arg file to our hmap format """
	
	file = sys.argv[1]
	output = file.rsplit(".",1)[0]+".hmap"

	filetype = file.rsplit(".",1)[-1]
	if filetype in ( 'jpg', 'jpeg' ):
		im = Image.open( file )
		pix = im.load()
		size = im.size
		
		l = list()
		for x in range(0,size[0]):
			l.append( [] )
			for y in range(0,size[1]):
				l[x].append( pix[x,y]/255.0 )
		
		f = open( output, "w" )
		json.dump( l, f )

if __name__ == '__main__':
  main()