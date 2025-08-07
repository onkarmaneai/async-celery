import os

folders = [
    "app/controller",
    "app/services",
    "app/workers",
    "app/config",
    "app/utils",
    "app/output",
]

files = {
    "app/main.py": "",
    "app/controller/pdf_controller.py": "",
    "app/services/pdf_service.py": "",
    "app/workers/tasks.py": "",
    "app/config/settings.py": "",
    "app/utils/logger.py": "",
    "requirements.txt": ""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully.")
