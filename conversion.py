import os
from logging_module import log_conversion_attempt, log_error

COMPATIBLE_FORMATS = {
    "txt": ["md", "csv"],
    "jpg": ["png", "jpeg", "bmp"],
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

    base_name = '.'.join(filename.split('.')[:-1])
    new_filename = f"{base_name}.{new_extension}"
    
    try:
        os.rename(filename, new_filename)
        if verbose:
            print(f"[Success] File converted: {new_filename}")
    except Exception as e:
        log_error(f"Conversion failed: {e}")
        if verbose:
            print(f"[Error] Conversion failed: {e}")

