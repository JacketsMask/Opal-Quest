#Created by the anonymous hacker group "We Love Jake"
import os
import sys
import pickle
from AreaModule import Area

if __name__ == "__main__":
	numArgs = len(sys.argv)
	subdir = "areas"
	i = 1
	while i < numArgs:
		if sys.argv[i] != "None":
			name = sys.argv[i]
		else:
			name = None
		i += 1
		if sys.argv[i] != "None":
			short_desc = sys.argv[i]
		else:
			short_desc = None
		i += 1
		if sys.argv[i] != "None":
			long_desc = sys.argv[i]
		else:
			long_desc = None
		i += 1
		if sys.argv[i] != "None":
			north = sys.argv[i]
		else:
			north = None
		i += 1
		if sys.argv[i] != "None":
			east = sys.argv[i]
		else:
			east = None
		i += 1
		if sys.argv[i] != "None":
			south = sys.argv[i]
		else:
			south = None
		i += 1
		if sys.argv[i] != "None":
			west = sys.argv[i]
		else:
			west = None
		i += 1
		if sys.argv[i] != "None":
			inside_desc = sys.argv[i]
		else:
			inside_desc = None
		i += 1
		area = Area(name, short_desc, long_desc, north, east, south, west, inside_desc)
		pickle.dump(area, open(os.path.join(subdir, name) + ".area","wb"))