import os

from crewai.tools import tool

@tool
def list_project_files(project_path: str) -> list[str]:
    """Lists all files from the provided project directory.

    Args:
        project_path (str): Path to the project directory

    Returns:
        list[str]: List of file paths
    """
    if not os.path.isdir(project_path):
        return [f"Error: Directory '{project_path}' does not exist"]

    file_list = []
    for root, _, files in os.walk(project_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


@tool
def read_file_content(file_path: str) -> str:
    """Reads file content.

    Args:
        file_path (str): Path to the file (UTF-8 encoded)

    Returns:
        str: File content or error message
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"
