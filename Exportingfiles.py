from __future__ import print_function
import argparse
import csv
import hashlib
import os
import pytsk3
import pyewf
import sys
from tqdm import tqdm
import pathlib

object_list = []

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("EVIDENCE_FILE", help="Evidence file path"),
    parser.add_argument("TYPE", help="Type of Evidence", choices=("raw", "ewf")),
    parser.add_argument("HASH_LIST", help="Filepath to Newline-delimited list of hashes (either MD5, SHA1, or SHA-256)"),
    parser.add_argument("-p", help="Partition Type", choices=("DOS", "GPT", "MAC", "SUN")),
    parser.add_argument("-t", type=int, help="Total number of files, for the progress bar"),
    args = parser.parse_args()
    main(args.EVIDENCE_FILE, args.TYPE, args.HASH_LIST, args.p, args.t)

def read_hashes(hashes):
    hash_list = []
    hash_type = None
    with open(hashes) as infile:
        for line in infile:
            if hash_type is None:
                if len(line.strip()) == 32:
                    hash_type = "md5"
            elif len(line.strip()) == 40:
                hash_type == "sha1"
            elif len(line.strip()) == 64:
                hash_type == "sha256"
            hash_list.append(line.strip().lower())
            if hash_type is None:
                print("[-] No valid hashes identified in {}".format(hashes))
                sys.exit(3)
    return hash_list, hash_type

def main(image, img_type, hashes, part_type=None, pbar_total=0):
    hash_list, hash_type = read_hashes(hashes)
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
        # Open PYTSK3 handle on EWF Image
        img_info = EWFImgInfo(ewf_handle)
    else:
        img_info = pytsk3.Img_Info(image)
        try:
            if part_type is not None:
                attr_id = getattr(pytsk3, "TSK_VS_TYPE_" + part_type)
                volume = pytsk3.Volume_Info(img_info, attr_id)
            else:
                volume = pytsk3.Volume_Info(img_info)
        except IOError:
            _, e, _ = sys.exc_info()
            print("[-] Unable to read partition table:\n {}".format(e))
            open_fs(volume, img_info, hash_list, hash_type, pbar_total)

def open_fs(vol, img, hashes, hash_type, pbar_total=0):
    # Open FS and Recurse
    print("[+] Recursing through and hashing files")
    pbar = tqdm(desc="Hashing", unit=" files",
    unit_scale=True, total=pbar_total)
    if vol is not None:
        for part in vol:
            if part.len > 2048 and "Unallocated" not in part.desc and \
                "Extended" not in part.desc and \
                "Primary Table" not in part.desc:
                try:
                    fs = pytsk3.FS_Info(
                    img, offset=part.start * vol.info.block_size)
                except IOError:
                    _, e, _ = sys.exc_info()
                    print("[-] Unable to open FS:\n {}".format(e))
        root = fs.open_dir(path="/")
        recurse_files(part.addr, fs, root, [], [""], hashes,
        hash_type, pbar)
    else:
            try:
                fs = pytsk3.FS_Info(img)
            except IOError:
                _, e, _ = sys.exc_info()
                print("[-] Unable to open FS:\n {}".format(e))
    root = fs.open_dir(path="/")
    recurse_files(1, fs, root, [], [""], hashes, hash_type, pbar)
    pbar.close()

def recurse_files(part, fs, root_dir, dirs, parent, hashes, hash_type, pbar):
 dirs.append(root_dir.info.fs_file.meta.addr)
 for fs_object in root_dir:
 # Skip ".", ".." or directory entries without a name.
    if not hasattr(fs_object, "info") or \
            not hasattr(fs_object.info, "name") or \
            not hasattr(fs_object.info.name, "name") or \
            fs_object.info.name.name in [".", ".."]:
        continue
    try:
        file_path = "{}/{}".format("/".join(parent), fs_object.info.name.name)
        if getattr(fs_object.info.meta, "type", None) == pytsk3.TSK_FS_META_TYPE_DIR:
            parent.append(fs_object.info.name.name)
            sub_directory = fs_object.as_directory()
            inode = fs_object.info.meta.addr
            # This ensures that we don't recurse into a directory
            # above the current level and thus avoid circular loops.
            if inode not in dirs:
                recurse_files(part, fs, sub_directory, dirs,
                parent, hashes, hash_type, pbar)
                parent.pop(-1)
        else:
                hash_file(fs_object, file_path, hashes, hash_type, pbar)
    except IOError:
        pass
        dirs.pop(-1)

def hash_file(fs_object, path, hashes, hash_type, pbar):
    if hash_type == "md5":
        hash_obj = hashlib.md5()
    elif hash_type == "sha1":
        hash_obj = hashlib.sha1()
    elif hash_type == "sha256":
        hash_obj = hashlib.sha256()
    f_size = getattr(fs_object.info.meta, "size", 0)
    pbar.set_postfix(File_Size="{:.2f}MB".format(f_size / 1024.0 / 1024))
    hash_obj.update(fs_object.read_random(0, f_size))
    hash_digest = hash_obj.hexdigest()
    pbar.update()
    if hash_digest in hashes:
        object_list.append(fs_object)
        pbar.write("[*] MATCH: {}\n{}".format(path, hash_digest))


def extension_check(path):
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


def call(evidence_file, hash_list):
    type = extension_check(evidence_file)
    main(evidence_file, type, hash_list)

    # if os.path.exists(evidence_file) and \
    #     os.path.isfile(evidence_file) and \
    #     os.path.exists(hash_list) and \
    #     os.path.isfile(hash_list):
    #
    # else:
    #     print("[-] Supplied input file {} does not exist or is not a "
    #     "file".format(evidence_file))
    #     sys.exit(1)
    return object_list

def extract(path, hash, output):
    object_img = call(path, hash)
    file: object = object_img[0]
    imginfo = pytsk3.Img_Info('C:/Users/calvi/Desktop/image.dd')
    fs = pytsk3.FS_Info(imginfo)
    f = fs.open_meta(inode=file.info.meta.addr)
    offset = 0
    BUFF_SIZE = 1024 * 1024
    size = file.info.meta.size

    while offset < size:
        available_to_read = min(BUFF_SIZE, size - offset)
        data_file = f.read_random(offset, available_to_read)
        if not data_file: break
        offset += len(data_file)

    extractFile = open(output + str(file.info.name.name.decode("UTF-8")), 'wb')
    extractFile.write(data_file)
    extractFile.close()
    return file

if __name__ == '__main__':
    extract('C:/Users/calvi/Desktop/image.dd', 'hash_opslage.txt', 'files/')



