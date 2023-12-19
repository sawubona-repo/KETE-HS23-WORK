# -*- coding: utf-8 -*-
"""JUPYTER_Tutorial-2_Plotting_with_matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ngW5iLVmOnW8369wVAsB_vzm9Ck7gRUJ

# COLAB TUTORIAL 2: Plotting with **matplotlib**  


### What is Matplotlib?

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

+ Create publication quality plots
+ Make interactive figures that can zoom, pan, update
+ Customize visual style and layout
+ Export to many file formats
+ Embed in JupyterLab and Graphical User Interfaces
+ Use a rich array of third-party packages built on Matplotlib


Matplotlib was created by **John D. Hunter** in 2003.  

Matplotlib is open source and can be used freely. The library is mostly written in python, a few segments are written in C, Objective-C and Javascript for platform compatibility.

Source/Links:
+ [Matplotlib](https://matplotlib.org/)  
+ [Gallery/Examples](https://matplotlib.org/stable/gallery/index)


History:
+ Nov'2023 v1 dbe -- adapted for KETE HS23 (using the Python repl *Tutorial1-Plotting_main.py*)  

---
"""

import matplotlib.pyplot as plt
import numpy as np

"""### Sample Plot - Slide#12"""

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.show()

"""### Sample Plot - Slide#13"""

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2])
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.show()

"""### Sample Plot - Slide#14"""

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], 'ro')
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.show()

"""### Sample Plot - Slide#15"""

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], '-', linewidth=3.0)
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.show()

"""### Sample Plot - Slide#16"""

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], '-', linewidth=3.0)
plt.axis([0, 10, 0, 60])
plt.xticks([0, 5, 10])
plt.yticks([0, 25, 50, 60])
plt.ylabel('some numbers')
plt.xlabel('A meaningless axis')
plt.show()

"""### Sample Plot - Slide#19"""

# evenly sampled values t at 200ms time intervals
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'rx', t, t**2, 'b*', t, t**3, 'go')
plt.ylabel('measured values')
plt.xlabel('time (s)')
plt.show()

"""### Sample Plot - Slide#21"""

# evenly sampled values t at 200ms time intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r-', t, t**2, 'b*', t, t**3, 'go')

plt.ylabel('measured values')
plt.xlabel('time (s)')
plt.title('An example graph')
plt.text(0.25,
           90,
           'This is a cool graph!',
           color='r',
           fontsize=15,
           fontstyle='italic')

plt.show()

"""### Sample Plot - Slide#23"""

# evenly sampled values t at 200ms time intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'r-', linewidth=2.0, label='Thing 1')
lines = plt.plot(t, t**2, 'b*', linewidth=2.0, label='Thing 2')
lines = plt.plot(t, t**3, 'go', linewidth=2.0, label='Thing 3')

plt.title('An example graph - with legends')
plt.ylabel('measured values')
plt.xlabel('time (s)')
plt.legend(loc='upper left')
plt.show()

"""### Sample Plot - Slide#24"""

# evenly sampled values t at 200ms time intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'r-', linewidth=2.0, label='Thing 1')
lines = plt.plot(t, t**2, 'b*', linewidth=2.0, label='Thing 2')
lines = plt.plot(t, t**3, 'go', linewidth=2.0, label='Thing 3')

plt.title('An example graph - with legends')
plt.ylabel('measured values')
plt.xlabel('time (s)')
plt.legend(loc='upper left')
plt.savefig('test.png')
plt.show()