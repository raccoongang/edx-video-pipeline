#!/usr/bin/env python
"""
VEDA Environment variables

"""

import os
import sys
import django
from django.utils.timezone import utc
from django.db import reset_queries

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_path not in sys.path:
    sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VEDA.settings.local')

django.setup()

from VEDA_OS01.models import Institution
from VEDA_OS01.models import Course
from VEDA_OS01.models import Video
from VEDA_OS01.models import Destination
from VEDA_OS01.models import Encode
from VEDA_OS01.models import URL
from VEDA_OS01.models import VedaUpload

"""
Central Config
"""
DELIVER_WORK_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'veda_temp_deliver_data'
)
INGEST_WORK_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'veda_temp_ingest_data'
)

if not os.path.exists(DELIVER_WORK_DIR):
    os.mkdir(DELIVER_WORK_DIR)

if not os.path.exists(INGEST_WORK_DIR):
    os.mkdir(INGEST_WORK_DIR)

"""
Occasionally this throws an error in the env,
but on EC2 with v_videocompile it's no biggie

"""
FFPROBE = "ffprobe"
FFMPEG = "ffmpeg"

"""
Generalized display and such

"""

"""
TERM COLORS
"""
NODE_COLORS_BLUE = '\033[94m'
NODE_COLORS_GREEN = '\033[92m'
NODE_COLORS_RED = '\033[91m'
NODE_COLORS_END = '\033[0m'
