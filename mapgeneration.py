import numpy as np
from PIL import Image

mollewide_image = Image.open("mollewide.png")
mollewide_array = np.asarray(mollewide_image)

L, M, N = np.shape(mollewide_array)
