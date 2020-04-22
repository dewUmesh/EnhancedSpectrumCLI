

# find the type of compression used (tgz or zip)
# create a dummy folder
# extract the first layer of compression
# create list of files to be backed up.
# create  a directory if not exist and move the existing artifacts in a dated folder. including .rls file
# finally install patch

import os
import shutil
import tarfile
import zipfile

def filereplace():
    for d,r,f in os.walk("t1/server"):
        # print(d,r,f)
        for file in f:
            fp = os.path.join(d,file)
            print(fp)

def extract():

    for d,r,f in os.walk("t1"):
        # print(d,r,f)
        for file in f:
            fp = os.path.join(d,file)
            if fp.endswith(".rls") or fp.endswith(".jar"):
                break

            print(fp)
            if tarfile.is_tarfile(fp):
                print("it is tar file \n")
                def comman():
                    tar.extractall(d)
                    tar.close()
                    os.remove(fp)
                    extract()

                if fp.endswith("tar.gz"):
                    # print(fp)
                    tar = tarfile.open(fp,'r:gz')
                    comman()
                elif fp.endswith("tar"):
                    tar = tarfile.open(fp,'r:')
                    comman()
            elif zipfile.is_zipfile(fp):
                print("it is zip file \n")
                zip = zipfile.ZipFile(fp)
                # print(zip.infolist())
                zip.extractall(d)
                zip.close()
                os.remove(fp)
                extract()

def compressionType():

    f = "cdq20191s09_Linux_Unix.zip"

    if os.path.exists("t1"):
        shutil.rmtree("t1/")

    os.mkdir("t1")
    fp = shutil.copy2(f,"t1/")

    extract()
    filereplace()

def main():
    compressionType()

if __name__ == '__main__':
    main()

