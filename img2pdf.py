# grabs all images from current folder and turns them into a pdf

from pathlib import Path
from PIL import Image

script_path = Path(__file__)
folder_name = script_path.parent.name
suggestion_name = folder_name

image_folder = Path("./")

output_pdf = input(f"Enter filename: ({suggestion_name}.pdf)\n>").strip()
if not output_pdf:
  output_pdf = f"{suggestion_name}.pdf"
else:
  if not output_pdf.lower().endswith(".pdf"):
      output_pdf += ".pdf"

input_files = sorted(
  [f for f in image_folder.iterdir() if f.suffix.lower() in {'.jpg', '.jpeg', '.png'}]
)

if input_files:
  try:
    images = [Image.open(img).convert("RGB") for img in input_files]
    output_pdf_path = Path(output_pdf)
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF created successfully: {output_pdf_path}")
  except Exception as e:
    print(f"An error occurred while creating the PDF: {e}")
else:
  print("No valid image files found in the folder.")
