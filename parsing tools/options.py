import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "DataSets")
SLICED_DIR = os.path.join(DATA_DIR, "Sliced")
RAW_DATA_DIR = os.path.join(DATA_DIR, "Raw")
RAW_SUBT_DIR = os.path.join(DATA_DIR, "Raw_subtitles")
RESULTS_DIR = os.path.join(DATA_DIR, "Results")
SUBS_FORMAT = r"subs"
MY_SUB_DIR = os.path.join(DATA_DIR, "my_subtitles")
MY_MUSIC_DIR = os.path.join(DATA_DIR, "m")
IMAGE_DIR = os.path.join(DATA_DIR, "IMAGE_DIR")


SLICE_TIME = 2 # seconds
PARSE_ALL = True
SAMPLE_RATE = 48000






















#
