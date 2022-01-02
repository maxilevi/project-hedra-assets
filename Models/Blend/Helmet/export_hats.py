import bpy
import os

def deselect_all():
    for ob in bpy.data.objects:
        ob.select = False

def try_export():
    file_path = bpy.data.filepath
    scene = bpy.context.scene
    deselect_all()
    for ob in bpy.data.objects:
        if ob.hide:
            continue
        scene.objects.active = ob
        ob.select = True
        bpy.ops.wm.collada_export(
            filepath = file_path[:-10] + ob.name + '.dae',
            check_existing = False,  
            selected = True,
        )
        print('Exporting ' + ob.name)
        ob.select = False
    return True
    
result = try_export()

if not result:
    print ("Export failed.")