class Colors:
	black = (0, 0, 0)
	green = (5, 255, 3)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (254, 253, 3)
	purple = (166, 0, 247)
	cyan = (0, 255, 254)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_gray = (40, 40, 40)
	black = (25, 25, 25)

	@classmethod
	def get_cell_colors(cls):
		return [cls.black, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
