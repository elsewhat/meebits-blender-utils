# Docker for meebits blender utils
Provides access to convert meebits without installing blender locally

Step 1: Install docker desktop https://docs.docker.com/get-docker/
Step 2: Copy your meebits meebit_xxx_t_solid.vox to meebits-blender-utils/docker/meebits
Step 2: Open command prompt and navigate to directory meebits-blender-utils/docker
Step 3: Build docker image with `docker build -t blender-meebits-v1 .`
Step 4: Run the docker image interactively `docker run -it blender-meebits-v1`
Step 5: Run `blender MeebitRig.blend --background --python meebit_export_to_vrm.py -- --meebit "/meebits/meebit_17871_t_solid.vox"` . Converted .vrm file will be in root folder /
Step 6. 


## Useful commands
`docker images` - Get existing images
`docker ps` - View running images
`docker cp meebit_17871_t_solid.vox 8b7b72e384aa:/meebits` - Copy local file to docker container (8b7b72e384aa is container id found in `docker ps`)

`blender MeebitRig.blend --background --python meebit_export_to_vrm.py -- --meebit "/meebits/meebit_17871_t_solid.vox"` - Convert meebit if running in the image interactively
`docker system prune -a --volumes` - Reclaim space