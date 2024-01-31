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

For this file:

 - ⏳ means work in progress
 - ✅ means done
 - 🔍 means there is a note present

### Create github repo ✅

https://github.com/NicolaCortinovis/MLOPS_Project

### Write the structure logic ✅

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

### Write the requirements 🔍

Contains a first batch of packages that could be useful (according to our tests) for running our app. This will be used to create a `conda` environment from which we'll install a custom package containing everything we need to run the app.

#### Note

Still lacking the packages needed for the app

### Project setup ✅

Write the `setup.py` file that is required to install the package as a custom local package in order to facilitate the execution of the app

### Logging ✅

Write a logging system for the project

### Exceptions ✅

Write an exception handler for the project. Actually we can use `box.exceptions` to handle them in a easier way

### Utils models ✅

Write a file containing common functions used in different parts of the app

###  Demo notebooks ✅

We should create a bunch of demo notebooks that will simulate what happens inside each file in `src/ConversationSummarizer/components`.

We can follow a structure based on the following steps:

    - data ingestion (get the data) ⏳
    - data validation (check that the data is the correct one)  ⏳
    - data transformation (manipulate the data so that it can be handled for the next step) ⏳
    - model trainer (train the model on the transformed data) ⏳
    - model evaluation (evaluate the model on some metrics) ⏳


### Implement demo in components ⏳

Can and should be done in parallel with the previous step since each passage is needed for the next one

### Develop user app ⏳

Link everything

### Project CI/CD deployement on AWS ⏳

To be discussed
