from PIL import Image
import os, sys
import glob


def delete():
    import os
    txt_type = ".txt"
    jpg_type = ".jpg"
    srt_type = ".url"
    url_type = ".url"
    nfo_type = ".nfo"
    png_type = ".png"




    dir_name = "/Volumes/My Passport for Mac/Calibre Library/**"
    #dir_name = "/Volumes/My Passport for Mac/Kindle/**"
    #dir_name = "/Volumes/My Passport for Mac/Courses/**"
    dir_name = "/Volumes/My Passport for Mac/Series/**"


    files = glob.glob(dir_name, recursive=True)


    for item in files:
        if item.endswith(txt_type) or item.endswith(jpg_type) or item.endswith(srt_type) or item.endswith(url_type) or item.endswith(nfo_type) or item.endswith(png_type):
            print(item)
            os.remove(os.path.join(dir_name, item))


delete()
