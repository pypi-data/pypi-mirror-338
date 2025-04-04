import os
import sys
import click

def create_folder_structure(project_name):
    """ Yaratilishi kerak bo'lgan papkalar va fayllar """
    folders = [
        "handlers", "utils", "services", "state"
    ]
    
    files = [
        "bot.py", "loader.py", ".env", ".env.example",
        "dockerfile", "docker-compose.yml", ".gitignore",
        "requirements.txt"
    ]
    
    files_structure = {
        "handlers": ["__init__.py", "start.py"],
        "utils": ["__init__.py", "texts.py", "buttons.py", "env.py"],
        "services": ["__init__.py", "services.py"],
        "state": ["__init__.py", "state.py"]
    }

    for folder in folders:
        folder_path = os.path.join(project_name, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file in files:
        with open(os.path.join(project_name, file), "w") as f:
            f.write("")

    for folder, sub_files in files_structure.items():
        for sub_file in sub_files:
            file_path = os.path.join(project_name, folder, sub_file)
            with open(file_path, "w") as f:
                if sub_file == "__init__.py":
                    f.write("from . import start\n" if folder == "handlers" else "from . import start\n" if folder == "services" else "from . import state\n")
                else:
                    f.write(f"# {sub_file} fayli\n")
    
    print(f"'{project_name}' loyihasi uchun paket struktura yaratildi!")

@click.command()
@click.argument("project_name")  # Argumentni to'g'ri qo'shish
def create(project_name):
    """ Yangi loyiha yaratish uchun komanda """
    print(f"{project_name} loyihasini yaratish uchun tasdiqlang (y/n): ")
    confirm = input().strip().lower()
    
    if confirm == "y":
        create_folder_structure(project_name)
        print(f"✅ '{project_name}' loyihasi yaratildi!")
    else:
        print("❌ Yaratish bekor qilindi.")
        sys.exit(0)

if __name__ == "__main__":
    create()
