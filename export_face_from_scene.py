import os
import gzip
import json
from datetime import datetime
from os.path import exists
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--custom_scene_dir', '-cs' , dest='scene_dir', type=str, help='Caminho do diretório que vai pegar as cenas')
parser.add_argument('--single_scene', '-single' , dest='scene_path', type=str, help='Caminho absoluto para cena única')
parser.add_argument('--output_dir', '-out', dest='out_dir', type=str, help='Diretório para output das poses')
args = parser.parse_args()

# Diretorios padrões
default_dir = r"C:\Users\\" +os.getlogin() + r"\Documents\DAZ 3D\Studio\My Library\Scenes"
default_out_dir = r"C:\Users\\" +os.getlogin() + r"\Documents\DAZ 3D\Studio\My Library\Presets\Poses"


# Preparação esqueleto arquivo
group_to_find = "/Head"
animations = set()
data_set = {
    "file_version": "0.6.0.0",
    "asset_info": {
        "id": "/Presets/Poses/express_1.duf",
        "type": "preset_pose",
                "contributor": {
                    "author": "dev.pedroivo",
                    "email": "",
                    "website": ""
                },
        "revision": "1.0",
        "modified": datetime.now().strftime("%Y-%m%dT%H:%M:%SZ")
    },
    "scene": {
        "animations": []
    }
}

def scene_to_pose_file(file_path, filename):
    duf = gzip.open(file_path, "rb")
    data = json.load(duf)
    
    for i in data['scene']['modifiers']:
        if "group" in i:
            if group_to_find.upper() in str(i['group']).upper():
                path = "name://@selection#" + str(i['id']) + ":?value/value"
                value = i['channel']['current_value']
                data_set["scene"]["animations"].append({"url":path, "keys": [[0,value]]})
    
    filepath = default_out_dir + "\\head_" + filename
    
    if args.out_dir:
        filepath = args.out_dir +  "\\head" + filename
    
    with open(filepath, 'w') as outfile:
        json.dump(data_set, outfile)    

def folder_to_pose_file(folder_path):
    for file in os.listdir(folder_path):
        filename = os.fsdecode(file)
        if filename.endswith(".duf") or filename.endswith(".7z"):
            absolute_path = folder_path + "\\" + str(filename)
            scene_to_pose_file(absolute_path, filename)
            
        
if __name__ == "__main__":
    ## Cena Única
    if args.scene_path and exists(args.scene_path):
        scene_to_pose_file(args.scene_path, os.path.basename(args.scene_path))
        sys.exit()

    ## Diretório
    if args.scene_dir and exists(args.scene_dir):
        folder_to_pose_file(args.scene_dir)
        sys.exit()

    folder_to_pose_file(default_dir)