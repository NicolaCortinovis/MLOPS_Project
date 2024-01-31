# MLOPS_Project

## ConversationSummarizer

### Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entities.yaml
4. Update configuration manager `in src/mlopsProject/config/configuration.py`
5. Update components
6. Update pipeline
7. Update `main.py`
8. Update `app.py`

## How to run

### STEP 0: Clone the repository

```
git clone https://github.com/NicolaCortinovis/MLOPS_Project.git
```

### STEP 1: Create and activate a new conda environment

```
conda create -n YourEnvName python=3.8 -y
conda activate YourEnvName
```

### STEP 2: Install the requirements

```
# You must be in the project folder

pip install -r requirements.txt
```

### STEP 3: Run the main file

```
python main.py
```