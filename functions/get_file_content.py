import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    wd = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, file_path))
    
    if os.path.commonpath([wd, target]) != wd:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error: {e}"
    
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read specified file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file being read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)