import json
from datetime import datetime
import gzip

path = "C:\Users\pedro.vasconcelos\Documents\DAZ 3D\Studio\My Library\Scenes\boca_aberta_2.duf"

duf = gzip.open(path, "rb")
data = json.load(duf)

group_to_find = "/Head"
c = 0
animations = set()


## PREFIXO DE EXPRESSAO
# name://@selection#eCTRLBrowInnerUp-Down
##

data_set = {"file_version" : "0.6.0.0",
	"asset_info" : {
		"id" : "/Presets/Poses/express_1.duf",
		"type" : "preset_pose",
		"contributor" : {
			"author" : "dev.pedroivo",
			"email" : "",
			"website" : ""
		},
		"revision" : "1.0",
		"modified" : datetime.now().strftime("%Y-%m%dT%H:%M:%SZ")
	},
    "scene": {
        "animations" : []
    }
    }

print(data_set["scene"])
for i in data['scene']['modifiers']:
    if "group" in i:
        c+=1
        if group_to_find.upper() in str(i['group']).upper():
            path = "name://@selection#" + str(i['id']) + ":?value/value"
            value = i['channel']['current_value']
            print("+-----+")
            print(path)
            print(value)

            data_set["scene"]["animations"].append({"url":path, "keys": [[0,value]]})


with open('json_data.duf', 'w') as outfile:
    json.dump(data_set, outfile)





            
            
        
    
