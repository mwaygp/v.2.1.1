import os
import hashlib
import time

# Define a list of known malware file hashes (simplified signatures)
known_malware_hashes = {
    'malware_file_1.exe': 'hash_of_malware_file_1',
    'malware_file_2.exe': 'hash_of_malware_file_2',
    # Add more malware file hashes here
}

def calculate_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_file(filename, hash_type=None):
    """
    Scans a file for malicious activity and returns a message indicating whether any suspicious activity was found.
    """
    with open(filename, 'rb') as f:
        contents = f.read()
        
        # Check for virus signatures
        md5_hash = hashlib.md5(contents).hexdigest()
        if md5_hash in known_malware_hashes:
            return "Virus detected!"
        
        # Check for a specific hash type, if specified
        if hash_type:
            if hash_type == 'md5':
                file_hash = hashlib.md5(contents).hexdigest()
            elif hash_type == 'sha256':
                file_hash = hashlib.sha256(contents).hexdigest()
            else:
                raise ValueError("Unsupported hash type: {}".format(hash_type))

            # Prompt the user to enter a target hash to compare against
            target_hash = input("Enter target hash ({}): ".format(hash_type))
            if file_hash == target_hash:
                return "Hash match found!"
            
            return "Hash match not found."
        
        # If no malicious activity was detected, return a message indicating that the file is clean
        return "File is clean"

def md5_checksum(file_path, block_size=8192):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def scan_directory_with_progress(directory):
    total_files = 0
    scanned_files = 0

    for root, _, files in os.walk(directory):
        total_files += len(files)

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            md5_hash = md5_checksum(file_path)
            scanned_files += 1
            progress = (scanned_files / total_files) * 100
            print(f"Scanning: {file_path} | Progress: {progress:.2f}%")

if __name__ == '__main__':
    filename = input("Enter filename: ")
    if os.path.isfile(filename):
        scan_type = input("Enter scan type (virus, hash): ")
        if scan_type == 'virus':
            result = scan_file(filename)
        elif scan_type == 'hash':
            hash_type = input("Enter hash type (md5, sha256): ")
            result = scan_file(filename, hash_type)
        else:
            print("Invalid scan type.")
            exit()
        print(result)
    else:
        print("File not found.")
    
    target_directory = input("Enter the directory to scan: ")
    if os.path.isdir(target_directory):
        scan_directory_with_progress(target_directory)
        print('Scan complete.')

    # Check if any malware was found
    malware_found = False
    for root, _, files in os.walk(target_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_file_hash(file_path)
            if file_hash in known_malware_hashes.values():
                print(f'Found malware: {filename} - {file_path}')
                malware_found = True

    if not malware_found:
        print("No malware found in the scanned directory.")