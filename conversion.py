import os
from logging_module import log_conversion_attempt, log_error
from PIL import Image  

COMPATIBLE_FORMATS = {
    "txt": ["md", "csv"],
    "jpg": ["png", "jpeg", "bmp"],
    "jpeg": ["png", "jpg", "bmp"],
    "png": ["jpg", "jpeg", "bmp"],
    "md": ["txt", "html"],
}

def convert_file(filename, new_extension, verbose=False):
    if not os.path.exists(filename):
        log_error(f"File not found: {filename}")
        if verbose:
            print(f"[Error] File not found: {filename}")
        return
    
    current_extension = filename.split('.')[-1]
    
    if new_extension not in COMPATIBLE_FORMATS.get(current_extension, []):
        log_error(f"Incompatible conversion: .{current_extension} to .{new_extension}")
        if verbose:
            print(f"[Error] Cannot convert from .{current_extension} to .{new_extension}.")
        return

    log_conversion_attempt(filename, new_extension)
    
    if verbose:
        print(f"[Info] Converting {filename} to .{new_extension}...")

    # Handle different conversion types
    try:
        base_name = '.'.join(filename.split('.')[:-1])
        new_filename = f"{base_name}.{new_extension}"

        if current_extension in ["jpg", "jpeg", "png"]:
            convert_image(filename, new_filename, verbose)
        elif current_extension == "txt" and new_extension in ["md", "csv"]:
            convert_text_file(filename, new_filename, verbose)
        else:
            os.rename(filename, new_filename)  # For other simple renames

        if verbose:
            print(f"[Success] File converted: {new_filename}")
    except Exception as e:
        log_error(f"Conversion failed: {e}")
        if verbose:
            print(f"[Error] Conversion failed: {e}")

def convert_image(input_file, output_file, verbose=False):
    with Image.open(input_file) as img:
        img.save(output_file)
        if verbose:
            print(f"[Info] Image converted: {input_file} to {output_file}")

def convert_text_file(input_file, output_file, verbose=False):
    with open(input_file, "r") as infile:
        content = infile.read()
    
    if output_file.endswith(".md"):
        content = "# Markdown Conversion\n\n" + content  # Simple markdown formatting

    with open(output_file, "w") as outfile:
        outfile.write(content)
    
    if verbose:
        print(f"[Info] Text file converted: {input_file} to {output_file}")

