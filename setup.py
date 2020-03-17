import os
import sys
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

def check_userSetup():
    # check that userSetup.py loads cbtools on startup
    user = os.path.expanduser('~')
    userSetup = os.path.join(user, 'maya', 'scripts', 'userSetup.py')
    startup_code = ["import sys",
                    "sys.path.append('C:\\Users\\guest1\\Desktop\\scratch\\cbtools2\\Calabash-Tools')",
                    "from src import makeMenus",
                    "evalDeferred(makeMenus.makeMenu())",
                    "evalDeferred(makeMenud.cbtools_shelf())",
                    ]
    
    failed = False
    with open(userSetup, 'r') as usFile:
        usRead = usFile.read()
        
        for line in startup_code:
            if not line in usRead:
                failed = True
                usRead = usRead + '\n' + line
    if failed:
        with open(userSetup, 'w') as usFile:
            usWrite = usFile.write(usRead)
            