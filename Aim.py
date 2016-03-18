from SimpleCV import Camera, Display
import time

cam = Camera(0, {"width": 640, "height": 320})
display = Display()

while not display.isDone():
	cam.getImage().toRGB().colorDistance((0, 0, 255)).binarize(50).save(display)
	time.sleep(0.01)