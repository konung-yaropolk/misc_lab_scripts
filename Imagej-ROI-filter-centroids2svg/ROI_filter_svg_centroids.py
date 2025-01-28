import os
import zipfile
import svgwrite
from roifile import ImagejRoi
from PIL import Image
from shapely.geometry import Polygon, Point
import base64
import io

def load_points_from_first_roi(zip_path):
    points = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        first_name = zip_ref.namelist()[0]
        with zip_ref.open(first_name) as roi_file:
            roi_data = roi_file.read()
            roi = ImagejRoi.frombytes(roi_data)
            if roi.roitype == 10:  # Type 10 is for point ROIs
                points = [(int(x), int(y)) for x, y in zip(roi.coordinates()[:, 0], roi.coordinates()[:, 1])]
    return points

def load_other_rois(zip_path):
    rois = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for name in zip_ref.namelist()[1:]:  # Start from the second ROI
            with zip_ref.open(name) as roi_file:
                roi_data = roi_file.read()
                roi = ImagejRoi.frombytes(roi_data)
                rois.append(roi)
    return rois

def split_points(points, division_point):
    Vglut2 = points[:division_point]  # Elements up to the division point
    Vgat = points[division_point:]    # Elements after the division point
    return Vglut2, Vgat

def roi_contains_point(roi, x, y):
    polygon = Polygon(roi.coordinates())
    point = Point(x, y)
    return polygon.contains(point)

def calculate_centroid(roi):
    polygon = Polygon(roi.coordinates())
    centroid = polygon.centroid
    return int(centroid.x), int(centroid.y)

def sort_rois(rois, Vglut2, Vgat):
    Vglut2_rois = []
    Vgat_rois = []
    Vglut2_and_Vgat_rois = []
    neither_rois = []

    for roi in rois:
        contains_vglut2 = any(roi_contains_point(roi, x, y) for x, y in Vglut2)
        contains_vgat = any(roi_contains_point(roi, x, y) for x, y in Vgat)

        if contains_vglut2 and contains_vgat:
            Vglut2_and_Vgat_rois.append(roi)
        elif contains_vglut2:
            Vglut2_rois.append(roi)
        elif contains_vgat:
            Vgat_rois.append(roi)
        else:
            neither_rois.append(roi)

    return Vglut2_rois, Vgat_rois, Vglut2_and_Vgat_rois, neither_rois

def save_rois_to_zip(rois, zip_path):
    num_rois = len(rois)
    base_name = os.path.splitext(zip_path)[0]
    output_zip_path = f'{base_name}_({num_rois}_rois).zip'
    with zipfile.ZipFile(output_zip_path, 'w') as zip_out:
        for i, roi in enumerate(rois):
            roi_bytes = roi.tobytes()
            zip_out.writestr(f'roi_{i+1}.roi', roi_bytes)
    return output_zip_path

def create_svg_with_centroids(grouped_centroids, background_image_path, svg_path):
    # Open the background JPEG image
    image = Image.open(background_image_path)
    width, height = image.size

    # Convert the image to base64
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    jpg_data = buffer.getvalue()
    jpg_base64 = base64.b64encode(jpg_data).decode('utf-8')

    # Create the SVG file
    svg_document = svgwrite.Drawing(svg_path, size=(width, height))
    svg_document.add(svg_document.image(href=f'data:image/jpeg;base64,{jpg_base64}', insert=(0, 0), size=(width, height)))

    # Draw the centroids grouped hierarchically by categories
    groups = {
        "Vglut2": svg_document.g(id="Vglut2", fill="green", stroke="green"),
        "Vgat": svg_document.g(id="Vgat", fill="red", stroke="red"),
        "Vglut2_and_Vgat": svg_document.g(id="Vglut2_and_Vgat", fill="yellow", stroke="yellow"),
        "neither": svg_document.g(id="neither", fill="#555555", stroke="#555555")
    }

    for group, centroids in grouped_centroids.items():
        for x, y in centroids:
            groups[group].add(svg_document.circle(center=(x, y), r=8))

    for group in groups.values():
        svg_document.add(group)

    svg_document.save()

# List of input files and division points
input_files = [ 

    ['folder/your_rois_file.zip', 100],


]

for input_zip_path, division_point in input_files:
    # Ensure relative path is resolved to absolute path
    input_zip_path = os.path.abspath(input_zip_path)
    base_name = os.path.splitext(os.path.basename(input_zip_path))[0]
    output_dir = os.path.dirname(input_zip_path)
    background_image_path = f'{output_dir}/{base_name}.jpg'

    # Load the points from the first ROI
    points = load_points_from_first_roi(input_zip_path)

    # Split the points into Vglut2 and Vgat based on the division point
    Vglut2, Vgat = split_points(points, division_point)

    # Load the other ROIs
    other_rois = load_other_rois(input_zip_path)

    # Sort the ROIs into groups
    Vglut2_rois, Vgat_rois, Vglut2_and_Vgat_rois, neither_rois = sort_rois(other_rois, Vglut2, Vgat)

    # Calculate centroids for each ROI group
    Vglut2_centroids = [calculate_centroid(roi) for roi in Vglut2_rois]
    Vgat_centroids = [calculate_centroid(roi) for roi in Vgat_rois]
    Vglut2_and_Vgat_centroids = [calculate_centroid(roi) for roi in Vglut2_and_Vgat_rois]
    neither_centroids = [calculate_centroid(roi) for roi in neither_rois]

    # Group centroids
    grouped_centroids = {
        "Vglut2": Vglut2_centroids,
        "Vgat": Vgat_centroids,
        "Vglut2_and_Vgat": Vglut2_and_Vgat_centroids,
        "neither": neither_centroids
    }

    # Create an SVG file with centroids overlaid on the background image
    svg_output_path = os.path.join(output_dir, f'{base_name}_centroids.svg')
    create_svg_with_centroids(grouped_centroids, background_image_path, svg_output_path)

    print(f'Successfully saved centroids to {svg_output_path}')
