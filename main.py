import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types # type information/hinting for api

def main():
    # Load genai with api key from environment variable
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    # Check if prompt is provided as command line argument
    if len(sys.argv) < 2:
        print("I need a prompt to generate a response.")
        sys.exit(1) # Exit with error code 1 if no prompt is provided
    
    verbose_flag = False
    # Check if --verbose flag is provided as command line argument
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True



    # sys.argv[0] = name of file
    # sys.argv[1] = prompt, first command line argument
    prompt = sys.argv[1]

    #Create a list of messages, starting with the user's prompt
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    #Creating a list of messages helps give context to Gemini about the conversation history.


    # Generate response from Gemini
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=prompt # Use the provided prompt to generate a response
    )

    # Print the generated response
    print(response.text)

    #If response is empty or malformed, print error and exit
    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return

    # If --verbose flag is provided, print usage metadata
    if verbose_flag:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()