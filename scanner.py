import hashlib
import os
#from tqdm import tqdm

def scan_file(filename, hash_type=None):
    """
    Scans a file for malicious activity and returns a message indicating whether any suspicious activity was found.
    """
    with open(filename, 'rb') as f:
        contents = f.read()
        
        # Check for virus signatures
        md5_hash = hashlib.md5(contents).hexdigest()
        known_virus_signatures = ['a46e8487d8b646ec5476a551e6dc5f6a', 'ff2e56e7c77d34c02c8d8065c2e5e5a5']
        if md5_hash in known_virus_signatures:
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

# check for md5 hash 
def md5_checksum(file_path, block_size=8192):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def scan_directory(directory):
    total_files = 0
    scanned_files = 0

    for root, _, files in os.walk(directory):
        total_files += len(files)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            md5_hash = md5_checksum(file_path)
            scanned_files += 1
            progress = (scanned_files / total_files) * 100
            print(f"Scanning: {file_path} | Progress: {progress:.2f}%")

if __name__ == "__main__":
    target_directory = "/path/to/your/directory"  # Replace this with the target directory you want to scan
    scan_directory(target_directory)  


# Define a list of known malware file hashes (simplified signatures)
known_malware_hashes = {
    'malware_file_1.exe': 'hash_of_malware_file_1',
    'malware_file_2.exe': 'hash_of_malware_file_2',
    # Add more malware file hashes here
}

# Directory to scan
scan_directory = '/path/to/scan'

def calculate_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory_for_malware(directory):
    """Scan a directory for malware based on file hashes."""
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename in known_malware_hashes:
                file_hash = calculate_file_hash(file_path)
                if file_hash == known_malware_hashes[filename]:
                    print(f'Found malware: {filename} - {file_path}')
                else:
                    print(f'Suspicious file with the same name: {filename} - {file_path}')

if __name__ == '__main__':
    scan_directory_for_malware(scan_directory)          