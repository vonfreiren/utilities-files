from PIL import Image
import os, sys
import glob
from delete_movies_files import delete

filetype="jpeg"
filetype2="webp"

path = "/Users/mariajosealvarez/IdeaProjects/vonfreiren.github.io/img/posts"
path = "/Users/mariajosealvarez/IdeaProjects/vonfreiren.github.io/img/posts/nomad"

files = glob.glob(path + '/**/*.jpg', recursive=True)


def resize():
    for item in files:
        try:
            print(item)
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((1920,1220), Image.ANTIALIAS)
            print(item)
            imResize.save(f+'.jpg', 'JPEG', quality=85)
        except:
            print(item+" cannot be saved")
resize()

#delete()


