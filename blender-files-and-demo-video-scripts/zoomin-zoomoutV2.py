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

# Add a plane if it doesn't exist
if "Background_Plane" not in bpy.data.objects:
    bpy.ops.mesh.primitive_plane_add(size=20)
    plane = bpy.context.active_object
    plane.name = "Background_Plane"
else:
    plane = bpy.data.objects["Background_Plane"]

# Set up material for the plane
plane_mat = bpy.data.materials.new(name="PlaneBackground")
plane.data.materials.clear()
plane.data.materials.append(plane_mat)
plane_mat.use_nodes = True
nodes = plane_mat.node_tree.nodes
links = plane_mat.node_tree.links

# Clear existing nodes
nodes.clear()

# Create a simple diffuse material that won't be affected by lighting changes
diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
output = nodes.new(type='ShaderNodeOutputMaterial')
color_ramp = nodes.new(type='ShaderNodeValToRGB')

# Set up color ramp for gradient
color_ramp.color_ramp.elements[0].position = 0.3
color_ramp.color_ramp.elements[0].color = (0.2, 0.2, 0.4, 1.0)  # Dark blue
color_ramp.color_ramp.elements[1].position = 0.7
color_ramp.color_ramp.elements[1].color = (0.3, 0.3, 0.5, 1.0)  # Light blue

# Create texture coordinates for gradient
tex_coord = nodes.new(type='ShaderNodeTexCoord')
mapping = nodes.new(type='ShaderNodeMapping')

# Connect nodes
links.new(tex_coord.outputs["Generated"], mapping.inputs["Vector"])
links.new(mapping.outputs["Vector"], color_ramp.inputs["Fac"])
links.new(color_ramp.outputs["Color"], diffuse.inputs["Color"])
links.new(diffuse.outputs["BSDF"], output.inputs["Surface"])

# Adjust mapping to control gradient direction
mapping.inputs["Rotation"].default_value = (0, 0, 0)
mapping.inputs["Scale"].default_value = (1, 1, 1)

# Lighting setup with improved stability
sun_obj = bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
sun = bpy.context.active_object.data
sun.energy = 3  # Reduced energy
sun.use_shadow = False  # Disable shadows
sun.color = (1, 0.9, 0.8)  # Slightly warm color

fill_obj = bpy.ops.object.light_add(type='AREA', location=(-5, 5, 5))
fill_light = bpy.context.active_object.data
fill_light.energy = 1.5  # Reduced energy
fill_light.color = (0.8, 0.9, 1.0)  # Slightly cool color
fill_light.use_shadow = False  # Disable shadows

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

# Additional render settings to prevent flickering
scene.render.use_motion_blur = False
scene.eevee.use_ssr = False           # Disable screen space reflections
scene.eevee.use_soft_shadows = False  # Disable soft shadows
scene.eevee.use_bloom = False         # Disable bloom effect
scene.eevee.taa_render_samples = 64   # Increase samples to reduce noise

# Ensure all lights have shadows disabled
for light in bpy.data.lights:
    if hasattr(light, 'use_shadow'):
        light.use_shadow = False

print("Animation and render settings configured. Start rendering in the Render tab.")