def load_file_to_string(file_path):
  """
  Reads the contents of a file and loads it into a string variable.
  
  :param file_path: Path to the file to be read.
  :return: The contents of the file as a string.
  """
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()
    return content
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")
  return None