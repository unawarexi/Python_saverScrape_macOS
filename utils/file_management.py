import json
import os
import plistlib

from routes.paths import ENTRIES_PATH, IDLEASSETSD_PATH, STRINGS_PATH, VIDEO_PATH

def validate_environment() -> None:
    """
    Validate the environment by checking necessary paths and files.
    """
    if not os.path.isdir(IDLEASSETSD_PATH):
        print("Unable to find idleassetsd path.")
        exit()
    if not os.path.isfile(STRINGS_PATH):
        print("Unable to find localizable strings file.")
        exit()
    if not os.path.isfile(ENTRIES_PATH):
        print("Unable to find entries.json file.")
        exit()
    if not os.path.isdir(VIDEO_PATH):
        print("Unable to find video path.")
        exit()

def read_localizable_strings() -> dict:
    """
    Read localizable strings from the specified file.
    """
    with open(STRINGS_PATH, "rb") as fp:
        return plistlib.load(fp)

def read_asset_entries() -> dict:
    """
    Read asset entries from the specified JSON file.
    """
    with open(ENTRIES_PATH) as fp:
        return json.load(fp)

def as_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return -1
