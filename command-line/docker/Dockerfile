# Blender docker file from https://hub.docker.com/r/nytimes/blender https://github.com/nytimes/rd-blender-docker

FROM nytimes/blender:latest

# Copy scripts
copy *.py ./
# Copy blender scene with aramature
copy MeebitRig.blend .
# Copy VRM add-on
copy VRM_Addon_for_Blender-release.zip .

# Install VRM add-on through our script
run blender -b  -y  --python blender_install_vrm_addon.py

# Copy meebits
RUN mkdir -p /meebits
copy meebits/*.vox /meebits

# Create volume which will be exported once container is don
mkdir output_vrm