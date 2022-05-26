import numpy as np
from PIL import Image
import gif2numpy
import os

###########################

colors = [
    [240, 235, 241],
    [224, 187, 161],
    [33, 38, 37],
    [230, 227, 223],
    [186, 146, 119],
    [74, 78, 90],
    [51, 49, 43],
    [255, 255, 255],
    [246, 229, 220]
]

###########################

def main(image):
    image_array = np.array([])

    if "gif" in image_name:
        frames, _, _ = gif2numpy.convert(image_name)

        for f in range(len(frames)):
            if f == 0:
                image_array = frames[f]
            else:
                np.concatenate((image_array, frames[f]))
    else:
        image_array = np.array(image)

    print(image_array.shape)

    score = 0

    for j in range(image_array.shape[0]):
        for k in range(image_array.shape[1]):
            lowest = 256

            for color in colors:
                color_score = np.linalg.norm(np.array(color) - image_array[j][k])

                lowest = min(lowest, color_score)

            score += lowest

    score /= image_array.shape[0] * image_array.shape[1]
    score = 102 / score

    return score

###########################

# image_name = "./control.png"
# image = Image.open(image_name)
# print(main(image))

###########################

path = ""
folders = os.listdir(path)

total = 0
count = 0

for subpath in folders:
    subfolder = os.listdir(path + "/" + subpath)

    for image in subfolder:
        image_name = path + "/" + subpath + "/" + str(image)
        image = Image.open(image_name)
        score = main(image)

        total += score
        count += 1

        print(subpath + "/" + str(image), str(score))

print(str(total/count))

###########################

