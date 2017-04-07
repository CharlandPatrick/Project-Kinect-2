from Xlib import X, display
import Xlib.XK
import Xlib.error
import Xlib.ext.xtest

while(True):
    d = display.Display()
    s = d.screen()
    infoX = s.width_in_pixels
    infoY = s.height_in_pixels
    mousePtr = display.Display().screen().root.query_pointer()._data
    print("{0} - {1} - {2} - {3}".format(mousePtr["root_x"],mousePtr["root_y"], infoX, infoY))
