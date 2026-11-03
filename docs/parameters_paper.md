# Tracking parameters used in the CytoTactix paper

Ultrack tracking parameters per dataset, as used in the distributed runs of the CytoTactix manuscript
(Cell Tracking Challenge benchmarks and the UTSE lightsheet analysis). This table was previously Supplementary
Table 5 of the manuscript.

The Cell Tracking Challenge columns reproduce Ultrack's published examples for the same datasets (for
Fluo-N3DL-TRIC, the configuration without optical flow). The lightsheet column is the lightsheet analysis
configuration. Unlisted parameters use the Ultrack defaults.

| Parameter | Fluo-N2DL-HeLa | Fluo-N3DL-TRIC | Lightsheet (cancer cells) |
|---|---|---|---|
| Input | CTC `ERR_SEG` labels | raw images<sup>a</sup> | Cellpose labels, center patch |
| Temporal binning | 1 | 1 | 10 |
| Contour blur σ<sub>xy</sub> / σ<sub>t</sub> | 4 px / 0 | –<sup>a</sup> | 1 px / 1.2<sup>b</sup> |
| `min_area` / `max_area` | 50 / 950 | 250 / 15000 | 30 / 600 |
| `max_noise` | default | default | 0.2 |
| `max_distance` | 25 | 20 | 15<sup>c</sup> |
| `max_neighbors` | default | 5 | 5 |
| `appear_weight` | −1 | −0.01 | −1 |
| `disappear_weight` | −1 | −0.001 | −1 |
| `division_weight` | −0.1 | 0 | −1 |
| `power` / `bias` | 4 / −0.001 | default | 4 / 0 |
| `solution_gap` | 0.0 | default | 0.01 |
| `window_size` / `overlap_size` | 100<sup>d</sup> / 5<sup>d</sup> | 70 / 5 | 20 / 5 |

<sup>a</sup> Fluo-N3DL-TRIC provides no segmentation for tracking-only use; as in Ultrack's example, foreground and
contour maps were computed from the images (contour smoothing σ = 3).
<sup>b</sup> Earlier contour preparation, which fragments nuclei; the lightsheet run is to be repeated with the
HeLa setting.
<sup>c</sup> Linking distance widened for the 10-fold temporal binning (5 px at 10 s per frame).
<sup>d</sup> Setting added for distributed execution.

Areas are in px (2D) or voxels (3D); distances in px.
