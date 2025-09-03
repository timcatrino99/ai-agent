import os

def get_files_info(working_directory, directory="."):
    wd = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, directory))
    
    if os.path.commonpath([wd, target]) != wd:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory'
    
    try:
        entries = os.listdir(target)
        entries = [e for e in entries if e != "__pycache__"]
        files = sorted([x for x in entries if os.path.isfile(os.path.join(target, x))])
        dirs = sorted([x for x in entries if os.path.isdir(os.path.join(target, x))])
        entries = files + dirs

        lines = []
        for item in entries:
            target_item = os.path.join(target, item)
            file_size = os.path.getsize(target_item)
            is_dir = os.path.isdir(target_item)
            lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {e}"
    return "\n".join(lines)