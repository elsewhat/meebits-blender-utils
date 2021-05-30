# Blender docker file from https://hub.docker.com/r/nytimes/blender https://github.com/nytimes/rd-blender-docker

FROM nytimes/blender:latest

copy blender_install_vrm_addon.py .
copy VRM_Addon_for_Blender-release.zip .

# Install VRM add-on through our script
run blender -b  -y  --python blender_install_vrm_addon.py