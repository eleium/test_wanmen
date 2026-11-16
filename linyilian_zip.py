import os
import zipfile

source_dir = "/home/elei/test/林忆莲"
target_dir = "/home/elei/test/zip_folder"
os.makedirs(target_dir, exist_ok=True)


def zipf():
    z = zipfile.ZipFile("lyl.zip")
    z.write(os.path.join("source_dir,file"), "w")
