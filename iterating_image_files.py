from __future__ import print_function
import argparse
import csv
from datetime import datetime
import os
import pytsk3
import pyewf
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description= 'Omschrijving',
    epilog="Developed by {} on {}".format(
    ", ".join('HOAX'), '13-01-2018')
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


def iterate_image(image, img_type, output, part_type):
    volume = None
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
        print(filenames)
        # Open PYTSK3 handle on EWF Image
        img_info = EWFImgInfo(ewf_handle)
    else:
        img_info = pytsk3.Img_Info(image)
        print(img_info)

    try:
        if part_type is not None:
            attr_id = getattr(pytsk3, "TSK_VS_TYPE_" + part_type)
            volume = pytsk3.Volume_Info(img_info, attr_id)
            print(volume)
        else:
            volume = pytsk3.Volume_Info(img_info)
            print(volume)
    except IOError:
        _, e, _ = sys.exc_info()
        print("[-] Unable to read partition table:\n {}".format(e))
    open_fs(volume, img_info, output)

def open_fs(vol, img, output):
    print("[+] Recursing through files..")
    recursed_data = []
    # Open FS and Recurse
    if vol is not None:
        for part in vol:
            print(part.desc)
            if part.len > 2048 and b"Unallocated" not in part.desc and b"Extended" not in part.desc and b"Primary Table" not in part.desc:
                try:
                     fs = pytsk3.FS_Info(
                        img, offset=part.start * vol.info.block_size)
                except IOError:
                    _, e, _ = sys.exc_info()
                    print("[-] Unable to open FS:\n {}".format(e))
                root = fs.open_dir(path="/")
                data = recurse_files(part.addr, fs, root, [], [], [""])
                recursed_data.append(data)
    else:
        try:
            fs = pytsk3.FS_Info(img)
        except IOError:
            _, e, _ = sys.exc_info()
            print("[-] Unable to open FS:\n {}".format(e))
        root = fs.open_dir(path="/")
        data = recurse_files(1, fs, root, [], [], [])
        recursed_data.append(data)
        print(len(data))
    write_csv(recursed_data, output)

def recurse_files(part, fs, root_dir, dirs, data, parent):
    teller = 0
    dirs.append(root_dir.info.fs_file.meta.addr)
    for fs_object in root_dir:
        teller += 1
        # Skip ".", ".." or directory entries without a name.
        if not hasattr(fs_object, "info") or \
                not hasattr(fs_object.info, "name") or \
                not hasattr(fs_object.info.name, "name") or \
                fs_object.info.name.name in [".", ".."]:
            continue
        try:
            file_name = fs_object.info.name.name.decode("utf-8")
            print(file_name)
            file_path = "{}/{}".format(
                "".join(str(parent)), fs_object.info.name.name.decode("utf-8"))
            print(file_path)
            try:
                if fs_object.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
                    f_type = "DIR"
                    file_ext = ""
                else:
                    f_type = "FILE"
                    if "." in file_name:
                        file_ext = file_name.rsplit(".")[-1].lower()
                    else:
                        file_ext = ""
            except AttributeError:
                continue

            size = fs_object.info.meta.size
            create = convert_time(fs_object.info.meta.crtime)
            change = convert_time(fs_object.info.meta.ctime)
            modify = convert_time(fs_object.info.meta.mtime)
            data.append(["PARTITION {}".format(part), file_name, file_ext,
                         f_type, create, change, modify, size, file_path])

            if f_type == "DIR":
                parent.append(fs_object.info.name.name)
                sub_directory = fs_object.as_directory()
                inode = fs_object.info.meta.addr
                # This ensures that we don't recurse into a directory
                # above the current level and thus avoid circular loops.
                if inode not in dirs:
                    recurse_files(part, fs, sub_directory, dirs, data,
                              parent)
                parent.pop(-1)
        except IOError:
            pass
    dirs.pop(-1)
    return data

def convert_time(ts):
    if str(ts) == "0":
        return ""
    return datetime.utcfromtimestamp(ts)

def write_csv(data, output):
    if data == []:
        print("[-] No output results to write")
        sys.exit(3)
    print("[+] Writing output to {}".format(output))
    with open(output, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        headers = ["Partition", "File", "File Ext", "File Type",
               "Create Date", "Modify Date", "Change Date", "Size",
               "File Path"]
        csv_writer.writerow(headers)
        for result_list in data:
            csv_writer.writerows(result_list)


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

def open_iterater_image(path,output_name):
    output_name += '.csv'
    iterate_image(path,extension_check(path),output_name, None)



open_iterater_image('USB_Sjors.E01','hoedje')