from datetime import datetime

def log_conversion_attempt(filename, new_extension):
    with open("conversion_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: Attempted to convert {filename} to {new_extension}\n")

def log_error(message):
    with open("conversion_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: [Error] {message}\n")

