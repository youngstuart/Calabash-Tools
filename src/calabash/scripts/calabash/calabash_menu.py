import maya.cmds as cmds
import os

calabash_menu = None




def calabash_menu():
    global calabash_menu
    if cmds.menu('calabash_m', exists=True):
        cmds.deleteUI('calabash_m')

    ###############################################################################

    calabash_menu = cmds.menu('calabash_m', p='MayaWindow', label='Calabash', tearOff=True)

    ###############################################################################

    this_path = os.path.normpath(os.path.dirname(__file__))
    up_path = (os.path.dirname(this_path))

    general_submenu = cmds.menuItem('general_sub', p=calabash_menu, subMenu=True, label='General', tearOff=True)
    ani_submenu = cmds.menuItem('ani_sub', p=calabash_menu, subMenu=True, label='Animation', tearOff=True)
    model_submenu = cmds.menuItem('model_sub', p=calabash_menu, subMenu=True, label='Modeling', tearOff=True)
    rendering_submenu = cmds.menuItem('rendering_sub', p=calabash_menu, subMenu=True, label='Render', tearOff=True)
    rigging_submenu = cmds.menuItem('rigging_sub', p=calabash_menu, subMenu=True, label='Rigging', tearOff=True)
    shading_submenu = cmds.menuItem('shading_sub', p=calabash_menu, subMenu=True, label='Shading', tearOff=True, version="2017")
    xgen_submenu = cmds.menuItem('xgen_sub', p=calabash_menu, subMenu=True, label='XGen', tearOff=True)
    fx_submenu = cmds.menuItem('fx_sub', p=calabash_menu, subMenu=True, label='FX', tearOff=True)
    publish_submenu = cmds.menuItem('pub_sub', p=calabash_menu, subMenu=True, label='Publish', tearOff=True)
    pipeman_submenu = cmds.menuItem(p=calabash_menu, label='Pipeline Manager', c='from pipeman import pipeman;import importlib;importlib.reload(pipeman);pipeman.run()')
    #cmds.menuItem(p=rigging_submenu, divider=True, itl=True)
    #hatch_submenu = cmds.menuItem('hatch_sub', p=calabash_menu, subMenu=True, label='Hatchimals', tearOff=True)


    ###############################################################################


    # General Submenu
    cmds.menuItem(p=general_submenu, label='Increase File Version', c='from calabash import increaseVersion;import importlib; importlib.reload(increaseVersion);increaseVersion.versionUp()')


    ###############################################################################


    # Animation Submenu
    cmds.menuItem(p=ani_submenu, label='Good Playblast', c='from goodPlayblast_c import playblast_utils as gu;import importlib; importlib.reload(gu); pb = gu.Playblaster(); pb.playblast()', image="goodplayblast.png")
    cmds.menuItem(p=ani_submenu, optionBox=True, c='import goodPlayblast_c.playblast_view as gp;import importlib; importlib.reload(gp); gp.launch()')


    ###############################################################################


    # Modeling Submenu
    cmds.menuItem(p=model_submenu, label='Delete Intermediate Shapes', c='from calabash import model_utils;import importlib; importlib.reload(model_utils);model_utils.del_int_shapes()')
    cmds.menuItem(p=model_submenu, label='Basic Mesh Cleanup', c='from calabash import model_utils;import importlib; importlib.reload(model_utils);model_utils.cleanup_mesh()', version="2017")
    cmds.menuItem(p=model_submenu, label='abSymMesh', c='from maya import mel; mel.eval("abSymMesh")', version="2017")


    ###############################################################################


    # Rendering Submenu
    cmds.menuItem(p=rendering_submenu, label='Submit to Smedge', c='from maya import mel; mel.eval("smedgeRender");')
    cmds.menuItem(p=rendering_submenu, label='Set Overscan', c='from calabash import overscan;import importlib; importlib.reload(overscan); overscan.run()')
    cmds.menuItem(p=rendering_submenu, divider=True, dividerLabel='Vray Attributes', itl=True)
    cmds.menuItem(p=rendering_submenu, label='Vray Toolbox', c='from calabash import vray_toolbox;import importlib; importlib.reload(vray_toolbox);vray_toolbox.launch()')
    cmds.menuItem(p=rendering_submenu, label='Add Material ID Attributes (Beta)', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.makeVrayMatId()')
    cmds.menuItem(p=rendering_submenu, divider=True, dividerLabel='Vray Object Properties', itl=True)
    cmds.menuItem(p=rendering_submenu, label='Apply single object properties node to selection', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.single_vop()')
    cmds.menuItem(p=rendering_submenu, label='Primary Vis Off', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.primVis()')
    cmds.menuItem(p=rendering_submenu, label='Matte Surface', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.matteSurface()')
    cmds.menuItem(p=rendering_submenu, divider=True, dividerLabel='Render Settings', itl=True)
    cmds.menuItem(p=rendering_submenu, label='Apply Final Render Settings', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.renderSettings()')
    cmds.menuItem(p=rendering_submenu, label='Apply Final Render GI Settings', c='from calabash import vrayUtils;import importlib; importlib.reload(vrayUtils);vrayUtils.giSettings()')
    cmds.menuItem(p=rendering_submenu, label='Render Elements for Selected Lights', c='from maya import mel;mel.eval("vrLightPass;")')


    ###############################################################################

    # Publish Submenu
    cmds.menuItem(p=publish_submenu, label='Publish Selected Asset', c='from calabash import fileUtils;import importlib; importlib.reload(fileUtils);fileUtils.publishCurrentFile()')
    cmds.menuItem(p=publish_submenu, label='Publish Animation', c='from calabash import animUtils;import importlib; importlib.reload(animUtils);animUtils.publishAnim()')
    cmds.menuItem(p=publish_submenu, label='Create AutoCache',  c='from calabash import animUtils;import importlib; importlib.reload(animUtils); animUtils.autocache_gui.run()')
    cmds.menuItem(p=publish_submenu, label='Publish Camera from animation', c='from calabash import animUtils;import importlib; importlib.reload(animUtils); animUtils.ouroboros()')
    #cmds.menuItem(p=rigging_submenu, label='Publish Vray Shading', c='from calabash import fileUtils;import importlib; importlib.reload(fileUtils);fileUtils.publish_vray_rig()')
    cmds.menuItem(p=publish_submenu, label='Publish Groom', c='from calabash import fileUtils;import importlib; importlib.reload(fileUtils);fileUtils.publish_groom_rig()')

    cmds.menuItem(p=rigging_submenu, divider=True, itl=True)
    cmds.menuItem(p=rigging_submenu, label='Hide Joints', c='from calabash import rigUtils;import importlib; importlib.reload(rigUtils);rigUtils.jointDisplay()')
    cmds.menuItem(p=rigging_submenu, label='Show Joints', c='from calabash import rigUtils  ;import importlib; importlib.reload(rigUtils);rigUtils.jointDisplay(show=True)')

    cmds.menuItem(p=rigging_submenu, divider=True, itl=True)
    cmds.menuItem(p=rigging_submenu, label='MoveCtrl', c='from calabash import moveControl;import importlib; importlib.reload(moveControl);moveControl.moveCtrlUI()')
    cmds.menuItem(p=rigging_submenu, label='Jamm Joint Orient', c='import jammOrientJoint as oj;oj.orientJointsWindow()',version="2017")


    ###############################################################################


    # Shading Submenu
    cmds.menuItem(p=shading_submenu, label='Rename Shading Groups', c='from calabash import shading_utils;import importlib; importlib.reload(shading_utils);shading_utils.rename_shading_groups()', version="2017")
    cmds.menuItem(p=shading_submenu, label='Apply Materials to Asset', c='from calabash import shading_utils;import importlib; importlib.reload(shading_utils);shading_utils.apply_look()')

    ###############################################################################


    # XGen Submenu
    cmds.menuItem(p=xgen_submenu, label='Cache Descriptions', c='from calabash import xgen_utils;import importlib; importlib.reload(xgen_utils);xgen_utils.cache_groomableSplines()')
    cmds.menuItem(p=xgen_submenu, label='Repath Caches', c='from calabash import xgen_utils;import importlib; importlib.reload(xgen_utils);xgen_utils.repath_caches()')


    ###############################################################################

    # FX Submenu
    cmds.menuItem(p=fx_submenu, label='RGB TBS', c='from calabash import rgb_tbs;import importlib; importlib.reload(rgb_tbs);rgb_tbs.tbs()')
    cmds.menuItem(p=fx_submenu, label='Classic TBS', c='mel.eval("TBS")')


    ###############################################################################

    # Hatchimal Submenu
    # cmds.menuItem(p=hatch_submenu, label='Publish Season2 Rig', c='from calabash import oldHatchUtils;import importlib; importlib.reload(oldHatchUtils);oldHatchUtils.ohPublishCurrentFile()')
    # cmds.menuItem(p=hatch_submenu, label='Publish Season2 No Vray Rig', c='from calabash import oldHatchUtils;import importlib; importlib.reload(oldHatchUtils);oldHatchUtils.ohPublish_mayaMat_rig()')
    # cmds.menuItem(p=hatch_submenu, label='Rename New Hatch Rigs', c='from calabash import fileUtils;import importlib; importlib.reload(fileUtils);fileUtils.rename_hatch_rigs()')




calabash_menu()