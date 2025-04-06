import os
import argparse
import shutil
import re
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

ESTRUTURA = {
    "src": ["app", "core", "integracoes", "utils", "api"],
    "config": [],
    "dados": [],
    "logs": [],
    "tests": [],
}

ARQUIVOS_BASE = [
    "requirements.txt",
    "README.md",
    "main.py",
    ".env",
    "Dockerfile",
    ""
]

def validar_nome_projeto(nome):
    """Verifica se o nome do projeto é válido (sem espaços e caracteres especiais)."""
    if re.match(r'^[a-zA-Z0-9_-]+$', nome):
        return True
    print("Erro: O nome do projeto contém caracteres inválidos! Use apenas letras, números, hífens ou underscores.")
    return False

def criar_arquitetura(caminho_base, criar_venv=True, inicializar_git_flag=False):
    """Cria a estrutura do projeto no caminho especificado."""
    if not os.path.exists(caminho_base):
        os.makedirs(caminho_base)

    for pasta, subpastas in ESTRUTURA.items():
        pasta_path = os.path.join(caminho_base, pasta)
        os.makedirs(pasta_path, exist_ok=True)
        print(Fore.YELLOW + f"🔧 Pasta {pasta} criada com sucesso")
        for subpasta in subpastas:
            subpasta_path = os.path.join(pasta_path, subpasta)
            os.makedirs(subpasta_path, exist_ok=True)
            print(Fore.YELLOW + f"🔧 Subpasta {subpasta} criada com sucesso")
            with open(os.path.join(subpasta_path, "__init__.py"), "w", encoding="utf-8") as f:
                f.write("")

    for arquivo in ARQUIVOS_BASE:
        caminho_arquivo = os.path.join(caminho_base, arquivo)
        print(Fore.YELLOW + f"🔧 O {arquivo} foi criado com sucesso...")
        if not os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                if arquivo == "README.md":
                    f.write(f"""
# Projeto

## Estrutura do Projeto

O projeto segue a seguinte estrutura de diretórios:

```
    ├── src/                # Código-fonte principal
    │   ├── app/            # Aplicação principal
    │   ├── core/           # Módulos essenciais e configurações
    │   ├── integracoes/    # Integrações com serviços externos
    │   ├── utils/          # Funções utilitárias
    │   ├── api/            # Endpoints da API
    ├── config/             # Arquivos de configuração
    ├── dados/              # Entrada/Saída de arquivos
    ├── logs/               # Logs detalhados de execução
    ├── tests/              # Testes unitários
    ├── requirements.txt    # Dependências do projeto
    ├── .env                # Variáveis de ambiente
    ├── Dockerfile          # Configuração do container Docker
    ├── README.md           # Documentação do projeto
    ├── main.py             # Ponto de entrada do projeto
```

                    """)
                elif arquivo == "requirements.txt":
                    f.write("# Lista de dependências do projeto\n")
                elif arquivo == "main.py":
                    f.write("""# Ponto de entrada do projeto\n\nif __name__ == '__main__':\n    print('Projeto iniciado!')""")
                elif arquivo == ".env":
                    f.write("""# Variáveis de ambiente\nSECRET_KEY=your_secret_key_here\nDEBUG=True""")
                elif arquivo == "Dockerfile":
                    f.write("""# Dockerfile exemplo\nFROM python:3.12\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"python\", \"main.py\"]""")
    
    criar_logger(caminho_base)
    criar_dockerignore(caminho_base)
    inicializar_git(caminho_base, inicializar_git_flag)
        
    if criar_venv:  
        criar_ambiente_virtual(caminho_base)
    
    print(Fore.GREEN + "✅ Estrutura do projeto foi gerada com sucesso! 🎉")

