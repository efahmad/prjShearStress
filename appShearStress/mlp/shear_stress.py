import os

import django
import sys

sys.path.append('/home/saef/Documents/projects/prjShearStress')
os.environ['DJANGO_SETTINGS_MODULE'] = 'prjShearStress.settings'
django.setup()