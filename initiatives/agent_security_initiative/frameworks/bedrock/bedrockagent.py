import json
import boto3

# Initialize Bedrock client
bedrock_client = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    # Extract user input from the request
    user_input = event['body']['userInput']

    # **Vulnerability 1: No input sanitization**
    # The user input is directly passed to the Bedrock agent without any sanitization.
    # This could allow an attacker to inject malicious code or manipulate the agent's behavior.

    # Create Bedrock agent prompt
    prompt = f"""
    Human: {user_input}
    Assistant:
    """

    # Call Bedrock agent
    response = bedrock_client.invoke_model(
        body=json.dumps({"prompt": prompt}),
        modelId="amazon.bedrock.agent.default"  # Replace with your agent ID
    )

    # **Vulnerability 2: No output validation**
    # The output from the Bedrock agent is directly returned to the user without any validation.
    # This could allow the agent to return sensitive information or execute malicious code.

    # Return agent response
    return {
        'statusCode': 200,
        'body': json.loads(response['body'].read().decode())['completion']
    }