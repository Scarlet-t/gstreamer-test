the robotics team's cam system is currently windows-only and i have a macbook so this is part of my attempt to port it to mac.  
  

this project has me setting up a gstreamer project, with a requirements.txt file that i can use for the mac port of the cams system.  
  
current setup requires creating a virtual environment. Am using Python3.14. I am sourcing gst and other pygobject modules by installing it into said virtual environment. The PyPI install would be "gstreamer-bundle" (already included in requirements.txt). 

I am unsure if this may work on Linux environments. I will have to investigate that further, eventually, though I can't see why it wouldn't work (With some tweaks), at least with the dependencies I'm currently using.

## MAC/LINUX config differences:
### Video sink:
*refer to https://gstreamer.freedesktop.org/documentation/tutorials/basic/platform-specific-elements.html?gi-language=python for usage info*  
- Mac: osxvideosink
- Linux: ximagesink, xvimagesink
