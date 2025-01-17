import os
from mistralai import Mistral

# Set your Mistral API key (replace with your API key if not using environment variables)
os.environ["MISTRAL_API_KEY"] = "kLdfhPekcU0ROO57K0B62U4yxQHL5jN6"  # Replace with your actual API key

# Get the API key from the environment variables
api_key = os.environ.get("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the MISTRAL_API_KEY environment variable.")

# Create a Mistral client instance
with Mistral(api_key=api_key) as mistral:
    # Make a chat completion request using the mistral-large-2411 model
    response = mistral.chat.complete(
        model="mistral-large-latest",  # Specify the correct model
        messages=[
            {"role": "user", "content": "How can I improve my financial health?"}
        ]
    )

    # Debug: Print the entire response object
    print("Response Object:", response)

    # Extract the generated response content
    generated_text = response.choices[0].message.content
    print("Generated Response:", generated_text)
