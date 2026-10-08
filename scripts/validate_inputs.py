from pathlib import Path
import csv
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PROJECT_ROOT / "data" / "input_manifest.csv"
IMAGES_DIR = PROJECT_ROOT / "data" / "baseline_inputs"

print("Manifest:", MANIFEST_PATH)
print("Exists:", MANIFEST_PATH.is_file())

with MANIFEST_PATH.open(encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_path = IMAGES_DIR / row["filename"]

        try:
            with Image.open(image_path) as image:
                image.load()
                width, height = image.size
        except OSError as error:
            print(row['photo_id'], 'FAILED:', error)
        else:
            print(row["photo_id"], row["filename"], width, height)