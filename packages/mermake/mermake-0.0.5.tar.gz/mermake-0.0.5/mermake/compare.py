import numpy as np
import napari


tile = np.load('tile_pad.npz')['arr_0']
print(tile.shape)
image = np.load('image_pad.npz')['arr_0']
print(image.shape)
viewer = napari.Viewer()
viewer.add_image(tile, name='tile')
viewer.add_image(image, name='image')
napari.run()
