import glob
import os.path
import yaml
import constants
import shutil

def sort_movies_series():

    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    path = data['dir_name_delete_movies_files']
    path_recursive = path + "/**"

    path_series = path + "/Series"
    path_movies = path + "/Movies"

    files = glob.glob(path_recursive, recursive=True)

    create_directories(path_series, path_movies)

    for item in files:
        try:
            if os.path.isdir(path_movies) or os.path.isdir(path_series):
                print("Directory already exists")

            if os.path.isdir(item):
                if constants.SEASON in item:
                    shutil.move(item, path_series)
                    print("Item moved to Series: " + item)
                else:
                    shutil.move(item, path_movies)
                    print("Item moved to Movies: " + item)
        except:
            print("Item not moved: " + item)



def create_directories(path_series, path_movies):
    if not os.path.exists(path_series):
        os.makedirs(path_series)

    if not os.path.exists(path_movies):
        os.makedirs(path_movies)

sort_movies_series()