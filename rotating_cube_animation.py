import bpy
from math import radians

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create cube mesh
bpy.ops.mesh.primitive_cube_add(size=2)

# Get cube object
cube = bpy.context.active_object

# Create material for cube
material = bpy.data.materials.new(name="CubeMaterial")
material.diffuse_color = (0.8, 0.1, 0.3, 1)
cube.data.materials.append(material)

# Set cube rotation
cube.rotation_euler = (radians(45), radians(45), radians(45))

# Create light source
bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 0, 5))

# Create camera
bpy.ops.object.camera_add(align='VIEW', location=(6, -6, 6))
camera = bpy.context.active_object
camera.rotation_euler = (radians(60), 0, radians(45))

# Set camera as active
bpy.context.scene.camera = camera

# Set up animation
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 100
cube.rotation_euler = (radians(0), radians(0), radians(0))
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=1)
cube.rotation_euler = (radians(0), radians(0), radians(360))
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=100)

# Render settings
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'AVI'
bpy.context.scene.render.ffmpeg.codec = 'MPEG4'
bpy.context.scene.render.filepath = "//animation.avi"

# Render animation
bpy.ops.render.render(animation=True)
