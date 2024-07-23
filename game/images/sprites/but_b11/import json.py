import json
import os

script_dir = os.path.dirname(__file__)
input_file = os.path.join(script_dir, 'but_b11.json')
output_file = os.path.join(script_dir, 'output.rpy')

with open(input_file, encoding='utf-8') as f:
    data = json.load(f)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('layeredimage but:\n')
    wrote_attribute = False
    wrote_face = {}
    wrote_mouth = {}
    for key, value in data.items():
        for item in value:
            base_sprite = item['parts'][0]['path']
            pose = base_sprite.split('/')[0].split('_')[1]  # extract the pose from the base sprite path
            face = item['parts'][1]['path']
            mouth = item['parts'][2]['path']
            face_x, face_y = item['parts'][1]['x'], item['parts'][1]['y']
            mouth_x, mouth_y = item['parts'][2]['x'], item['parts'][2]['y']

            if pose == 'b11' and not wrote_attribute:
                f.write(f'    attribute {pose} default:\n')
                f.write(f'        "images/sprites/{base_sprite}"\n')
                wrote_attribute = True

            face_key = f'face_{pose}_{key}'
            if face_key not in wrote_face:
                f.write(f'\n    group {face_key}:\n')
                f.write(f'        pos ({face_x}, {face_y})\n')
                f.write(f'        attribute {pose}_{key}_f:\n')
                f.write(f'            "images/sprites/{face}"\n')
                wrote_face[face_key] = True

            mouth_key = f'mouth_{pose}_{key}'
            if mouth_key not in wrote_mouth:
                f.write(f'\n    group {mouth_key}:\n')
                f.write(f'        pos ({mouth_x}, {mouth_y})\n')
                f.write(f'        attribute {pose}_{key}_m:\n')
                f.write(f'            "images/sprites/{mouth}"\n')
                wrote_mouth[mouth_key] = True