import os

PATH = "test1"
LENGTH = 3


def build_structure(path):

    structure = {}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            structure[item] = build_structure(item_path)
        else:
            structure[item] = None

    sorted_structure = dict(
        sorted(structure.items(),
               key=lambda item: not isinstance(item[1], dict))
    )

    return sorted_structure


def trim_dictionary(structure):
    for _, val in list(structure.items()):  
        
        if isinstance(val, dict):
            
            if len(val) - 1 > LENGTH:
                for k in list(val.keys())[LENGTH:]:
                    del val[k]

            trim_dictionary(val)

def print_structure(structure, prefix="", root=True):
    output = ""

    items = list(structure.items())
    for i, (name, content) in enumerate(items):
        is_last = i == len(items) - 1

        connector = "└── " if not root and is_last else (
            "├── " if not root else "")

        if isinstance(content, dict):
            output += f"{prefix}{connector}{name}/\n"
            new_prefix = prefix + \
                ("" if root else ("    " if is_last else "│   "))
            output += print_structure(content, new_prefix, root=False)
        else:
            output += f"{prefix}{connector}{name}\n"

    return output


file_structure = {os.path.basename(PATH): build_structure(PATH)}

trim_dictionary(file_structure)

output = print_structure(file_structure)
print(f"```\n{output}```")