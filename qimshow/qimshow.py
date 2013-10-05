import pylab

def qimshow(A, exit=True):
      pylab.figure()
      pylab.imshow(A)
      pylab.colorbar()
      pylab.show()
      if exit:
            quit()