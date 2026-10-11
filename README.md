The robotics team's camera system is currently windows-only. I have a macbook and am sick of using vms. This is a small step in my attempt to port it to mac.  

This test project uses gstreamer and pyqt6. Documentation for gstreamer on python is scarce. Once again, I am apart from c++ (my beloved).
  
My setup uses a virtual environment. Am using Python3.14. Requirements.txt is included. 

I am unsure if this would work on Linux environments. I may look into that eventually. It *should* work with some tweaks to the sink/source configs, I think.

## MAC/LINUX config differences:
### Video sink:
*refer to https://gstreamer.freedesktop.org/documentation/tutorials/basic/platform-specific-elements.html?gi-language=python for usage info*  
- Mac: osxvideosink
- Linux: ximagesink, xvimagesink
