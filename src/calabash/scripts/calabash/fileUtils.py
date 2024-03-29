from maya import cmds
import pymel.core as pm
import os
import shutil
#import zipfile
#import datetime
from . import increaseVersion
from . import shading_utils
import importlib
importlib.reload(shading_utils)
import json
import datetime

__all__ = [
    'publishCurrentFile',
    'rename_hatch_rigs',
    #'publish_vray_rig'
]
debug = True

def get_location():

    # Returns a dictionary of paths and names for asset dev

    file_path = pm.system.sceneName()
    assetroot, filename = os.path.split(file_path)
    dept = ('default', assetroot)
    if os.path.split(assetroot)[1] == 'shd':
        shd_path = os.path.dirname(file_path)
        dept = ('shd', shd_path)
        assetroot, throwaway = os.path.split(shd_path)
    if debug: print('file path: {0}\nassetroot: {1}\nfilename: {2}'.format(file_path, assetroot, filename))
    publish_dir = os.path.join(assetroot, 'publish')
    dev_dir = os.path.dirname(assetroot)
    type_dir = os.path.dirname(dev_dir)
    basename, ver, ext = filename.split(".")


    return {'file_path': file_path, 'assetroot_filename': (assetroot, filename), 'publish_dir': publish_dir,
            'dev_dir': dev_dir, 'type_dir': type_dir, 'basename_ver_ext': (basename, ver, ext), 'dept':dept}


def ismultipart(path, basename):
    if os.listdir(path):
        for n in os.listdir(path):
            if basename in n:
                if '-' in n:
                    return True

def getLatest(path, basename, **kwargs):
    debug = False
    #if debug: print "path: {0}, basename: {1} kwargs: {2}".format(path, basename, kwargs)
    filename = False
    integer = False
    stage = ''
    parts = False
    none_return = False
    for kwarg, value in list(kwargs.items()):

        if kwarg == 'filename':
            filename = value
        elif kwarg == 'integer':
            integer = value
        elif kwarg == 'stage':
            stage = value
        elif kwarg == 'parts':
            parts = value
        elif kwarg == 'none_return':
            none_return = value

    #versions_num = []
    versions_name = []
    parts_list = []
    def getParts():
        if os.path.exists(path):
            if debug: print("listdir: {0}".format(os.listdir(path)))
            if os.listdir(path):
                for n in os.listdir(path):
                    if not 'Smedge' in n:
                        if basename in n:
                            if debug: print('basename:', basename)
                            try:
                                basename_full, ver, ext = n.split('.')
                                # basename = spot_shot
                                #basename_full = spot_shot-<optionalPart>_stage
                                if stage:

                                    if stage in basename_full:
                                        if not basename_full in parts_list:
                                            if debug: print(basename_full)
                                            parts_list.append(basename_full)
                                else:
                                    if not basename_full in parts_list:
                                        if debug: print(basename_full)
                                        parts_list.append(basename_full)
                            except:
                                pass

    def latest(basename_part):
        versions = []
        if os.path.exists(path):
            #if debug: print "listdir: {0}".format(os.listdir(path))
            if os.listdir(path):
                for n in os.listdir(path):
                    if basename_part in n:
                        versions.append(n)
        return sorted(versions)[-1]

    getParts()
    for part in parts_list:
        versions_name.append(latest(part))

    #if debug: print "versions_num: {0}".format(versions_num)
    if debug: print("versions_name: {0}".format(versions_name))

    return versions_name

def changelog(assetroot, version, comment):
    log = os.path.join(assetroot, 'changelog.json')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subname, ver, ext = version.split('.')
    if not os.path.exists(log):
        with open(log, 'w') as log_init:
            log_body = {}
            json.dump(log_body, log_init)

    log_entry = [timestamp,comment]
    with open(log, 'r') as log_read:
        log_body = json.load(log_read)
    with open(log, 'w') as log_write:
        try:
            log_body[subname][version].append(log_entry)
        except KeyError:
            try:
                log_body[subname][version] = [log_entry]
            except KeyError:
                log_body[subname] = {version:[log_entry]}

        # if not subname in log_body:
        #     log_body[subname] = [log_entry]
        # else:
        #     log_body[subname].append(log_entry)
        json.dump(log_body, log_write)

