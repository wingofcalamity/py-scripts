# grabs all images from current folder and turns them into a pdf

from pathlib import Path
from PIL import Image

script_path = Path(__file__)
folder_name = script_path.parent.name
suggestion_name = folder_name.replace(" ", "_")

image_folder = Path("./")

output_pdf = input(f"Enter filename: (Default: {suggestion_name}.pdf)\n>").strip()
if not output_pdf:
  output_pdf = f"{suggestion_name}.pdf"

image_files = sorted(
  [f for f in image_folder.iterdir() if f.suffix.lower() in {'.jpg', '.jpeg', '.png'}]
)


if image_files:
    images = [Image.open(img).convert("RGB") for img in image_files]
    output_pdf_path = Path(output_pdf).with_suffix(".pdf")
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    
    print(f"PDF created successfully: {output_pdf_path}")
else:
    print("No valid image files found in the folder.")
