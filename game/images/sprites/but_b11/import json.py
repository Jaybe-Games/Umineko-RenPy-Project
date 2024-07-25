import json
import os

script_dir = os.path.dirname(__file__)

# Get a list of all.json files in the script directory
json_files = [f for f in os.listdir(script_dir) if f.endswith('.json')]

for json_file in json_files:
    input_file = os.path.join(script_dir, json_file)
    output_file = os.path.join(script_dir, json_file.replace('.json', '.rpy'))

    with open(input_file, encoding='utf-8') as f:
        data = json.load(f)

    written_faces = set()
    written_mouths = set()

    with open(output_file, 'w', encoding='utf-8') as f:
        character_name = json_file.replace('.json', '').replace('_', ' ')
        f.write(f'layeredimage {character_name}:\n')
        f.write('    always:\n')
        f.write(f'        "images/bustup/{json_file.replace(".json", "")}/{json_file.replace(".json", "")}.png"\n')
        f.write('\n    group face:\n')
        for key, value in data.items():
            for item in value:
                face = item['parts'][1]['path']
                face_x, face_y = item['parts'][1]['x'], item['parts'][1]['y']
                if '_1.png' not in face and face not in written_faces:
                    f.write(f'        attribute {key}:\n')
                    f.write(f'            pos ({face_x}, {face_y})\n')
                    written_faces.add(face)
        f.write('\n    group mouth:\n')
        for key, value in data.items():
            for item in value:
                mouth = item['parts'][2]['path']
                mouth_x, mouth_y = item['parts'][2]['x'], item['parts'][2]['y']
                if '_0.png' not in mouth and '_2.png' not in mouth and '_3.png' not in mouth and mouth not in written_mouths:
                    mouth_key = f'{key}_{mouth.split("_")[-1].split(".")[0]}'
                    f.write(f'        attribute {mouth_key}:\n')
                    f.write(f'            pos ({mouth_x}, {mouth_y})\n')
                    written_mouths.add(mouth)