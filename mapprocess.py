import numpy as np
from PIL import Image

#### Constants #####

colors = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'dark_blue': (0, 60, 85),
    'light_blue': (90, 200, 220),
    'yellow': (255, 255, 0),
    'orange': (255, 127, 0),
    'white': (255, 255, 255),
    'brown': (155, 150, 125)
}

correction_colors = {
    'a': (136, 136, 136),
    'b': (119, 8, 8),
    'c': (135, 135, 135),
    # 'd': (85, 42, 42),
    'e': (119, 119, 136)
}

#### Main ######

map_image = Image.open("devonian.jpg")
map_array = np.asarray(map_image)

L, M, N = np.shape(map_array)

edited_map_array = np.copy(map_array)

for i in range(L):
    for j in range(M):
        r, g, b = map_array[i][j]

        color_scores = [sum((l - r) ** 2 for l, r in zip((r, g, b), control_color)) ** 0.5 for control_color in colors.values()]

        min_color_score = min(color_scores)
        color_name = list(colors.keys())[color_scores.index(min_color_score)]

        if color_name == "dark_blue":
            edited_map_array[i][j] = [0, 0, 255]
        if color_name == "light_blue":
            edited_map_array[i][j] = [5, 170, 250]
        elif color_name == "green" or color_name == "brown":
            edited_map_array[i][j] = [255, 255, 0]
        elif color_name == "black":
            edited_map_array[i][j] = [0, 0, 0]
        else:
            edited_map_array[i][j] = [255, 127, 127]

edited_map_image = Image.fromarray(edited_map_array)
edited_map_image.save('devonian_edited.png')
edited_map_image.show()

edited_map_image = Image.open("devonian_edited.png")
edited_map_array = np.asarray(edited_map_image)

L, M, N = np.shape(edited_map_array)

deviations_array = np.copy(edited_map_array)

for i in range(L):
    for j in range(M):
        if L - 3 > i > 2 and M - 3 > j > 2:
            section = edited_map_array[i-2:i+3, j-2:j+3]

            section_avg_r = np.average([color[0] for color in section])
            section_avg_g = np.average([color[1] for color in section])
            section_avg_b = np.average([color[2] for color in section])

            section_avg = [section_avg_r, section_avg_b, section_avg_g]

            outlier_scores = [abs(edited_map_array[i][j][c] - section_avg[c]) for c in range(0, 3)]

            deviations_array[i][j] = outlier_scores

deviations_image = Image.fromarray(deviations_array)
deviations_image.save("devonian_deviations.png")

deviations_image = Image.open("devonian_deviations.png")
deviations_array = np.asarray(deviations_image)

L, M, N = np.shape(deviations_array)

deviation_corrected_map_array = np.copy(deviations_array)

for i in range(L):
    for j in range(M):
        r, g, b = deviations_array[i][j]

        color_scores = [sum((l - r) ** 2 for l, r in zip((r, g, b), control_color)) ** 0.5 for control_color in correction_colors.values()]

        min_color_score = min(color_scores)
        color_name = list(correction_colors.keys())[color_scores.index(min_color_score)]

        if min_color_score < 30:
            if color_name == "a" or color_name == "e" or color_name == "d":
                deviation_corrected_map_array[i][j] = [85, 85, 170]
            elif color_name == "b" or color_name == "c":
                deviation_corrected_map_array[i][j] = [85, 42, 42]

deviation_corrected_map_image = Image.fromarray(deviation_corrected_map_array)
deviation_corrected_map_image.save("devonian_deviation_corrected.png")

map_image = Image.open("devonian.jpg")
map_array = np.asarray(map_image)

L, M, N = np.shape(map_array)

filtered_array = map_array.copy()

