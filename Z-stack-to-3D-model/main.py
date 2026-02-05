# =============================================================================
#          PHYSICAL DIMENSIONS — SET THESE ACCORDING TO YOUR MICROSCOPE
# =============================================================================
# All values in micrometers (µm)
import pyvista as pv
from skimage import measure, filters
from scipy import ndimage
import tifffile
import numpy as np
pixel_size_xy_um = 0.155       # usually same for X and Y (lateral resolution)
pixel_size_z_um = 3.00        # Z-step / slice thickness / optical sectioning interval
# Example values:
#   Confocal: xy ~0.1–0.5 µm, z ~0.5–2 µm
#   Lightsheet: xy ~0.3–0.8 µm, z ~1–5 µm
#   Check microscope metadata / acquisition software export

# If you have anisotropic voxels, just set different values above
voxel_spacing = (pixel_size_xy_um, pixel_size_xy_um,
                 pixel_size_z_um)  # (dx, dy, dz)

# =============================================================================
#                               IMPORTS
# =============================================================================


def load_zstack(path_or_list, normalize=True):
    """
    Load TIFF Z-stack → shape (Z, Y, X) or (Z, Y, X, C)
    """
    if isinstance(path_or_list, str):
        stack = tifffile.imread(path_or_list)
    else:
        # List of files — assume already sorted
        stack = np.stack([tifffile.imread(f)
                         for f in sorted(path_or_list)], axis=0)

    stack = stack.astype(np.float32)

    if normalize:
        stack = (stack - stack.min()) / (stack.max() - stack.min() + 1e-8)

    print(f"Loaded shape: {stack.shape}  dtype: {stack.dtype}")
    print(
        f"Physical voxel size set to: XY = {voxel_spacing[0]:.3f} µm, Z = {voxel_spacing[2]:.3f} µm")

    return stack


def preprocess_volume(volume, sigma=2.0, threshold_method='otsu'):
    """Gaussian smoothing + automatic thresholding"""
    if sigma > 0:
        volume = ndimage.gaussian_filter(volume, sigma=sigma)

    if threshold_method == 'otsu':
        from skimage.filters import threshold_otsu
        thresh = threshold_otsu(volume)
    elif threshold_method == 'li':
        from skimage.filters import threshold_li
        thresh = threshold_li(volume)
    else:
        thresh = np.percentile(volume, 50)

    print(f"Threshold value: {thresh:.3f}")
    binary = volume > thresh
    return binary.astype(np.float32), thresh


def extract_surface(volume, level=0.0, step_size=1):
    """Marching Cubes from scikit-image"""
    verts, faces, _, _ = measure.marching_cubes(
        volume,
        level=level,
        step_size=step_size,
        # allow_larger=True
    )
    print(f"Mesh created → {len(verts):,} vertices, {len(faces):,} faces")
    return verts, faces


def create_physical_mesh(verts, faces, voxel_spacing):
    """
    Scale vertex coordinates to physical units (µm)
    Verts from marching_cubes are in voxel indices: (z, y, x)
    """
    verts_phys = verts.astype(np.float64).copy()

    # Order: marching_cubes returns (z, y, x) — match voxel_spacing (dx, dy, dz)
    verts_phys[:, 0] *= voxel_spacing[2]   # Z
    verts_phys[:, 1] *= voxel_spacing[1]   # Y
    verts_phys[:, 2] *= voxel_spacing[0]   # X

    # Create PyVista mesh
    mesh = pv.PolyData(verts_phys)
    mesh.faces = np.hstack([np.full((len(faces), 1), 3), faces]).ravel()
    mesh = mesh.compute_normals()

    return mesh


def visualize_and_export(mesh, output_stl="model_physical.stl", show=True):
    """Visualize and save STL with physical scaling already applied"""
    if show:
        plotter = pv.Plotter()
        plotter.add_mesh(mesh, color='ivory', show_edges=False, opacity=0.95)
        plotter.add_axes(labels_off=True)
        plotter.add_text(f"Spacing: XY={voxel_spacing[0]:.2f} µm, Z={voxel_spacing[2]:.2f} µm",
                         position='upper_edge', font_size=11)
        plotter.show_grid()
        plotter.show()

    mesh.save(output_stl)
    print(f"Saved physical STL: {output_stl}")
    print(f"Model bounding box (µm): {mesh.bounds}")


# ────────────────────────────────────────────────
#                   MAIN PIPELINE
# ────────────────────────────────────────────────

if __name__ == "__main__":
    # ============= CHANGE THIS =============
    # or list of files: glob.glob("folder/*.tif")
    filepath = "..\\2-photon\\Kavita Injection tdTomato\\9062-3\\Field_1_overview_crop_registered"
    # ========================================

    # 1. Load data
    volume = load_zstack(filepath + ".tif", normalize=True)

    # 2. Preprocess
    binary_vol, thresh = preprocess_volume(
        volume,
        sigma=1.5,
        threshold_method='otsu'
    )

    # 3. Extract isosurface (in voxel coordinates)
    verts_vox, faces = extract_surface(
        binary_vol,
        level=0.1,
        step_size=1          # 1 = full res, 2–4 = faster & lighter mesh
    )

    # 4. Scale to physical units & create mesh
    mesh = create_physical_mesh(verts_vox, faces, voxel_spacing)

    # 5. Visualize & export
    visualize_and_export(
        mesh, output_stl="..\\2-photon\\Kavita Injection tdTomato\\9062-3\\Field_1_overview_crop_registered" + '.stl', show=False)
