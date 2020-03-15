import os
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


os.chdir(os.path.dirname(__file__))
cwd = os.getcwd()

if not os.path.exists(cwd):
    os.mkdir(cwd)

def update():
    repoUrl = "https://github.com/youngstuart/Calabash-Tools/archive/master.zip"

    with urlopen(repoUrl) as repoArchive:
        with ZipFile(BytesIO(repoArchive.read())) as zfile:
            # extract everything and overwrite itself
            zfile.extractall(cwd)
            # If overwriting itself causes maya to crash, only extract src
            # for fileName in zfile.namelist():
            #     if fileName.startswith('Calabash-Tools-master/src'):
            #         zfile.extract(fileName, cwd)
            print(f'Calabash Tools extracted to:{cwd}')

update()

