# increaseVersion
# by Thomas Moore

import maya.cmds as cmds
import pymel.core as pm
import os
from maya import mel
from . import fileUtils
import importlib
importlib.reload(fileUtils)


def versionUp(*args):
    debug = False
    currentFile = cmds.file(location=True, query=True)
    path, file = os.path.split(currentFile)
    basename, ver, ext = file.split('.')
    fileNameSplit = file.split(".")
    curVer = fileNameSplit[-2]
    vCurToken = ''
    if 'v' in curVer:
        vCurToken = 'v'
        curVer = int(curVer.split('v')[1])
    else:
        curVer = int(curVer)
    if debug: print(fileUtils.getLatest(path, basename))
    latestVer = fileUtils.getLatest(path, basename)[0].split('.')[1]
    vToken = ''
    if 'v' in latestVer:
        vToken = 'v'
        latestVer = int(latestVer.split('v')[1])
    else:
        latestVer = int(latestVer)
    if debug: print(latestVer)
    newVerInt = '%03d' % (int(curVer) + 1)
    newVer = newVerInt

    if int(newVer) <= latestVer:
        nextVerInt = '%03d' % (latestVer + 1)
        nextVer = '{0}{1}'.format(vToken, nextVerInt)
        print('new version, {0}, is less than or equal to the latest, {1} \n next version is {2}'.format(int(newVer), latestVer, nextVer))
        newVer = nextVer
    newVer = '{0}{1}'.format(vCurToken, newVerInt)
    newfile = ".".join((fileNameSplit[0], newVer, fileNameSplit[-1]))
    new_file_path = os.path.join(path, newfile)

    # ver_exists = False
    # if os.path.exists(new_file_path):
    #     ver_exists = True
    # if ver_exists:
    #     cmds.error("Next version already exists. Action cancelled. Please save manually.")

    save = cmds.confirmDialog(message="Would you like to save the current file before creating new version?",
                              title="Save file?", button=["Save", "Don't Save", "Cancel"], defaultButton="Save",
                              cancelButton="Cancel")
    if save == "Save":
        print('Saving before versioning up')
        pm.saveFile(force=True)
    elif save =="Cancel":
        print('Cancelling anim publish')
        return None
    else:
        print('Skipping save before versioning')

    pm.saveAs(new_file_path, f=True)


    # that slash replace might not work on mac
    mel.eval('addRecentFile("%s", "mayaAscii")'%(new_file_path.replace("\\","/")))
    return newfile
