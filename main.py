from PIL import Image
import os, sys
import glob
from delete_movies_files import delete

filetype="jpg"
filetype2="webp"

path = "/Users/mariajosealvarez/IdeaProjects/vonfreiren.github.io/img/posts"
files = glob.glob(path + '/**/*.jpg', recursive=True)


def resize():
    for item in files:
        try:
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((1920,1220), Image.ANTIALIAS)
            imResize.save(f+'.jpg', 'JPEG', quality=85)
        except:
            print(item+" cannot be saved")
#resize()

delete()


