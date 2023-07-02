import streamlit as st
from cnnCDClassifier.pipeline.predict import PredictionPipeline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import json
import tensorflow as tf
import yaml
from streamlit_tensorboard import st_tensorboard
st.set_page_config
def load_params():
    # Load the training parameters from the param.yaml file
    with open('params.yaml') as f:
        params = yaml.safe_load(f)
    return params



# def save_params(params):
#     # Save the updated training parameters to the param.yaml file
#     with open('params.yaml', 'w') as f:
#         yaml.safe_dump(params, f, default_style='', default_flow_style=False)

def execute_dvc_stage(stage_name):
    # Execute the DVC stage
    cmd = f"dvc repro -s {stage_name}"
    subprocess.run(cmd.split(), check=True)

def load_training_metrics():
    # Load the training metrics from the scores.json file
    with open('scores.json') as f:
        metrics = json.load(f)

    if isinstance(metrics, dict):
        # If the metrics are in dictionary format
        df = pd.DataFrame([metrics])
    elif isinstance(metrics, list):
        # If the metrics are in list format
        df = pd.DataFrame(metrics)
    else:
        # Invalid metrics format
        raise ValueError("Invalid metrics format in scores.json")

    return df



def main():

    # >>>>>>>>>>>>

    st.title("Chicken-Disease-Classifier Using VGG16")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg","png"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        pipeline = PredictionPipeline("temp.jpg")
        prediction = pipeline.predict()
        prediction_value = prediction[0]['image']
        
        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown("### Image")
            col1.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        with col2:
            st.markdown("### Model Prediction")
            col2.write(prediction_value)

    # >>>>>>>>>>>>
    
    show_params = st.sidebar.checkbox('Show Parameters Configurations') 

    if show_params:
        # Load the training parameters
        params = load_params()

        # Display the current parameter values
        st.sidebar.subheader("Current Parameters")
        # Display the params.yaml file in a decorative format
        for key, value in params.items():
            st.sidebar.write(f"**{key}:** {value}")
    #>>>>>>>>>>>>>>>>>>>>>

    logs_directory = 'artifacts/prepare_callbacks/tensorboard_log_dir'
    show_tensorboard = st.sidebar.checkbox('Show Tensorboard Log Directory') 

    if show_tensorboard:
        # Define the CSS styling for the container element
        container_style = '''
            <style>
            .tensorboard-container {
                width: 100%;  /* Adjust the width as needed */
            }
            </style>
        '''

        # Display the TensorBoard logs if the checkbox is checked
        if show_tensorboard:
            # Apply the CSS styling to the container element
            st.markdown(container_style, unsafe_allow_html=True)
            # Display the TensorBoard logs
            st_tensorboard(logdir=logs_directory)


    # >>>>>>>>>>>>>>>>>>>

    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # st.title("Model Training Visualization")


    # # Execute the 'training' stage if requested
    # run_training = st.button("Run Training")
    # if run_training:
    #     execute_dvc_stage("training")


    # Check if the training artifacts exist
    training_artifacts_exist = st.sidebar.checkbox("Check Training Artifacts Existence")

    if training_artifacts_exist:
        # Load training metrics data
        df = load_training_metrics()
        st.header('Training Metrics')
        st.write(df)


if __name__ == '__main__':
    main()
