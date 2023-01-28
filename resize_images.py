from PIL import Image
import os
import glob
import yaml



def resize(width=1920, height=1220, quality=90, input_format='jpeg', output_format="JPEG"):
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    path = data['dir_name_resize_images']

    files = glob.glob(path + '/**/*.' + input_format, recursive=True)

    for item in files:
        try:
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((width,height), Image.ANTIALIAS)
            print("Saving image: " + f + "." + output_format)
            imResize.save(f +'.jpg', output_format, quality=quality)
        except:
            print(item+" cannot be saved")



resize(width=1920, height=1220, quality=90, input_format='jpeg', output_format="JPEG")



