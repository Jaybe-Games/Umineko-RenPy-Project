import os
from PIL import Image
import multiprocessing
from functools import partial

# Set the source_folder to the path of your "images/sprites" directory
source_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'game/images/sprites')

# Output file format args.
SAVE_EXT = ".png"
SAVE_FORMAT = {
    "format": "png", 
    "lossless": True, 
    "quality": 100, 
    "method": 6
}

def process_diff_file(root, diff_file_name, source_image):
    source_image_px = source_image.load()
    diff_file_path = os.path.join(root, diff_file_name)
    if os.path.exists(diff_file_path):
        diff_image = Image.open(diff_file_path).convert(mode="RGBA")
        diff_image_px = diff_image.load()

        if diff_image.size!= source_image.size:
            print(f"Image dimensions for {diff_file_path} do not match, skipping!")
            return

        # Normal mode.
        difference = Image.new("RGBA", source_image.size, color=(0,0,0,0))
        difference_px = difference.load()
        
        for y in range(source_image.height):
            for x in range(source_image.width):
                r, g, b, a = diff_image_px[x, y]
                
                if a!= 0 and source_image_px[x, y]!= diff_image_px[x, y]:
                    difference_px[x, y] = diff_image_px[x, y]
        
        fn = "{}{}".format(diff_file_name.rsplit('.',maxsplit=1)[0], SAVE_EXT)
        save_path = os.path.join(root, fn)
        difference.save(save_path, **SAVE_FORMAT)
        
        print(f"{fn} saved at {save_path}")

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        for root, dirs, files in os.walk(source_folder):
            if '0.png' in files:
                source_image = Image.open(os.path.join(root, '0.png')).convert(mode="RGBA")
                process_diff_file_partial = partial(process_diff_file, root, source_image=source_image)
                pool.map(process_diff_file_partial, ['1.png', '2.png'])

    print("Done.")




