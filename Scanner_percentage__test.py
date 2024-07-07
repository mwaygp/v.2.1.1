import os
import time

# Directory to scan
scan_directory = 'C:\\Users\\mpc\\Documents\\File scanner with python'

def scan_directory_with_progress(directory):
    total_files = 0
    scanned_files = 0

    # Count the total number of files to scan
    for _, _, files in os.walk(directory):
        total_files += len(files)

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Simulate scanning by sleeping for a short time
            time.sleep(0.1)

            # Calculate the progress percentage
            scanned_files += 1
            progress_percentage = (scanned_files / total_files) * 100

            # Display the loading percentage
            print(f'Scanning: {filename} ({progress_percentage:.2f}% complete)')

if __name__ == '__main__':
    scan_directory_with_progress(scan_directory)
    print('Scan complete.')