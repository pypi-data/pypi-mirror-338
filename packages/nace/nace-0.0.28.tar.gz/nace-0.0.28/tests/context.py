# -*- coding: utf-8 -*-

import sys
import os
# insert the parent directory at the start of the sys path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import modeules here, so they can be re-imported elsewhere in unit tests
import nace

