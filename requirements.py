import sys
import subprocess
try:
    import numpy as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'numpy'])
try:
    import pandas as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'pandas'])
try:
    import matplotlib as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'matplotlib'])
try:
    import seaborn as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'seaborn'])
try:
    import plotly as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'plotly'])