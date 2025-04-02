NetTracer3D is a python package developed for both 2D and 3D analysis of microscopic images in the .tif file format. It supports generation of 3D networks showing the relationships between objects (or nodes) in three dimensional space, either based on their own proximity or connectivity via connecting objects such as nerves or blood vessels. In addition to these functionalities are several advanced 3D data processing algorithms, such as labeling of branched structures or abstraction of branched structures into networks. Note that nettracer3d uses segmented data, which can be segmented from other softwares such as ImageJ and imported into NetTracer3D, although it does offer its own segmentation via intensity and volumetric thresholding, or random forest machine learning segmentation. NetTracer3D currently has a fully functional GUI. To use the GUI, after installing the nettracer3d package via pip, enter the command 'nettracer3d' in your command prompt:


This gui is built from the PyQt6 package and therefore may not function on dockers or virtual envs that are unable to support PyQt6 displays. More advanced documentation is coming down the line, but for now please see: https://www.youtube.com/watch?v=cRatn5VTWDY
for a video tutorial on using the GUI.

NetTracer3D is free to use/fork for academic/nonprofit use so long as citation is provided, and is available for commercial use at a fee (see license file for information).

NetTracer3D was developed by Liam McLaughlin while working under Dr. Sanjay Jain at Washington University School of Medicine.

-- Version 0.6.4 updates --

1. Fixed bug with tabulated data in top right having a right click window corresponding to the bottom left.

2. Fixed bug when converting communities to nodes that let the same community connect to itself in the new network.

3. Removed attempted trendline fitting from degree distribution

4. Added new feature to skeletonization (and corresponding branch labeler/gennodes)
	Now you can have the program attempt to auto-correct 3D skeletonization loop artifacts through a method that just runs the 3d fill holes algo and then attempts to reskeletonize the output. This worked well in my own testing. 

5. Other minor fixes/improvements