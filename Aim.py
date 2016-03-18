from SimpleCV import Camera, Display

cam = Camera(0, {"width": 640, "height": 360})
display = Display()

while True:
	img = cam.getImage().show()