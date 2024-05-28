#   Licence
#
#   Copyright (c) 2024, JAYBE GAMES
#
#   All rights reserved.
#
#   Reproduction and distribution of this code, with or without modification, are prohibited without the express written permission of the author.
#
#   THIS CODE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.

import importlib
import subprocess
import sys

print(f"JAYBE'S ENHANCED LIPSYNC\n\n")
print(f"Copyright (c) 2024, JAYBE GAMES")
print(f"All rights reserved.")
print(f"Reproduction and distribution of this code, with or without modification, are prohibited without the express written permission of the author.")
print(f"THIS CODE IS PROVIDED 'AS IS' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.\n")

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

modules = ['numpy', 'os', 'soundfile', 'math', 'shutil']

for module in modules:
    try:
        importlib.import_module(module)
    except ImportError:
        print(f"{module} is not installed.")
        user_input = input("Do you want to install {module}? (y/n): ")
        if user_input.lower() == 'y':
            print("Installing now...")
            install(module)
        else:
            sys.exit()

import numpy as np
import os
import soundfile as sf
import math
import shutil

class lipsync:
    def __init__(self, filename, output_dir):
        self.filename = filename
        try:
            self.data, self.sample_rate = sf.read(filename)
        except Exception as e:
            raise ValueError(f"Error while reading file {filename}: {str(e)}")
        self.num_samples_per_chunk = int(self.sample_rate * 50 / 1000)  # 50 ms chunks
        self.max_sample = np.iinfo(np.int16).max
        self.max_db = 20 * np.log10(np.max(np.abs(self.data)) / self.max_sample) + 240  # Calculate the maximum peak in dB + offset
        self.lower_limit_db = self.max_db - 30  # Lower limit in dB
        self.upper_limit_db = self.max_db - 12  # Upper limit in dB
        self.lip_stage = 0
        self.last_lip_stage = 0
        self.output_dir = output_dir
        self.chunk_index = 0

    def read_chunk(self):
        start = self.chunk_index * self.num_samples_per_chunk
        end = start + self.num_samples_per_chunk
        self.chunk_index += 1
        if end > len(self.data):
            return None  # End of file
        chunk = self.data[start:end]
        # If the audio file is stereo, take the average of the two channels
        if chunk.ndim > 1:
            chunk = np.mean(chunk, axis=1)
        return chunk


    def process_chunk(self, samples):
        peak_sample = max(np.abs(samples))
        peak_value = peak_sample / self.max_sample
        # Convert the peak value to decibels
        min_peak_value = 1e-12  # Set a minimum peak value to avoid log(0)
        peak_db = 20 * math.log10(max(peak_value, min_peak_value))
        # Add an offset to make the dB value positive
        peak_db_offset = peak_db + 240
        if peak_db_offset < self.lower_limit_db:
            self.lip_stage = 0
        elif peak_db_offset < self.upper_limit_db:
            self.lip_stage = 1
        else:
            self.lip_stage = 2
        if abs(self.last_lip_stage - self.lip_stage) > 1:
            self.lip_stage = 1
        self.last_lip_stage = self.lip_stage
        return self.lip_stage

    def run(self):
        print(f'Analyse audiofile {self.filename}...')
        output_filename = os.path.join(self.output_dir, os.path.splitext(os.path.basename(self.filename))[0] + '.txt')
        with open(output_filename, 'w') as f:
            while True:
                samples = self.read_chunk()
                if samples is None:
                    break
                lip_stage = self.process_chunk(samples)
                # Write the lip stage to the file for each chunk
                f.write(f'{lip_stage}\n')
            print(f'Analysis complete!\n')

import os
import shutil

def process_directory(directory):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Join the script directory with the relative path
    full_dir = os.path.join(script_dir, directory)
    if not os.path.isdir(full_dir):
        raise ValueError(f"The {full_dir} directory does not exist.")
    output_dir = os.path.join(script_dir, 'processed')
    os.makedirs(output_dir, exist_ok=True)

    # List of supported extensions
    supported_extensions = ['.ogg', '.opus', '.mp3', '.flac', '.wma', '.wav']

    for filename in os.listdir(full_dir):
        # Check if the file extension is in the list of supported extensions
        if os.path.splitext(filename)[1] in supported_extensions:
            # Convert the filename to lowercase
            lower_filename = filename.lower()
            # Rename the file
            os.rename(os.path.join(full_dir, filename), os.path.join(full_dir, lower_filename))
            try:
                action = lipsync(os.path.join(full_dir, lower_filename), output_dir)
                action.run()
            except Exception as e:
                print(f"Error while processing file {lower_filename}: {str(e)}")

process_directory('game/audio/voice')

def process_txt_file(input_dir, output_dir, txt_name):
    # Get the prefix before the underscore
    prefix = txt_name.split('_')[0]

    # Open the input file
    with open(os.path.join(input_dir, txt_name + '.txt'), 'r') as f:
        lines = f.readlines()

    # Prepare the output file
    output_filename = os.path.join(output_dir, txt_name + '.rpy')  # Add the .rpy extension
    with open(output_filename, 'w') as f:
        f.write(f'image {txt_name}:\n')
        for line in lines:
            lip_stage = line.strip()  # Get the number as a string
            f.write(f'    "/sprites/{prefix}/[{prefix}_pose]/[{prefix}_face]/{lip_stage}.png"\n')
            f.write(f'    .05\n')
                # If the last number was 2, add 1.png and 0.png at the end
        if lip_stage == '2':
            f.write(f'    "/sprites/{prefix}/[{prefix}_pose]/[{prefix}_face]/1.png"\n')
            f.write(f'    .05\n')
            f.write(f'    "/sprites/{prefix}/[{prefix}_pose]/[{prefix}_face]/0.png"\n')
        # force a 0 at every end
        f.write(f'    "/sprites/{prefix}/[{prefix}_pose]/[{prefix}_face]/0.png"\n')
        

def process_directory_second(input_dir, output_dir):
    # Set the working directory to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Process all .txt files in the input directory
    print(f'Processing lipsync for RenPy...')
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            # Convert filename to lowercase
            filename = filename.lower()
            filename_without_extension = os.path.splitext(filename)[0]
            # Split the filename on underscore and get the prefix
            prefix = filename_without_extension.split('_')[0]
            # Create the output directory with the prefix
            specific_output_dir = output_dir.format(prefix=prefix)
            os.makedirs(specific_output_dir, exist_ok=True)
            process_txt_file(input_dir, specific_output_dir, filename_without_extension)

    # Delete the processed directory
    shutil.rmtree(input_dir)

    print(f"All .rpy files have been generated in {os.path.dirname(output_dir)} !")

process_directory_second('processed', 'game/images/sprites/voices/{prefix}')





