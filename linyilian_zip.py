import os
import zipfile

source_dir = "/home/elei/test/林忆莲"
target_dir = "/home/elei/test/linyilian_zipfolder"

os.makedirs(target_dir, exist_ok=True)


def zipf():
    z = zipfile.ZipFile(os.path.join(target_dir, "linyilian.zip"), "w")
    for file in os.listdir(source_dir):
        z.write(os.path.join(source_dir, file), arcname)
    with open("linyilian.txt", "a", encoding="utf-8") as w:
        w.write(file + "\n")
    z.close()


zipf()
