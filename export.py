from pathlib import Path
from subprocess import run
from typing import Dict

import yaml

from main import data_dir, load_csv

output_dir = Path("output/")

tmpfile = output_dir / "tmp.wav"

with open("choices.yaml") as f:
    choices: Dict[int, int] = yaml.safe_load(f)

files = []

for id, text in load_csv().items():
    file_dir = data_dir / str(id)
    if id in choices:
        chosen_num = choices[id]
    else:
        chosen_num = 0
    chosen_file = file_dir / f"{chosen_num}.wav"
    if id == 0:
        chosen_file = Path("tmp/Aperture Science Intro (60fps)-8tIfC2aeuL8.f251.wav")
    if id == 200:
        chosen_file = Path("tmp/Turret_turret_disabled_4.wav")
    if not chosen_file.exists():
        print(chosen_file, "is missing")
        break
    output_file = output_dir / f"{id}.ogg"
    run([
        "ffmpeg",
        "-i", str(chosen_file),
        "-filter:a", "loudnorm=I=-14:LRA=1:dual_mono=true:tp=-1",
        str(tmpfile)
    ])
    run([
        "oggenc",
        str(tmpfile),
        "--output", str(output_file),
        "--bitrate", str(100),
        "--resample", str(16000)
    ])
    tmpfile.unlink()
    files.append(output_file.name)


run([
    "tar", "-c", "-f", "../voice_pack.tar.gz", *files
], cwd="output")
