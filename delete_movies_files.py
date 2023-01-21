import glob
import yaml

def delete():
    import os
    txt_type = ".txt"
    jpg_type = ".jpg"
    url_type = ".url"
    nfo_type = ".nfo"
    png_type = ".png"
    jpeg_type = ".jpeg"

    formats_to_be_deleted = [txt_type, jpg_type, url_type, nfo_type, png_type, jpeg_type]


    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    path = data['dir_name_delete_movies_files']
    path = path + "/**"


    files = glob.glob(path, recursive=True)


    for item in files:
        if any(item.endswith(format) for format in formats_to_be_deleted):
            os.remove(os.path.join(path, item))
            print("Removed: " + item)


delete()
