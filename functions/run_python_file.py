import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    wd = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(wd, file_path))

    if os.path.commonpath([wd, target]) != wd:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target):
        return f'Error: File "{file_path}" not found.'
    if not target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    if not args:
        args = []
    arg_list = [str(a) for a in args]
    
    try:
        py_output = subprocess.run(["python", target, *arg_list], cwd=working_directory, capture_output=True, text=True, timeout=30)
        if (not py_output.stdout) and (not py_output.stderr):
            return "No output produced."
        out = f"STDOUT: {py_output.stdout}" + "\n" + f"STDERR: {py_output.stderr}"
        if py_output.returncode:
            out = out + "\n" + f"Process exited with code {py_output.returncode}"
        return out
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file being executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of arguments passed to the script.",
            ),
        },
        required=["file_path"]
    ),
)