#!/usr/bin/env python3
from PIL import Image
import os

dir = "images/"
output_dir = "/opt/icons/"

for filename in os.listdir(dir):
    if filename != ".DS_Store":
        im = Image.open(os.path.join(dir, filename))
        im = im.rotate(-90)
        im = im.resize(128, 128)
        im = im.convert("RGB")
        im.save(os.path.join(output_dir.filename+".jpeg"))