for i in range(L):
    for j in range(M):
        if L - 3 > i > 2 and M - 3 > j > 2:
            section = map_array[i-2:i+3, j-2:j+3]

            section_avg_r = np.average([color[0] for color in section])
            section_avg_g = np.average([color[1] for color in section])
            section_avg_b = np.average([color[2] for color in section])

            section_avg = [section_avg_r, section_avg_b, section_avg_g]

            difference = np.average([abs(map_array[i][j][c] - section_avg[c]) for c in range(0, 3)])

            print(map_array[i][j], " - ", section_avg)

            if difference > 30:
                filtered_array[i][j] = section_avg
            else:
                print(difference)

deviations_image = Image.fromarray(filtered_array)
deviations_image.save("devonian_filtered.png")

edited_map_image = Image.fromarray(edited_map_array)
edited_map_image.save("devonian_edited.png")
edited_map_image.show()

deep_ocean = [255, 127, 127]
shallow_ocean = [5, 170, 250]
land = [255, 255, 0]
empty = [0, 0, 0]

deep_ocean_pixels = []
deep_ocean_colors = [0, 0, 0]
shallow_ocean_pixels = []
shallow_ocean_colors = [0, 0, 0]
land_pixels = []
land_colors = [0, 0, 0]

revision_pixels = []

for i in range(L):
    for j in range(M):
        original_color = map_array[i][j]
        edited_color = edited_map_array[i][j]

        if sum([abs(edited_color[x] - deep_ocean[x]) for x in range(0, 3)]) == 0:
            deep_ocean_pixels.append([i, j])
            deep_ocean_colors = [deep_ocean_colors[x] + original_color[x] for x in range(0, 3)]
        elif sum([abs(edited_color[x] - shallow_ocean[x]) for x in range(0, 3)]) == 0:
            shallow_ocean_pixels.append([i, j])
            shallow_ocean_colors = [shallow_ocean_colors[x] + original_color[x] for x in range(0, 3)]
        elif sum([abs(edited_color[x] - land[x]) for x in range(0, 3)]) == 0:
            land_pixels.append([i, j])
            land_colors = [land_colors[x] + original_color[x] for x in range(0, 3)]
        else:
            revision_pixels.append([i, j])

deep_ocean_color = [deep_ocean_colors[x]/len(deep_ocean_pixels) for x in range(0, 3)]
shallow_ocean_color = [shallow_ocean_colors[x]/len(shallow_ocean_pixels) for x in range(0, 3)]
land_color = [land_colors[x]/len(land_pixels) for x in range(0, 3)]

print(deep_ocean_color)
print(shallow_ocean_color)
print(land_color)

depths_map_array = map_array.copy()
final_map_array = map_array.copy()

for pixel in deep_ocean_pixels:
    i, j = pixel

    depth = sum([map_array[i][j][k] - (deep_ocean_color[k] + 1e-14) for k in range(0, 3)])/3

    depths_map_array[i][j] = [depth, depth, depth]

    final_map_array[i][j] = [deep_ocean_color[x] + depth for x in range(0, 3)]

for pixel in shallow_ocean_pixels:
    i, j = pixel

    depth = sum([map_array[i][j][k] - (shallow_ocean_color[k] + 1e-14) for k in range(0, 3)])/3

    depths_map_array[i][j] = [depth, depth, depth]

    final_map_array[i][j] = [shallow_ocean_color[x] + depth for x in range(0, 3)]

for pixel in land_pixels:
    i, j = pixel

    depth = sum([map_array[i][j][k] - (land_color[k] + 1e-14) for k in range(0, 3)])/3

    depths_map_array[i][j] = [depth, depth, depth]

    final_map_array[i][j] = [land_color[x] + depth for x in range(0, 3)]

for pixel in revision_pixels:
    i, j = pixel

depths_map_image = Image.fromarray(depths_map_array)
depths_map_image.save('devonian_depths.png')

final_map_image = Image.fromarray(final_map_array)
final_map_image.save('devonian_final.png')

##### Count Possible Errors #####
error_count = 0

for i in range(L):
    for j in range(M):
        color = map_array[i][j]
        chosen_color = edited_map_array[i][j]

        score = sum([abs(color[x] - chosen_color[x]) for x in range(0, 3)])

        print(score)

        if score / (255 * 3) > 0.9:
            error_count += 1

print(error_count)
