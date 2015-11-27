#! C:\Python34

# /usr/bin/python
import sys, yaml, json, re, shutil, os, glob

source_path = "C:\\Users\\tom\\Dropbox\\LISA_PARENT_FOLDER\\1 LISA game files\\JOYFUL\\JOYFUL_UPDATED\\YAML\\"
output_path = "C:\\Users\\tom\\Dropbox\\LISA_PARENT_FOLDER\\1 LISA game files\\JOYFUL\\JOYFUL_UPDATED\\JSON\\"

if os.path.exists(output_path):
    shutil.rmtree(output_path)
    os.makedirs(output_path)
else:
    os.makedirs(output_path)

#for filename in os.listdir('/home/tom/Desktop/YAML-Edit/'):
#for filename in os.listdir(source_path):
for filename in glob.glob(source_path + "*.yaml"):
    with open(filename, 'r') as stream:
        data = stream.read()
        newname = os.path.basename(filename).replace("yaml", "json")
        result = re.sub("!ruby/object.*", '', data)
        with open((output_path + newname), 'w') as fp:
            json.dump(yaml.load(result), fp, indent=4)