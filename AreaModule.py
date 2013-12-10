class Area:
	
	def __init__(self, name, short_desc, long_desc, north, east, south, west, inside_desc = None):
		#The name of the area
		self.name = name
		self.short_desc = short_desc
		self.long_desc = long_desc
		self.inside_desc = inside_desc
		self.exits = dict({"north":north,"east":east,"south":south,"west":west})