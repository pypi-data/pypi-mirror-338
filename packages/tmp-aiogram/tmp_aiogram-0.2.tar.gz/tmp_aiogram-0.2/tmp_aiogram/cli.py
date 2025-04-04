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
            if file == "Dockerfile":
                f.write("# FROM baseImage\nFROM python:3.9-slim\n")
            elif file == ".gitignore":
                f.write("""
# Django #
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files #
*.bak

# If you are using PyCharm #
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python #
*.py[cod] 
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.whl
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text #
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files
PackageControl.last-run
PackageControl.ca-list
PackageControl.ca-bundle
PackageControl.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code #
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history

""")
                
            else:
                f.write(f"# {file} fayli\n")
                

    for folder, sub_files in files_structure.items():
        for sub_file in sub_files:
            file_path = os.path.join(project_name, folder, sub_file)
            with open(file_path, "w") as f:
                if sub_file == "__init__.py":
                    if folder == "handlers":
                        f.write("from . import start\n")
                    elif folder == "utils":
                        f.write("from . import texts, buttons, env\n")
                    elif folder == "services":
                        f.write("from . import services\n")
                    elif folder == "state":
                        f.write("from . import state\n")
                else:
                    f.write(f"# {sub_file} fayli\n")
    
    print(f"'{project_name}' loyihasi uchun paket struktura yaratildi!")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"



@click.command()
@click.argument("project_name")  
def create(project_name):
    """ Yangi loyiha yaratish uchun komanda """
    print(YELLOW + f"{project_name} loyihasini yaratish uchun tasdiqlang (y/n): " + RESET)
    confirm = input().strip().lower()
    
    if confirm == "y":
        create_folder_structure(project_name)
        print(GREEN + f"✅ '{project_name}' loyihasi yaratildi!" + RESET)
    else:
        print(RED + "❌ Yaratish bekor qilindi." + RESET)
        sys.exit(0)

if __name__ == "__main__":
    create()
