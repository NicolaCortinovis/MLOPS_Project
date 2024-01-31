import setuptools


# Save the long description from the README.md file

with open("README.md","r", encoding= "utf-8") as f:
    long_description = f.read()
    
# First version of the package

__version__ = "0.0.0"

REPO_NAME = "https://github.com/NicolaCortinovis/MLOPS_Project"
SRC_REPO = "mlopsProject"
AUTHOR_USER_NAME = "NicolaCortinovis, Erionis, annalisapaladino, lucapernice"
AUTHOR = "Cortinovis Nicola, Islamay Erion, Paladino Annalisa, Pernice Luca"
AUTHOR_EMAIL = "nicolacortinovis98@gmail.com" # to be filled

# Setting up the package

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = "Package for the the conversation summarizer app",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src"),
)