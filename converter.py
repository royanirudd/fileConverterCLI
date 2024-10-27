import argparse
import os
from datetime import datetime

VERSION = "0.1"

# Define compatible formats
COMPATIBLE_FORMATS = {
    "txt": ["md", "csv"],
    "jpg": ["png", "jpeg", "bmp"],
    "png": ["jpg", "jpeg", "bmp"],
    "md": ["txt", "html"],
}

def convert_file(filename, new_extension):
    # Extract the current file extension
    current_extension = filename.split('.')[-1]
    
    # Check compatibility
    if new_extension not in COMPATIBLE_FORMATS.get(current_extension, []):
        print(f"Error: Cannot convert from .{current_extension} to .{new_extension}.")
        return

    # Log the conversion
    log_conversion_attempt(filename, new_extension)
    
    # Conversion placeholder
    print(f"Converting {filename} to {new_extension}...")

    # Implement conversion logic here
    # For now, just simulate by renaming the file with a new extension
    base_name = '.'.join(filename.split('.')[:-1])
    new_filename = f"{base_name}.{new_extension}"
    os.rename(filename, new_filename)
    
    print(f"File converted: {new_filename}")

def log_conversion_attempt(filename, new_extension):
    with open("conversion_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: Attempted to convert {filename} to {new_extension}\n")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="File Converter Tool - Converts files to different formats based on the specified extension."
    )
    parser.add_argument("filename", nargs="?", help="The name of the file to convert")
    parser.add_argument("new_extension", nargs="?", help="The new extension for the converted file")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the conversion function if arguments are provided
    if args.filename and args.new_extension:
        convert_file(args.filename, args.new_extension)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

