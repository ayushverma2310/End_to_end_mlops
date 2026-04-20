# END TO END MACHINE_LEARNING_PROJECT_WITH_MLFLOW

## WORKFLOWS

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml





# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ayushverma2310/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ayushverma2310/End_to_end_mlops.mlflow
MLFLOW_TRACKING_USERNAME=ayushverma2310 \
MLFLOW_TRACKING_PASSWORD=ea792992d577aeb36f7d77403ca1009aea46df17\
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ayushverma2310/End_to_end_mlops.mlflow
export MLFLOW_TRACKING_USERNAME=ayushverma2310 
export MLFLOW_TRACKING_PASSWORD=ea792992d577aeb36f7d77403ca1009aea46df17


```
# Create ECR repo to store/ save docker image
 URI:  455919270070.dkr.ecr.eu-north-1.amazonaws.com/mlproj