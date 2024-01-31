## Baseline task definition

Develop an application where you can input a conversation to generate a summary. Immediately below we give an example of its functionality:

### Chat:

"____Martin____: I won two cinema tickets!

__Aggie__: oh cool, how come?

__Martin__: online. on fb, the movie mag organized it

__Aggie__: so what did you do

__Martin__: just write a short review and that's it

__Aggie__: well done :) so what and when. and where?

__Martin__: the new film with Redford

__Aggie__: i guess i heard sth

__Martin__: it's pretty cool i heard. till the end of the week

__Aggie__: sounds good. we'll find time XD"

### Summary:

Martin wrote a short review and won 2 cinema tickets on FB. Martin wants Aggie to go with him this week for the new film with Redford.


## Possible additional tasks
 - Introduce the capability to handle other formats (e.g. `.pdf` `.txt`)

## Notes for development

Not all tasks need to follow a sequential approach, we can tackle them however we see fit. In fact both `.ipynb` and `streamlit` demo interface can be implemented independently. Comment thoroughly to help everyone understand what you're doing.

### Create github repo ✓

https://github.com/NicolaCortinovis/MLOPS_Project

### Write the structure logic ✓

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
│   └── ConversationSummarizer.ipynb
├── setup.py
├── src
│   └── ConversationSummarizer
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
```

### Write the requirements ⏳

For now we can stick with the requirements used in video `lmqg` and `streamlit`. Eventually it must contain only the required packages.
This will be used to create a `conda` environment from which we'll install a custom package containing everything we need to run the app.

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
    ### updated
    `model_trainer.ipynb`  uses `Trainer` class from Hugging Face to train the flan-T5-small model 

### Implementate demo in components ⏳

Can be done in parallel with the previous tep

### Develop user app ⏳

Link everything with `streamlit`

### Project CI/CD deployement on AWS ⏳
