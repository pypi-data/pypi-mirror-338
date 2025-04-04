# SegmentMesher

Segmentmesher is a small python-application for creating labeled 2D meshes from segmented png-images.
A few example images are located in the `resources`-folder.

To install run

```bash
pip install .
```

and to run:

```
segmentmesher -i resources/pixelbrain.png -o 2dbrain.vtu --visualize
```

which will first open a pyplot-window showing the input image, then upon closing the pyplot-window the segments will be meshed and stored to the file `2dbrain.vtu` which will be visualized in a pyvista-window.
If you drop the `--visualize`-flag nothing will be shown underways, and the mesh can be inspected by e.g. `paraview`.

To see possible arguments, run

```
segmentmesher --help
```
