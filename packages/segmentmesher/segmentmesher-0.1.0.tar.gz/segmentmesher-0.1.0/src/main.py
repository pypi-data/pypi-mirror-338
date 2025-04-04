from pathlib import Path
import click

from segmentmesher.mesh import segmentmesher


@click.command("segmentmesher")
@click.option("--input", "-i", type=Path, required=True)
@click.option("--output", "-o", type=Path, required=True)
@click.option("--keep_outside", "-k", is_flag=True)
@click.option("--edge_length_r", "-r", type=float, default=0.01)
@click.option("--visualize", is_flag=True)
def segmentmesher_cli(**kwargs):
    segmentmesher(**kwargs)
