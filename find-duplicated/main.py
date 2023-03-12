import imagehash
from PIL import Image
import numpy as np
import os
from pathlib import Path
import time
import hashlib

# Method - using Image Hash (Not using cryptographic algorithms, after some transformation)
# Other methods:
# https://github.com/magamig/duplicate-images-finder (CV2)
# https://github.com/adumrewal/SIFTImageSimilarity (CV2)
# https://github.com/markusressel/py-image-dedup

dir_path = 'F:\\.akv-recover\\Pictures\\dupl'
HAMMING_DISTANCE_EQUAL_THRESHOLD = 0

list_of_files = os.walk(dir_path)

# Z Tranform Image Hashing
# ref: https://towardsdatascience.com/removing-duplicate-or-similar-images-in-python-93d447c1c3eb
def alpharemover(image):
    if image.mode != 'RGBA':
        return image
    canvas = Image.new('RGBA', image.size, (255,255,255,255))
    canvas.paste(image, mask=image)
    return canvas.convert('RGB')

def with_ztransform_preprocess(hashfunc, hash_size=8):
    def function(path):
        image = alpharemover(Image.open(path))
        image = image.convert("L").resize((hash_size, hash_size), Image.LANCZOS)
        data = image.getdata()
        quantiles = np.arange(100)
        quantiles_values = np.percentile(data, quantiles)
        zdata = (np.interp(data, quantiles_values, quantiles) / 100 * 255).astype(np.uint8)
        image.putdata(zdata)
        return hashfunc(image)
    return function
# End of Z Tranform Image Hashing support methods

def get_file_hash(file_path, z_transform=False):
    try:
        return hashlib.md5(open(file_path,'rb').read()).hexdigest()
    
        if z_transform:
            # With Z Transform
            z_transformed_imagehash = with_ztransform_preprocess(imagehash.dhash, hash_size = 8)
            return z_transformed_imagehash(file_path)

        # Using Simple Image Hash, see reference for more hash algorithm
        # ref: https://github.com/JohannesBuchner/imagehash
        return imagehash.average_hash(Image.open(file_path))
    except Exception as error:
        print(str(error))
        return None

processed_data = []
for root, folders, files in list_of_files:
    for file in files:
        file_path = Path(os.path.join(root, file))
        print(file_path)
        file_hash = get_file_hash(file_path)
        image = Image.open(file_path)
        if file_hash:
            processed_data.append({
                'file': str(file_path),
                'file_hash': str(file_hash),
                'width': image.width,
                'height': image.height,
                'created': os.path.getctime(file_path),
                'modified': os.path.getmtime(file_path)
            })

COMPARISON_RESULT = {}

for i in range(0, len(processed_data)):
    if processed_data[i].get('duplicate', False):
        continue
    for j in range(i+1, len(processed_data)):
        if processed_data[j].get('duplicate', False):
            continue
        print(processed_data[i]['file'], processed_data[j]['file'])
        try:
            hash_i = processed_data[i]['file_hash']
            hash_j = processed_data[j]['file_hash']

            # hamming_distance = abs(imagehash.hex_to_hash(hash_i) - imagehash.hex_to_hash(hash_j))
            # if hamming_distance <= HAMMING_DISTANCE_EQUAL_THRESHOLD:
            if hash_i == hash_j:
                processed_data[j]['duplicate'] = True
                if hash_j in COMPARISON_RESULT.keys():
                    COMPARISON_RESULT[hash_j].append(processed_data[j])
                else:
                    if not hash_i in COMPARISON_RESULT.keys():
                        COMPARISON_RESULT[hash_i] = []
                        COMPARISON_RESULT[hash_i].append(processed_data[i])
                    COMPARISON_RESULT[hash_i].append(processed_data[j])
            
        except Exception as error:
            print(str(error))
            print(processed_data[i], processed_data[j])

duplicates = []
from operator import itemgetter
for key in COMPARISON_RESULT.keys():
    COMPARISON_RESULT[key].sort(key=itemgetter('width', 'height', 'modified', 'created'))
    for _ in COMPARISON_RESULT[key][1:]:
        duplicates.append(_['file'])
print(duplicates)

import json
with open('result.json', 'w') as _:
    _.write(json.dumps(COMPARISON_RESULT, indent=2))

