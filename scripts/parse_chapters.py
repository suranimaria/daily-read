import re
import os

def split_chapters_from_output(file_path: str, output_dir: str):
    """
    Split the content of the provided text file into separate chapters based on specific patterns.
    
    :param file_path: Path to the input text file.
    :param output_dir: Directory where individual chapter files will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_file = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        
        # Check if the line contains only numbers
        if re.match('^[0-9]+$', line):
            continue

        # Check if the line matches pattern e.g. "A123!"
        elif re.match("^[A-Z]+[0-9]+!$", line):
            if current_file:
                current_file.close()
            
            chapter_num = re.findall(r'[0-9]+', line)[0]
            current_file = open(os.path.join(output_dir, f'maurelius_{chapter_num}.txt'), 'w')
        
        # Write to the current chapter file
        else:
            if current_file:
                current_file.write(line + "\n")

    # Close the last opened chapter file
    if current_file:
        current_file.close()


if __name__ == "__main__":
    input_path = 'your-path/DailyRead/output/output.txt'
    chapter_dir = 'your-path/DailyRead/chapters/maurelius'
    split_chapters_from_output(input_path, chapter_dir)
