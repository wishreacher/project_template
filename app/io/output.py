def print_to_console(text):
    """
    Prints the output to the console.
    """
    print(text)

def save_to_file(file_path, text):
    """
    Saves the output to a file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)