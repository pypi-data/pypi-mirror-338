from pathlib import Path
from PIL import Image

import numpy as np

from segmentmesher.geometry import (
    find_segment_contours,
    mesh_contours,
    label_mesh,
    fill_missing,
)


def segmentmesher(
    input: Path | str,
    output: Path | str,
    keep_outside: bool = False,
    edge_length_r: float = 0.05,
    binary: bool = False,
    visualize: bool = False,
):
    img = read_img(input)

    label_contours = find_segment_contours(img)
    mesh = mesh_contours(
        label_contours, cut_outside=not keep_outside, edge_length_r=edge_length_r
    )
    mesh.cell_data["labels"] = label_mesh(mesh, label_contours)
    mesh = fill_missing(mesh)
    mesh.cast_to_unstructured_grid().save(output, binary)
    if visualize:
        import matplotlib.pyplot as plt

        plt.imshow(img)
        plt.colorbar()
        plt.show()
        mesh.plot(show_edges=True)


def read_img(file_path):
    img = Image.open(file_path)
    img = img.convert("L")
    pixel_array = np.array(img)
    label_array = np.zeros_like(pixel_array)
    for idx, label in enumerate(np.unique(pixel_array)):
        label_array[pixel_array == label] = idx
    return label_array
