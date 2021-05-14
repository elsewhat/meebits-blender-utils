# Meebits vox importer
Blender import add-on for Meebits based on [MagicaVoxel `.vox` format](https://github.com/ephtracy/voxel-model/blob/master/MagicaVoxel-file-format-vox.txt)

![image](https://user-images.githubusercontent.com/1133607/118240998-ea5fa780-b49b-11eb-8090-6e48640d2211.png)

This builds upon [technistguru/MagicaVoxel_Importer](https://github.com/technistguru/MagicaVoxel_Importer)

## Getting Started

### Installation

This add-on needs to be installed into Blender in order to be used.
Directions for this process can be found [here](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#rd-party-add-ons) directly from the Blender Documentation.

Only [`io_scene_meebits_vox.py`](io_scene_meebits_vox.py) need be installed, other files in this repository are not functionally required.

**Note:** in order to enable the add-on, you will need to have `Testing` add-ons visible within the Blender Preferences menu.

![Enabling Add-on in Prefernces](https://user-images.githubusercontent.com/1133607/118179489-a89c1600-b435-11eb-9664-fd3f51c744a2.png)


### Usage

With the add-on installed and enabled, the importer can be accessed from `File > Import > Meebit (.vox)`

### Import options

This add-on offers several import options, seen on the file select menu of the import.

![image](https://user-images.githubusercontent.com/1133607/118270744-bba7f800-b4c0-11eb-8a73-2fa744a98e72.png)


Settings come from [technistguru/MagicaVoxel_Importer](https://github.com/technistguru/MagicaVoxel_Importer) and most of them will likely be removed in the future. 

- *Voxel Size*: how large each voxel should be, in Blender Units. Default is 0.025 which gives a meebit height of 1.675 meters
- *Rig with Meebit armature": If current scene has an armature with name MeebitArmature, it automatically joins them with automatic weights
- *Scale Meebit armature to fit": Will scale the armature dimension to be the same as the meebits dimensions

## Questions and Concerns

If in using this add-on you encounter difficulties, be sure to check [the issues](), in case a solution has been outlined there. If not, then issues are welcomed.

## Changelog and Versioning

## License

This project is licensed under the GPL v3.0 License - see the [LICENSE](LICENSE) file for details
