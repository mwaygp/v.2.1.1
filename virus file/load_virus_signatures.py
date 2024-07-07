def load_virus_signatures(signature_file):
    signatures = {}
    with open(signature_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                filename, file_hash = line.split()
                signatures[filename] = file_hash
    return signatures

# Specify the path to your virus signatures text file
virus_signatures_file = 'virus_signatures.txt'

# Load virus signatures from the file
known_virus_signatures = load_virus_signatures(virus_signatures_file)