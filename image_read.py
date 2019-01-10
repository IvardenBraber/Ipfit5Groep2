from __future__ import print_function
import argparse
import os
import pytsk3
import pyewf
import sys
from tabulate import tabulate
import hashlib


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description='Image reader',
    epilog="Developed by {} on {}".format(
    ", ".join('Hoax'), '10-01-2019')
    )

class EWFImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self._ewf_handle = ewf_handle
        super(EWFImgInfo, self).__init__(url="",type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self._ewf_handle.close()

    def read(self, offset, size):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()

def image_read(image, img_type, offset):
    print("[+] Opening {}".format(image))
    if img_type == "ewf":
        try:
            filenames = pyewf.glob(image)
        except IOError:
            _, e, _ = sys.exc_info()
            print("[-] Invalid EWF format:\n {}".format(e))
            sys.exit(2)
        ewf_handle = pyewf.handle()
        ewf_handle.open(filenames)
        # Open PYTSK3 handle on EWF Image
        img_info = EWFImgInfo(ewf_handle)
    else:
        img_info = pytsk3.Img_Info(image)

    try:
        fs = pytsk3.FS_Info(img_info, offset)
    except IOError:
        _, e, _ = sys.exc_info()
        print("[-] Unable to open FS:\n {}".format(e))
        exit()

    root_dir = fs.open_dir(path="/")
    table = [["Name", "Type", "Size", "Create Date", "Modify Date", "Hash Value"]]
    for f in root_dir:
        name = f.info.name.name
        if f.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
            f_type = "DIR"
        else:
            f_type = "FILE"
        size = f.info.meta.size
        create = f.info.meta.crtime
        modify = f.info.meta.mtime
        table.append([name, f_type, size, create, modify])
    print(tabulate(table, headers="firstrow"))



def extension_check(path: str):
    path = path.split('.')
    extension = str(path[1])
    text = 'Wrong datatype'
    if(extension == 'dd'):
        type = 'raw'
    elif(extension == 'E01'):
        type = 'ewf'
    else:
        return text
    return(type)




def main():
    #path = 'D:\Files\Jaar 2\IPFIT5\Code\Ipfit5Groep2\image.dd'
    path = 'D:\Files\Jaar 2\IPFIT5\Code\Ipfit5Groep2\image_sd_pi.E01'
    #4194304
    image_type = extension_check(path)
    image_read(path,image_type,4194304)

main()