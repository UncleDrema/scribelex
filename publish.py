import os
import shutil
import subprocess
import time

# Clear the dist folder
dist_folder = 'dist'
if os.path.exists(dist_folder):
    shutil.rmtree(dist_folder)

# Build the distribution files
subprocess.run(['python', './setup.py', 'sdist', 'bdist_wheel'])

time.sleep(2)

# Upload the distribution files to PyPI using twine
subprocess.run(['python', '-m', 'twine', 'upload', 'dist/*'])