def publishCurrentFile():


    debug = False  # False to disable variable printout

    file_path = pm.sceneName()
    filename = file_path.split('/')[-1]
    assetroot = os.path.dirname(file_path)
    type_dir = os.path.dirname(assetroot)
    publish_dir = os.path.join(assetroot, 'publish')
    dept = filename.split('.')[0].split('_')[-1]
    basename, ver, ext = filename.split('.')


    sel = pm.ls(sl=True)

    if not sel:
        return

    if debug:

        print('assetroot', assetroot)
        print('publish_dir', publish_dir)
        print('filename', filename)
        print('Type_dir', type_dir)
        print('basename: {0}, ver: {1} ext: {2}'.format(basename, ver, ext))
        print('dept:', dept)


    # Cleanup unknown nodes
    if pm.ls(type='unknown'):
        print('Unknown Nodes found, cleaning up...')
        # Source cleanUpScene.mel
        # to make scOpt_performOneCleanup available
        pm.mel.source('cleanUpScene')

        pm.mel.scOpt_performOneCleanup({
            'unknownNodesOption'
        }
        )
    else:
        print('No Unknown Nodes found...')


    # If in shd scene: define mtl export params, version up, import refs with namespaces,
    # export materials, remove namespaces, export shaded rig, reload current scene to restore references




    result = pm.promptDialog(
        title = 'Leave a comment',
        message = '         What did you do?            ',
        button = ['OK'],
        defaultButton = 'OK',
    )

    comment = pm.promptDialog(query=True, text=True)

    pm.saveFile(f=True)
    if dept == 'shd':
        basename = basename.replace('_shd', '')
        mtl_filename = '{0}_mtl.{1}.mb'.format(basename, ver)
        print('#############')
        print('export mtl')
        mtl_export_path = os.path.join(publish_dir, mtl_filename)


        for node in sel:
            if pm.referenceQuery(node, inr=True):
                refNode = pm.referenceQuery(node, rfn=True)
                fileRef = pm.FileReference(refnode=refNode)
                fileRef.importContents(removeNamespace=True)
        pm.select(sel)
        shading_utils.publish_mtl(mtl_export_path)
        print('#############')
        pm.select(sel)
        # for node in sel:
        #     ns, obj = node.split(':')
        #     pm.namespace(rm=str(ns), mnr=True)

        exp_ma = pm.exportSelected(os.path.join(publish_dir, filename),
                                   constructionHistory=True,
                                   channels=True,
                                   constraints=True,
                                   expressions=True,
                                   shader=True,
                                   preserveReferences=True,
                                   type='mayaBinary'
                                   )
        print("Exported: %s" % (exp_ma))
        revert_path = cmds.file(sceneName=True, q=True)
        print('Reverting: ', pm.system.openFile(revert_path, force=True))
    else:

        for asset in sel:
            ref_nodes = set()
            children = pm.listRelatives(asset, ad=True)
            for child in children:
                if pm.reference(child, isNodeReferenced=True):
                    ref_node = pm.referenceQuery(child, rfn=True)
                    ref_nodes.add(ref_node)
            ref_nodes = list(ref_nodes)
            for node in ref_nodes:
                ref_file = pm.FileReference(refnode=node)
                ref_file.importContents(removeNamespace=True)
        pm.select(sel)
        exp_ma = pm.exportSelected(os.path.join(publish_dir, filename),
                                   constructionHistory=True,
                                   channels=True,
                                   constraints=True,
                                   expressions=True,
                                   shader=True,
                                   preserveReferences=True,
                                   type='mayaBinary'
                                   )
        print(("Exported: %s" % (exp_ma)))
        revert_path = cmds.file(sceneName=True, q=True)
        print('Reverting: ', pm.system.openFile(revert_path, force=True))


    changelog(assetroot, filename.replace('.ma', '.mb'), comment)

    #
    # #shutil.copy2(exp_ma, os.path.join(nonvray_dir,non_ver))
    # shutil.copy2(exp_mb, os.path.join(nonvray_dir,non_ver_mb))


def rename_hatch_rigs():
    if cmds.objExists("|Group|Main"):
        cmds.rename("|Group|Main", "Character")

    if cmds.objExists("|Group"):
        cmds.rename("|Group", "World")


