import bpy
import math

# Antibody object name (replace if different)
antibody_name = "1HZH"

# Scene setup
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 250  # Adjust animation length

# Camera setup with error handling
if "Camera" not in bpy.data.objects:
    raise ValueError("Camera not found in scene")
camera = bpy.data.objects["Camera"]
camera.location = (5, -5, 5)  # Adjust camera position
camera.rotation_euler = (math.radians(45), 0, math.radians(45))  # Adjust camera rotation
camera.data.lens = 35  # Adjust focal length

# Lighting setup (inspired by the ad's bright, somewhat back-lit look)
sun_obj = bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))  # Main light, slightly behind
sun = bpy.context.active_object.data
sun.energy = 5  # Adjust brightness
sun.color = (1, 0.9, 0.8)  # Slightly warm color

fill_obj = bpy.ops.object.light_add(type='POINT', location=(-5, 5, 5))  # Fill light
fill_light = bpy.context.active_object.data
fill_light.energy = 2  # Lower intensity
fill_light.color = (0.8, 0.9, 1.0)  # Slightly cool color to balance

# Antibody object access with error handling
if antibody_name not in bpy.data.objects:
    raise ValueError(f"Antibody object '{antibody_name}' not found in scene")
antibody = bpy.data.objects[antibody_name]

# Antibody material setup
if antibody.data.materials:  # Check if a material already exists
    mat = antibody.data.materials[0]
else:
    mat = bpy.data.materials.new(name="AntibodyMaterial")
    antibody.data.materials.append(mat)

mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links

# Clear existing nodes
for node in nodes:
    nodes.remove(node)

principled_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
output = nodes.new(type='ShaderNodeOutputMaterial')

links.new(principled_bsdf.outputs["BSDF"], output.inputs["Surface"])
principled_bsdf.inputs["Metallic"].default_value = 0.2
principled_bsdf.inputs["Roughness"].default_value = 0.3  # Somewhat glossy

# Antibody animation with optimized keyframing
frames = [scene.frame_start, scene.frame_end]
for frame in frames:
    scene.frame_set(frame)
    antibody.rotation_euler[2] = math.radians(frame * 2)  # Rotate around Z-axis
    antibody.keyframe_insert(data_path="rotation_euler")

# World settings with error handling
if "World" not in bpy.data.worlds:
    world = bpy.data.worlds.new("World")
else:
    world = bpy.data.worlds["World"]
    
world.use_nodes = True
world_nodes = world.node_tree.nodes
world_links = world.node_tree.links

# Clear existing world nodes
for node in world_nodes:
    world_nodes.remove(node)

world_output = world_nodes.new("ShaderNodeOutputWorld")
background = world_nodes.new("ShaderNodeBackground")
background.inputs["Color"].default_value = (0.1, 0.1, 0.2, 1)  # Dark blue/gray
world_links.new(background.outputs["Background"], world_output.inputs["Surface"])

# Render settings
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.filepath = "//output.mp4"  # Render to project directory
scene.render.image_settings.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.ffmpeg.codec = 'H264'
scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'

print("Animation and render settings configured. Start rendering in the Render tab.")