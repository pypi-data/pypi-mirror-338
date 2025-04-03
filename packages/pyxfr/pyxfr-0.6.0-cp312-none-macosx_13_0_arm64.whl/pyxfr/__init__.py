"""pyxfr: the transferase Python API. See help for individual classes.

Transeferase is a system for downloading DNA methylation data from the
MethBase2 database. You can also use it with your own data. If you
want to list the classes available in this Python API, you can do the
following:

  import pyxfr, inspect
  classes = [
      cls for cls, obj in inspect.getmembers(transferase, inspect.isclass)
  ]
  print(classes)
"""

from .pyxfr import *

from .pyxfr_utils import *
