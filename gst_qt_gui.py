# refences :
# >>> https://gstreamer.freedesktop.org/documentation/tutorials/basic/concepts.html?gi-language=python 
# >>> https://gstreamer.freedesktop.org/documentation/video/gstvideooverlay.html?gi-language=python
# for GST logic
import sys, gi, cv2

gi.require_version('GLib', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')


from gi.repository import Gst, GstVideo, GLib, GObject
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget 

# ===GSTREAMER===
Gst.init(sys.argv[1:]) #init + read cmd line args

# note that an element in gst may be a source, sink, or filter
source = Gst.ElementFactory.make("avfvideosrc", "source") # "avfvideosrc" is the macbook webcam 
sink = Gst.ElementFactory.make("osxvideosink", "sink") # again, "osxvideosink" is mac-specific

#empty pipeline init
pipeline = Gst.Pipeline.new("voverlay")

if not pipeline or not source or not sink:
    print("error making pipeline, or source/sink element(s)")
    sys.exit(1)

# build pipeline
pipeline.add(source)
pipeline.add(sink)
# link sink to source, error if fail
if not (source.link(sink)):
    print("couldn't link sink to source.")
    sys.exit(1)

# set pattern (for fails i think??? this sets up um how the error bars look)
#source.set_property("pattern", 0)

# (try to) start playig
# === GUI ===
# = video window =
app = QApplication(sys.argv)

videoWindow = QWidget()
videoWindow.resize(1020, 720)
videoWindow.show()
windowId = videoWindow.winId()

# gst integration
GstVideo.VideoOverlay.set_window_handle(sink, int(windowId))
stateReturn = pipeline.set_state(Gst.State.PLAYING)  
# error handling
if stateReturn == Gst.StateChangeReturn.FAILURE:
    print("failed to set pipeline to playing state")
    sys.exit(1)



app.exec()
