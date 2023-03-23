import os
from pathlib import Path


def register_data_extractors():
    src_root = Path(__file__).resolve().parent.parent

    for submodule in [
        x
        for x in os.listdir(os.path.join(src_root, "data_extractors"))
        if "." not in x and not x.startswith("_")
    ]:
        exec(f"from data_extractors import {submodule}")
