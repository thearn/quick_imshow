
quick_imshow
=======================
Python code to quickly display an image with a colorscale using matplotlib.
Meant to help quickly debug image processing applications.

the `qimshow(A)` function provided here is a one-line alias for:

```python
import pylab
pylab.imshow(A)
pylab.colorbar()
pylab.show()
quit()
```

I found myself writing this sequence of statements often enough for debugging
image processing code (such as [stl_tools](https://github.com/thearn/stl_tools)) that I put this short script together.

# Usage

```python
from qimshow import qimshow

# test image
from scipy.misc import lena
A = lena()

qimshow(A) # displays image with color scale info, then quits
```

