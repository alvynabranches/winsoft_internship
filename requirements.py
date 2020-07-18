import sys
import subprocess
try:
    import numpy as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'numpy'])
finally:
    print('Numpy is installed')
try:
    import pandas as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'pandas'])
finally:
    print('Pandas is installed')
try:
    import matplotlib as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'matplotlib'])
finally:
    print('Matplotlib is installed')
try:
    import seaborn as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'seaborn'])
finally:
    print('Seaborn is installed')
try:
    import plotly as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'plotly'])
finally:
    print('Plotly is installed')
try:
    import dash as _
except Exception as e:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--user', 'dash'])
finally:
    print('Dash is installed')