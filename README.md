[Application Link](https://chicken-diseaseclassification-project.streamlit.app)
# Chicken-Disease_Classification-Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## To Run:
# Chicken-Disease-Classification--Project


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEP 1: Clone the repository
```bash
https://github.com/Deepshikhar/Chicken-Disease_Classification-Project
```
### STEP 02- Create a virtual environment after opening the repository
```bash
conda create -n cnncd python=3.8 -y
```

```bash
conda activate cnncd
```

### STEP 03- run requirements.txt to install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- run app.py
```bash
python app.py
```

### STEP 05- open your browser
```bash
open up you local host and port
```

## To Run using dvc file
### DVC cmd

1. dvc init # To initialize
2. dvc repro # To run 
3. dvc dag  # To show the workflow

Save pass:
s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6

Run from terminal:
docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest

