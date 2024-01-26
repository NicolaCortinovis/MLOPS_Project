import setuptools

with open("README.md","r", encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "https://github.com/NicolaCortinovis/MLOPS_Project"
SRC_REPO = "mlopsProject"
AUTHOR_USER_NAME = "NicolaCortinovis"
AUTHOR = "Cortinovis Nicola, Islamay Erion, Paladino Annalisa, Pernice Luca"
AUTHOR_EMAIL = "nicolacortinovis98@gmail.com" # add your emails here


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = "to be filled",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src"),
)