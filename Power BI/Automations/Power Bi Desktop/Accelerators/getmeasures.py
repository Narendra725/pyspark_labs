import re

# Path to your .tmdl file
tmdl_file = r"C:\Nahdi-articrafts\base_articrafts\Measures\Measures Table.tmdl"

# Function to extract measures and their display folders
def extract_measures_and_folders(content):
    # Regular expression to capture measure name and display folder
    measure_pattern = re.compile(r"measure '(.*?)' = .*?displayFolder: (.*?)\n", re.DOTALL)
    
    # Find all matches
    matches = measure_pattern.findall(content)
    
    # Print each measure with its display folder
    for measure, folder in matches:
        print(f"Measure: {measure}\nDisplay Folder: {folder}\n")

# Open and read the .tmdl file
try:
    with open(tmdl_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract and display measures and folders
    extract_measures_and_folders(content)

except Exception as e:
    print(f"Error reading the file: {e}")
