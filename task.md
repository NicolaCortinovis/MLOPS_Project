## Baseline task definition

Develop an application where you can input a text (either direclty or by uploading a .txt) to generate a series of couples question-answer in a flash card manner

## Possible additional tasks
 - Introduce the possibility to also summarize the text (evolve into a "study-buddy" app so to speak)
 - Introduce the possibility to handle other formats (e.g. `.pdf` )

## Notes

Not all tasks need to follow a sequential approach, we can takcle them however we see fit. In fact both `.ipynb` and `streamlit` demo interface can be implemented independently

## Workflow for the project
<center>


|   WRITE WHAT YOU DO AND NEEDS TO BE DONE ON [TRELLO](https://trello.com/b/pcxrCOyu/scrum)  |
|--------------------------------|
</center>

### Create github repo ✓

https://github.com/NicolaCortinovis/MLOPS_Project

### Write the logic of the structure ✓

It follows the same logic stated in the [video](https://www.youtube.com/watch?v=p7V4Aa7qEpw).

```
# Directory structure
.
├── Dockerfile 
├── LICENSE
├── README.md
├── app.py
├── config
│   └── config.yaml
├── main.py
├── params.yaml
├── requirements.txt
├── research
│   ├── demo.ipynb
│   └── trials.ipynb
├── setup.py
├── src
│   └── mlopsProject
│       ├── __init__.py
│       ├── components
│       │   └── __init__.py
│       ├── config
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── constants
│       │   └── __init__.py
│       ├── entity
│       │   └── __init__.py
│       ├── logging
│       │   └── __init__.py
│       ├── pipeline
│       │   └── __init__.py
│       └── utils
│           ├── __init__.py
│           └── common.py
└── template.py

11 directories, 22 files
```

Brief explaination for every file:
- `Dockerfile` contains instructions for building a _Docker_ container
- `LICENSE` standard __MIT__ license
- `README.md` provide information and guidance to users, developers, and contributors about the project.
- `app.py` contains code for web interface (streamlit)
- `config`
    - `config.yaml` config for the components (?)
- `main.py` main body of the project
- `params.yaml` contains the parameters for the training of the model
- `requirements.txt` contains the required packages 
- `research` contains notebook used for experemintation and training of the model
    - `demo.ipynb` experemintation
    - `training.ipynb` official training
- `setup.py` used for local package installation (?)
- `src/mlopsProject` folder containin the core of the project
    - `__init__.py` necessary to install as a local package
    - `components` contains `.py` files with the functions needed for each step of the app and constructor file
        - `__init__.py` constructor file
    - `config`
        - `__init__.py` constructor file
        - `configuration.py` contains the the functions needed to return other configurations for the functions in `src/mlopsProject/components` (to be populated)
    - `constants` contains constants and constructor file
        - `/__init__.py` constructor file
    - `entity` 
        - `/__init__.py` constructor file
    - `logging`
        - `__init__.py` constructor file
    - `pipeline` contains the creating and prediction pipeline and a constructor file (to be populated)
        - `/__init__.py` constructor file
    - `utils`
        - `__init__.py` constructor file
        - `common.py` contains general utility functions
 - `template.py` is responsible for building the project structure logic, as well as the type of `logging`

### Write the requirements ⏳

For now we can stick with the requirements used in video `lmqg` and `streamlit`. Eventually it must contain only the required packages. We should use a `conda` environment to all be on the same page and avoid conflitcs.

### Project setup ⏳

### Logging ⏳

### Exceptions ⏳

### Utils models ⏳

###  Demo notebooks ⏳

We should create a bunch of demo notebooks that will simulate what happens inside each file in `src/mlopsProject/components`. Refer to [video](https://www.youtube.com/watch?v=p7V4Aa7qEpw) for the blueprint (given below)

 - `data_ingestion.ipynb` data from [dataset](https://huggingface.co/datasets/lmqg/qag_squad])
 - `data_validation.ipynb` needed?
 - `data_transformation.ipynb` needed?
 - `model_trainer.ipynb`  uses `GridSearch` from `lmqg` library (maybe think how to connect it to Neptune). Explore what params exist for our model and what to add to GridSearch, also check if there exist a way to print results at the end of each epoch.
 - `model_evaluation.ipynb` refer to https://github.com/asahi417/lm-question-generation

### Implementate demo in components ⏳

Can be done in parallel with the previous tep

### Develop user app ⏳

Link everything with `streamlit`

### Project CI/CD deployement on AWS ⏳
