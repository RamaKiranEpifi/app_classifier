# Use the ListFoundationModels API to show the models that are available in &BR; in a given region.
import boto3
from botocore.exceptions import ClientError
# bedrock.list_foundation_models() #to list all the models available in &BR; in a given region
# Create an Amazon Bedrock Runtime client in the AWS Region you want to use.
brt = boto3.client("bedrock-runtime", region_name="ap-south-1")

# Set the model ID, e.g., Amazon Titan Text G1 - Express.
#  model_id = "amazon.titan-text-express-v1"
def bdr_connection(model_id):
   
    # Start a conversation with the user message.
    user_message = "Describe the purpose of a 'hello world' program in one line."
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = brt.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        print(response_text)

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)