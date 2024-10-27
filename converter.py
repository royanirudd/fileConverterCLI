import argparse
from conversion import convert_file

VERSION = "1.0"

def main():
    parser = argparse.ArgumentParser(
        description="File Converter Tool - Converts files to different formats based on the specified extension."
    )
    parser.add_argument("filename", nargs="?", help="The name of the file to convert")
    parser.add_argument("new_extension", nargs="?", help="The new extension for the converted file")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output for debugging")
    
    args = parser.parse_args()

    if args.filename and args.new_extension:
        convert_file(args.filename, args.new_extension, args.verbose)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

