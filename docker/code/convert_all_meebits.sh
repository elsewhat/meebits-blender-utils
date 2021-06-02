#!/bin/bash
find /meebits/*solid.vox -maxdepth 1 -type f -exec blender MeebitRig.blend --background --python meebit_export_to_vrm.py -- --meebit "{}" \;
echo "Moving VRM files to output_vrm/"
mv *.vrm /output_vrm