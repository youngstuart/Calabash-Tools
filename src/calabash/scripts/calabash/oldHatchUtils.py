from maya import cmds
import pymel.core as pm
import os
import shutil
import zipfile


def ohPublishCurrentFile():
    file_path = cmds.file(sceneName=True, q=True)

    dir, filename = os.path.split(file_path)
    rig_dir = os.path.dirname(dir)
    asset_dir = os.path.dirname(rig_dir)
    dev_dir = os.path.dirname(asset_dir)
    characters_dir = os.path.dirname(dev_dir)

    # rig, character, dev, "Characters"
    basename, ver, ext = filename.split(".")

    non_ver = ".".join((basename, ext))
    non_ver_mb = ".".join((basename, "mb"))

    version_dir = os.path.join(rig_dir, "publish")

    #nonvray_dir = os.path.join(characters_dir, "noVray")
    vray_dir = os.path.join(characters_dir, "vray")

    sel = pm.ls(sl=True)

    if not sel:
        return

    exp_ma = pm.exportSelected(os.path.join(version_dir, filename))
    exp_mb = pm.exportSelected(os.path.join(version_dir, filename), type="mayaBinary")

    print(("Exported: %s, %s" % (exp_ma, exp_mb)))

    shutil.copy2(exp_ma, os.path.join(vray_dir,non_ver))
    shutil.copy2(exp_mb, os.path.join(vray_dir,non_ver_mb))



def ohPublish_mayaMat_rig():
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

        nonvray_dir = os.path.join(characters_dir, "noVray")

        #vray_dir = os.path.join(characters_dir, "vray")

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
        exp_ma = pm.exportSelected(os.path.join(version_dir, filename), type="mayaAscii")
        exp_mb = pm.exportSelected(os.path.join(version_dir, filename), type="mayaBinary")

        print(("Exported: %s, %s" % (exp_ma, exp_mb)))

        shutil.copy2(exp_ma, os.path.join(nonvray_dir, rbasename + ".ma"))
        shutil.copy2(exp_mb, os.path.join(nonvray_dir, rbasename + ".mb"))

        pm.newFile(f=True)