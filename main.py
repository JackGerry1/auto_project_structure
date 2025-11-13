import os

PATH = "/home/jack/Documents/Work/Job Applications/Anima International Prep/reactProject/src"


def build_structure(path: str) -> dict:

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


def trim_dictionary(structure: dict, max_length: int) -> dict:
    trimmed = {}
    for key, val in structure.items():
        if isinstance(val, dict):
            sub = trim_dictionary(val, max_length)
            trimmed[key] = dict(list(sub.items())[:max_length])
        else:
            trimmed[key] = val

    return trimmed


def print_structure(structure: dict, prefix="", root=True) -> str:
    output = ""

    items = list(structure.items())
    for i, (name, content) in enumerate(items):
        is_last = i == len(items) - 1

        connector = "" if root else ("├── " if not is_last else "└── ")

        if isinstance(content, dict):
            output += f"{prefix}{connector}{name}/\n"
            new_prefix = prefix + ("" if root else "│   ")
            output += print_structure(content, new_prefix, root=False)
        else:
            output += f"{prefix}{connector}{name}\n"

    return output


def main(): 
    file_structure = {os.path.basename(PATH): build_structure(PATH)}

    length = 10

    cleaned_structure = trim_dictionary(file_structure, length)

    output = print_structure(cleaned_structure)
    final_output = f"```\n{output}```"
    
    print(final_output)

main()
