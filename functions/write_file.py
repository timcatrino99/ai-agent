import os

def write_file(working_directory, file_path, content):
    wd = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(wd, file_path))

    if os.path.commonpath([wd, target]) != wd:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(target, "w") as f:
            written = f.write(content)

        return f'Successfully wrote to "{file_path}" ({written} characters written)'
    except Exception as e:
        return f'Error: {e}'