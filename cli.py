import sys
import os
from model.model import Model

path = sys.argv[1]
length = int(sys.argv[2])
save_path = f"{path}/project_structure.txt"

model = Model()

structured_path = model.build_structure(path)
structure = {os.path.basename(path): structured_path}
trimmed = model.trim_dictionary(structure, length)
output = model.print_structure(trimmed)
formatted = model.format_final_output(output)


with open(f"{save_path}", 'w') as f:
    f.write(formatted)

print(f"Succesfully Saved Project Structure To: {save_path}")
