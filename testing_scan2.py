import os
import hashlib

# Define dictionaries for known malicious signatures
known_virus_signatures = {
    'virus_file_1.exe': 'hash_of_virus_file_1',
    'virus_file_2.exe': 'hash_of_virus_file_2',
    # Add more virus file hashes here
}

known_spyware_signatures = {
    'spyware_file_1.exe': 'hash_of_spyware_file_1',
    'spyware_file_2.exe': 'hash_of_spyware_file_2',
    # Add more spyware file hashes here
}

known_rootkit_signatures = {
    'rootkit_file_1.exe': 'hash_of_rootkit_file_1',
    'rootkit_file_2.exe': 'hash_of_rootkit_file_2',
    # Add more rootkit file hashes here
}

def calculate_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_file(filename, scan_type=None):
    """
    Scans a file for malicious activity and returns a message indicating whether any suspicious activity was found.
    """
    with open(filename, 'rb') as f:
        contents = f.read()
        
        # Check for virus signatures
        md5_hash = hashlib.md5(contents).hexdigest()
        if scan_type == 'virus' and md5_hash in known_virus_signatures:
            return f"Virus detected in: {filename}"
        
        # Check for spyware signatures
        if scan_type == 'spyware' and md5_hash in known_spyware_signatures:
            return f"Spyware detected in: {filename}"

        # Check for rootkit signatures
        if scan_type == 'rootkit' and md5_hash in known_rootkit_signatures:
            return f"Rootkit detected in: {filename}"

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

def scan_directory_with_progress(directory, scan_type):
    total_files = 0
    scanned_files = 0
    malware_count = 0
    malware_paths = []

    for root, _, files in os.walk(directory):
        total_files += len(files)

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            md5_hash = md5_checksum(file_path)
            scanned_files += 1
            progress = (scanned_files / total_files) * 100
            print(f"Scanning: {file_path} | Progress: {progress:.2f}%")

            # Scan the file based on the specified scan type
            result = scan_file(file_path, scan_type)
            if result != "File is clean":
                malware_count += 1
                malware_paths.append(file_path)
                print(result)

    # Display the number of scanned files and indicate whether malware was found
    print(f'Scan completed. Scanned {scanned_files} files.')
    
    if malware_count > 0:
        print(f'Malware found = {malware_count}')
        for path in malware_paths:
            print(f"File path has malware: {path}")
    else:
        print("File path empty")

def scan_single_file(file_path, scan_type):
    if os.path.isfile(file_path):
        result = scan_file(file_path, scan_type)
        print(result)
        if result != "File is clean":
            print("Malware found = 1")
            print(f"File path has malware: {file_path}")
    else:
        print("File not found.")

def run_scan():
    while True:
        print("\nChoose an option:")
        print("1. Scan a directory")
        print("2. Scan a single file")
        print("3. Exit")
        option = input("Enter your choice (1/2/3): ").strip()

        if option == "1":
            target_directory = input("Enter the directory to scan: ")
            if os.path.isdir(target_directory):
                scan_type = input("Enter scan type (virus, spyware, rootkit): ")
                if scan_type not in ['virus', 'spyware', 'rootkit']:
                    print("Invalid scan type.")
                    continue
                scan_directory_with_progress(target_directory, scan_type)
            else:
                print("Directory not found.")
        elif option == "2":
            file_path = input("Enter the path to the file to scan: ")
            scan_type = input("Enter scan type (virus, spyware, rootkit): ")
            if scan_type not in ['virus', 'spyware', 'rootkit']:
                print("Invalid scan type.")
                continue
            scan_single_file(file_path, scan_type)
        elif option == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    run_scan()

