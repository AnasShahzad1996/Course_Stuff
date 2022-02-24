from google.cloud import aiplatform

# Create a model resource from public model assets
model = aiplatform.Model.upload(
    display_name="mpg-imported",
    artifact_uri="gs://io-vertex-codelab/mpg-model/",
    serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest"
)

# Deploy the above model to an endpoint
#model = aiplatform.Model.upload_tensorflow_saved_model(saved_model_dir="gs://my-kubernetes-codelab-342121-bucket/mpg/model",display_name="my_model")


# Deploy the above model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4"
)