def criar_dockerignore(caminho_base):
 
    dockerignore_path = os.path.join(caminho_base, ".dockerignore")
    if not os.path.exists(dockerignore_path):
        with open(dockerignore_path, "w", encoding="utf-8") as f:
            f.write("""
# Ignore o ambiente virtual
venv/
.venv/
ENV/
env/
env.bak/
venv.bak/

# Ignore arquivos Python compilados
__pycache__/
*.py[cod]
*$py.class

# Ignore arquivos de log
*.log
logs/

# Ignore arquivos e diretórios de testes
tests/
.pytest_cache/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/

                
# Ignore dependências temporárias
*.egg-info/
.eggs/
dist/
build/
*.egg
pip-log.txt
pip-delete-this-directory.txt

# Ignore cache e lixo
*.DS_Store
*.swp
*.bak
*.tmp

# Ignore documentação gerada
docs/_build/

# Ignore arquivos de IDEs
.idea/
.vscode/
*.code-workspace

# Jupyter Notebooks
.ipynb_checkpoints/

# Arquivos de controle de versionamento que não devem ir pro container
.git/
.gitignore
.dockerignore
    """)
        print(Fore.YELLOW + "🔧 Arquivo .dockerignore criado com sucesso")


def criar_logger(caminho_base):
    """Cria o arquivo logger.py dentro de core."""
    logger_code = """import logging\nimport os\nfrom datetime import datetime\n\nclass Logger:\n    def __init__(self, log_dir='logs', log_level=logging.INFO):\n        self.log_dir = log_dir\n        os.makedirs(self.log_dir, exist_ok=True)\n        \n        log_filename = datetime.now().strftime('%Y-%m-%d.log')\n        log_path = os.path.join(self.log_dir, log_filename)\n        \n        logging.basicConfig(\n            level=log_level,\n            format='%(asctime)s - %(levelname)s - %(message)s',\n            handlers=[\n                logging.FileHandler(log_path, encoding='utf-8'),\n                logging.StreamHandler()\n            ]\n        )\n        \n        self.logger = logging.getLogger(__name__)\n    \n    def get_logger(self):\n        return self.logger"""
    
    caminho_logger = os.path.join(caminho_base, "src", "core", "logger.py")
    with open(caminho_logger, "w", encoding="utf-8") as f:
        f.write(logger_code)

def inicializar_git(caminho_base, inicializar_git_flag=False):
    """Inicializa um repositório Git no diretório do projeto e cria um .gitignore padrão."""
    gitignore_path = os.path.join(caminho_base, ".gitignore")
    if not os.path.exists(gitignore_path):
        if inicializar_git_flag:
            os.system(f"cd {caminho_base} && git init")
        with open(gitignore_path, "w") as f:
            f.write("""
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
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
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

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

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

""")




def criar_ambiente_virtual(caminho_base):
    """Cria e ativa o ambiente virtual no projeto."""
    venv_path = os.path.join(caminho_base, "venv")
    if not os.path.exists(venv_path): 
        print(Fore.YELLOW + "🔧 Criando o ambiente virtual...")
        subprocess.run(["python", "-m", "venv", venv_path])
        


def main():
    parser = argparse.ArgumentParser(description="Ferramenta para criar estrutura de projetos.")
    parser.add_argument("comando", choices=["create"], help="Comando para iniciar o projeto")

    # parser.add_argument("comando", choices=["start", "create", "init"], help="Comando para iniciar ou ativar o projeto")
    parser.add_argument("nome", nargs="?", help="Nome do projeto (necessário para 'create' e 'start')")
    parser.add_argument("--name", help="Definir o nome do projeto")
    parser.add_argument("--git", action="store_true", help="Inicializar um repositório Git no projeto")
    parser.add_argument("--no-venv", action="store_true", help="Desativa a criação do ambiente virtual")
    
    args = parser.parse_args()

    
    if args.comando == "create":
        if args.name:  
            caminho_base = os.path.join(os.getcwd(), args.name)
            if not os.path.exists(caminho_base):
                criar_arquitetura(caminho_base, not args.no_venv)
            else:
                print(Fore.RED + f"Erro: O diretório '{args.name}' já existe!")
        else:
            criar_arquitetura(os.getcwd(), not args.no_venv, args.git)
    

if __name__ == "__main__":
    main()