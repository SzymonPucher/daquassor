import os
from pathlib import Path


def register_data_extractors():
    data_extractors_folder = Path(__file__).resolve().parent

    for submodule in [
        folder
        for folder in os.listdir(data_extractors_folder)
        if "." not in folder and not folder.startswith("_")
    ]:
        exec(f"from data_extractors import {submodule}")
