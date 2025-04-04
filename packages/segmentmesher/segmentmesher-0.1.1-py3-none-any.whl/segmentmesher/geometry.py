import numpy as np
import pyvista as pv
import skimage
import wildmeshing as wm


def as_grid(contour_line, close=True):
    if np.allclose(contour_line[0], contour_line[-1]):
        contour_line = contour_line[:-1]
    n = len(contour_line)
    return {
        "points": contour_line,
        "edges": np.array([[i % n, (i + 1) % n] for i in range(n - (1 * (not close)))]),
    }


def vtk_connectivity(cells: np.ndarray):
    return np.hstack([[cells.shape[1]] + list(cell) for cell in cells])


def as_3d(points):
    return np.concatenate(
        [points] + [np.zeros((points.shape[0], 1))] * (3 - points.shape[1]), axis=1
    )


def connectivity_matrix(vtk_array: np.ndarray):
    connectivity_list = []
    idx = 0
    total_length = len(vtk_array)
    while idx < total_length:
        num_points = vtk_array[idx]
        idx += 1
        point_indices = vtk_array[idx : idx + num_points]
        connectivity_list.append(point_indices.tolist())
        idx += num_points
    return connectivity_list


def contour_union(grids):
    grid_lengths = [0, *np.cumsum([len(g["points"]) for g in grids])]
    return {
        "points": np.concatenate([g["points"] for g in grids]),
        "edges": np.concatenate(
            [g["edges"] + grid_lengths[idx] for idx, g in enumerate(grids)]
        ),
    }


def to_pyvista_grid(grid):
    return pv.PolyData(as_3d(grid["points"]), lines=vtk_connectivity(grid["edges"]))


def label_grid(grid, value):
    grid.cell_data["label"] = value
    grid.point_data["label"] = value
    return grid


def find_segment_contours(img):
    labels = sorted(np.unique(img))
    label_contours = {}
    # canvas = np.zeros((img.shape[0] + 2, img.shape[0] + 2), dtype=img.dtype)
    # canvas[1:-1, 1:-1] = img
    for idx, val in enumerate(labels):
        mask = (img == val).astype(bool)
        contours = skimage.measure.find_contours(mask)
        label_contours[int(val)] = [as_grid(line) for line in contours]
    return label_contours


def compute_winding_number(grid, P):
    V = grid["points"]
    U = V[np.newaxis, ...] - P[:, np.newaxis, :]
    Ue = U[:, grid["edges"]]
    X = np.cross(Ue[..., 0, :], Ue[..., 1, :], axis=-1)
    D = (Ue[..., 0, :] * Ue[..., 1, :]).sum(axis=-1)
    return np.arctan2(X, D).sum(axis=-1) / (2 * np.pi)


def label_mesh(mesh, label_contours):
    P = np.asarray(mesh.cell_centers().points)[:, :2]
    cell_labels = np.zeros(P.shape[0], dtype=int)
    for label, contours in label_contours.items():
        grid_union = contour_union(contours)
        winding_nums = np.rint(compute_winding_number(grid_union, P)).astype(int)
        cell_labels[winding_nums % 2 != 0] = label
    return cell_labels


def mesh_contours(label_contours, **kwargs):
    contour_soup = contour_union(
        [contour_union(contours) for contours in label_contours.values()]
    )
    vs, tris, marker, nomarker = wm.triangulate_data(
        contour_soup["points"], contour_soup["edges"], **kwargs
    )
    return pv.PolyData(as_3d(vs), vtk_connectivity(tris))


def fill_missing(mesh):
    cells = np.argwhere(mesh["labels"] == 0).flatten()
    for cell in cells:
        cell_neighbour_labels = mesh["labels"][
            mesh.cell_neighbors(cell, connections="edges")
        ]
        values, counts = np.unique(cell_neighbour_labels, return_counts=True)
        mesh["labels"][cell] = values[counts.argmax()]
    return mesh