# def publish_vray_rig():
#     file_path = cmds.file(sceneName=True, q=True)
#
#     if cmds.file(modified=True, q=True):
#         save = cmds.confirmDialog(title="Scene Unsaved",
#                                   message="Save scene before publishing",
#                                   button=["Save", "Cancel"],
#                                   defaultButton="Save",
#                                   cancelButton="Cancel",
#                                   dismissString="Cancel")
#         if save == "Save":
#             saved_file = pm.saveFile()
#             print("Scene saved")
#         else:
#             cmds.warning("Action canceled")
#             return
#
#     fdir, filename = os.path.split(file_path)
#     rig_dir = os.path.dirname(fdir)
#     asset_dir = os.path.dirname(rig_dir)
#     dev_dir = os.path.dirname(asset_dir)
#     characters_dir = os.path.dirname(dev_dir)
#     # rig, character, dev, "Characters"
#     basename, ver, ext = filename.split(".")
#
#     non_ver = ".".join((basename, ext))
#     non_ver_mb = ".".join((basename, "mb"))
#
#     version_dir = os.path.join(rig_dir, "publish")
#
#     vray_dir = os.path.join(characters_dir, "vray")
#
#     sel = pm.ls(sl=True)
#
#     if not sel:
#         cmds.warning("Nothing selected")
#         return
#     reference = False
#     for s in sel:
#         try:
#             ref_node = pm.referenceQuery(s, referenceNode=True)
#             ref_scene = pm.referenceQuery(s, filename=True, shortName=True)
#             pm.FileReference(ref_node).importContents(removeNamespace=True)
#             rbasename = ref_scene.split(".")[0]
#             reference = True
#             break
#         except:
#             continue
#
#     if not reference:
#         cmds.error("Reference not found")
#         return
#
#     pm.select(sel)
#     #exp_ma = pm.exportSelected(os.path.join(version_dir, filename), type="mayaAscii", constructionHistory=True, f=True)
#     exp_mb = pm.exportSelected(os.path.join(version_dir, filename), type="mayaBinary",
#                                constructionHistory=True,
#                                channels=True,
#                                constraints=True,
#                                expressions=True,
#                                shader=True,
#                                preserveReferences=True,
#                                )
#     print ("Exported: %s" % (exp_mb))
#     #path, file = os.path.split(exp_ma)
#     #file, ext = os.path.splitext(file)
#     #shutil.copy2(exp_ma, os.path.join(vray_dir,rbasename + ".ma"))
#     print vray_dir
#     shutil.copy2(exp_mb, os.path.join(vray_dir,rbasename + ".mb"))
#
#     pm.newFile(f=True)

def publish_groom_rig():
    file_path = cmds.file(sceneName=True, q=True)

    if cmds.file(modified=True, q=True):
        save = cmds.confirmDialog(title="Scene Unsaved",
                                  message="Save scene before publishing",
                                  button=["Save", "Cancel"],
                                  defaultButton="Save",
                                  cancelButton="Cancel",
                                  dismissString="Cancel")
        if save == "Save":
            saved_file = pm.saveFile()
            print("Scene saved")
        else:
            cmds.warning("Action canceled")
            return

    fdir, filename = os.path.split(file_path)
    rig_dir = os.path.dirname(fdir)
    asset_dir = os.path.dirname(rig_dir)
    dev_dir = os.path.dirname(asset_dir)
    characters_dir = os.path.dirname(dev_dir)
    # rig, character, dev, "Characters"
    basename, ver, ext = filename.split(".")

    non_ver = ".".join((basename, ext))
    non_ver_mb = ".".join((basename, "mb"))

    version_dir = os.path.join(rig_dir, "publish")

    groom_dir = os.path.join(characters_dir, "groom")

    sel = pm.ls(sl=True)

    if not sel:
        cmds.warning("Nothing selected")
        return
    reference = False
    for s in sel:
        try:
            ref_node = pm.referenceQuery(s, referenceNode=True)
            ref_scene = pm.referenceQuery(s, filename=True, shortName=True)
            pm.FileReference(ref_node).importContents(removeNamespace=True)
            rbasename = ref_scene.split(".")[0]
            reference = True
            break
        except:
            continue

    if not reference:
        cmds.error("Reference not found")
        return

    pm.select(sel)
    #exp_ma = pm.exportSelected(os.path.join(version_dir, filename), type="mayaAscii", constructionHistory=True, f=True)
    exp_mb = pm.exportSelected(os.path.join(version_dir, filename), type="mayaBinary",
                               constructionHistory=True,
                               channels=True,
                               constraints=True,
                               expressions=True,
                               shader=True,
                               preserveReferences=True,
                               )

    print(("Exported: %s " % (exp_mb)))
    #path, file = os.path.split(exp_ma)
    #file, ext = os.path.splitext(file)
    #shutil.copy2(exp_ma, os.path.join(groom_dir, rbasename + ".ma"))
    shutil.copy2(exp_mb, os.path.join(groom_dir, rbasename + ".mb"))

    pm.newFile(f=True)