from pathlib import Path

def write_file(file_name, file_content):
    """Writes content to a .txt file, creating it if it doesn't exist or overwriting if it does."""
    with open(str(file_name) + ".txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to an existing .txt file."""
    with open(str(file_name) + ".txt", 'a') as file:
        file.write(append_content)


def read_file(file_name):
    """Reads the content of a .txt file and returns it."""
    with open(str(file_name) + ".txt", 'r') as file:
        return file.read()


