import os
from PIL import Image
from PIL.ExifTags import TAGS

# Replace 'path_to_top_folder' with the path to your top-level folder containing subfolders with images.
# 用文本编辑器打开脚本，并将'path_to_top_folder'变量设置为包含您图片的文件夹路径。
top_folder_path = r'path_to_top_folder'

# Function to extract the DateTimeOriginal EXIF data
def get_exif_datetime_original(img_path):
    try:
        image = Image.open(img_path)
        exif_data = {
            TAGS[key]: value
            for key, value in image._getexif().items()
            if key in TAGS and TAGS[key] == 'DateTimeOriginal'
        }
        return exif_data.get('DateTimeOriginal')
    except Exception as e:
        print(f"Error extracting EXIF data from {img_path}: {e}")
        return None

# Function to recursively rename images with the DateTimeOriginal as prefix
def rename_images_with_datetime(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                img_path = os.path.join(root, filename)
                datetime_original = get_exif_datetime_original(img_path)
                if datetime_original:
                    # Format the datetime for filename (replace ":" with "-" and " " with "_")
                    datetime_formatted = datetime_original.replace(':', '-').replace(' ', '_')
                    new_filename = f"{datetime_formatted}_{filename}"
                    new_path = os.path.join(root, new_filename)
                    os.rename(img_path, new_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")

# Start the renaming process
rename_images_with_datetime(top_folder_path)
