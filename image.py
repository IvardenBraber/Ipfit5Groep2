#!/usr/bin/python
import sys
import pytsk3
import datetime
import pyewf



class ewf_Img_Info(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self._ewf_handle = ewf_handle
        super(ewf_Img_Info, self).__init__(
            url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self._ewf_handle.close()

    def read(self, offset, size):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()


ewf_handle = pyewf.handle()

filenames = pyewf.glob("image_sd_pi.E01")
filenames.open.dir(root)

ewf_handle.open(filenames)

imagehandle = ewf_Img_Info(ewf_handle)

partitionTable = pytsk3.Volume_Info(imagehandle)

for partition in partitionTable:
    print(partition.addr, partition.desc, "%ss(%s)" % (partition.start, partition.start * 512), partition.len)

filesystemObject = pytsk3.FS_Info(imagehandle, offset= 4194304)
fileobject = filesystemObject.open("/$FAT1")
print("File Inode:",fileobject.info.meta.addr)
print("File Name:",fileobject.info.name.name)
print("File Creation Time:",datetime.datetime.fromtimestamp(fileobject.info.meta.crtime).strftime('%Y-%m-%d %H:%M:%S'))
outfile = open('DFIRWizard-output', 'w')
filedata = fileobject.read_random(0,fileobject.info.meta.size)

