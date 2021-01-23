import subprocess
import os
import PIL
import imghdr
from pathlib import Path

current = Path(os.getcwd())

images_folder = current / website / static / images

def resize_images():
    """Resizes images in the images folder."""

    for files in images_folder.iterdir():
        if files.is_dir():
            for image in files.iterdir():
                img = PIL.Image.open(image)
                if img.size == (6000, 4000)  or img.size == (4000, 6000):
                    target = True
                else:
                    target = False
                if imghdr.test(image) and target:
                    subprocess.run([
                        "magick",
                        "convert",
                        str(image),
                        "-resize",
                        "50%",
                        str(image)
                    ])
                else:
                    print(f"{files} is not an image.")
        else:
            if img.test(files):
                img = PIL.Image.open(files)
                if img.size == (6000, 4000)  or img.size == (4000, 6000):
                    target = True
                else:
                    target = False
                if target:
                    subprocess.run([
                        "magick",
                        "convert",
                        str(files),
                        "-resize",
                        "50%",
                        str(files)
                    ])
            else:
                print(f"{files} is not an image.")
    return None

resize_images()