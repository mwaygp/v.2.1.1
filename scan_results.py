import os
import hashlib
import time

# Define a list of known malware file hashes (simplified signatures)
known_malware_hashes = {
    'malware_file_1.exe': 'hash_of_malware_file_1',
    'malware_file_2.exe': 'hash_of_malware_file_2',
    # Add more malware file hashes here
}

# Directory to scan
scan_directory = 'C:\\Users\\mpc\\Documents\\File scanner with python'

def calculate_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory_for_malware(directory):
    """Scan a directory for malware based on file hashes."""
    total_files = 0
    scanned_files = 0

    for root, _, files in os.walk(directory):
        total_files += len(files)

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename in known_malware_hashes:
                file_hash = calculate_file_hash(file_path)
                if file_hash == known_malware_hashes[filename]:
                    print(f'Found malware: {filename} - {file_path}')
                else:
                    print(f'Suspicious file with the same name: {filename} - {file_path}')

            scanned_files += 1
            progress_percentage = (scanned_files / total_files) * 100
            print(f'Scanning: {file_path} | Progress: {progress_percentage:.2f}%')

if __name__ == '__main__':
    scan_directory_for_malware(scan_directory)
    print('Scan complete.')