from pathlib import Path

assets_directory = Path("assets")
file_name = "x.csv"
file_path = assets_directory / file_name
print(file_path)