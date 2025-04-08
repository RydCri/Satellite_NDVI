import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndvi(nir, red):
    """Calculates the Normalized Difference Vegetation Index."""
    numerator = nir - red
    denominator = nir + red
    ndvi = np.where(denominator != 0, numerator / denominator, 0)
    return ndvi

def calculate_ndvi_change_from_tiffs(tiff1_nir_path, tiff1_red_path, tiff2_nir_path, tiff2_red_path, output_path=None):
    """Calculates the NDVI change between two sets of NIR and Red TIFF images."""
    try:
        with rasterio.open(tiff1_nir_path) as src1_nir, rasterio.open(tiff1_red_path) as src1_red, \
                rasterio.open(tiff2_nir_path) as src2_nir, rasterio.open(tiff2_red_path) as src2_red:

            nir1 = src1_nir.read(1).astype('float32')
            red1 = src1_red.read(1).astype('float32')
            nir2 = src2_nir.read(1).astype('float32')
            red2 = src2_red.read(1).astype('float32')

            ndvi1 = calculate_ndvi(nir1, red1)
            ndvi2 = calculate_ndvi(nir2, red2)

            ndvi_change = ndvi2 - ndvi1

            if output_path:
                profile = src1_nir.profile  # Use profile from one of the TIFFs
                with rasterio.open(output_path, 'w', **profile) as dst:
                    dst.write(ndvi_change, 1)

            return ndvi_change, src1_nir.profile

    except rasterio.RasterioIOError as e:
        print(f"Error opening file: {e}")
        return None, None

def visualize_ndvi_change(ndvi_change, loc, output_plot_path=None):
    """Plot cmap visualizes lowest values in Red, med in Yellow, Hi in Green."""

    if ndvi_change is not None:
        plt.figure(figsize=(10, 8))
        plt.imshow(ndvi_change, cmap='RdYlGn')
        plt.colorbar(label='NDVI Change')
        plt.title(f'NDVI Change Detection - {loc}')
        if output_plot_path:
            plt.savefig(output_plot_path)
        else:
            plt.show()
        plt.close()


# --- Main Processing ---
data_dir = "./Onera Satellite Change Detection dataset - Images/"
locations = []
output_dir = os.path.join('./output')
os.makedirs(output_dir, exist_ok=True)

for locs in os.listdir(data_dir):
    locations.append(locs)
print(locations)

for location in locations:
    location_dir = os.path.join(data_dir, location)
    imgs1_rect_dir = os.path.join(location_dir, "imgs_1_rect")
    print(imgs1_rect_dir)
    imgs2_rect_dir = os.path.join(location_dir, "imgs_2_rect")

    if os.path.isdir(imgs1_rect_dir) and os.path.isdir(imgs2_rect_dir):
        nir_file_1 = next((f for f in os.listdir(imgs1_rect_dir) if f.endswith(".tif") and "B08" in f), None)
        red_file_1 = next((f for f in os.listdir(imgs1_rect_dir) if f.endswith(".tif") and "B04" in f), None)
        nir_file_2 = next((f for f in os.listdir(imgs2_rect_dir) if f.endswith(".tif") and "B08" in f), None)
        red_file_2 = next((f for f in os.listdir(imgs2_rect_dir) if f.endswith(".tif") and "B04" in f), None)

        if nir_file_1 and red_file_1 and nir_file_2 and red_file_2:
            tiff1_nir_path = os.path.join(imgs1_rect_dir, nir_file_1)
            tiff1_red_path = os.path.join(imgs1_rect_dir, red_file_1)
            tiff2_nir_path = os.path.join(imgs2_rect_dir, nir_file_2)
            tiff2_red_path = os.path.join(imgs2_rect_dir, red_file_2)

            output_ndvi_change_path = os.path.join(location_dir, f"ndvi_change_{location}_rect_date1_vs_date2.tiff")
            # output_plot_path = os.path.join(location_dir, f"ndvi_change_plot_{location}_rect_date1_vs_date2.png")
            output_plot_path = os.path.join(output_dir, f"ndvi_change_plot_{location}_rect_date1_vs_date2.png")

            ndvi_change_data, profile = calculate_ndvi_change_from_tiffs(
                tiff1_nir_path, tiff1_red_path, tiff2_nir_path, tiff2_red_path,
                output_path=output_ndvi_change_path
            )

            if ndvi_change_data is not None:
                print(f"NDVI change calculated for {location} (using _rectified B08 and B04 bands)")
                visualize_ndvi_change(ndvi_change_data, profile, output_plot_path)
                print(f"NDVI change visualization saved to {output_plot_path}")
        else:
            print(f"Error: Could not find B08 (NIR) and B04 (Red) TIFF files in imgs_1_rect or imgs_2_rect for {location}")
    else:
        print(f"Warning: imgs_1_rect or imgs_2_rect directory not found in {location}")

print("Processing complete.")