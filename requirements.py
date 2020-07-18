import sys
import subprocess
try:
    import numpy as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
try:
    import pandas as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])