import os
from dotenv import load_dotenv
import utils

# Add OpenAI import. (Add code here)
from openai import AzureOpenAI


def main(): 
        
    try:     
        load_dotenv()
        utils.initLogFile()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Define Azure OpenAI client (Add code here)
        client = AzureOpenAI(
            azure_endpoint = azure_oai_endpoint, 
            api_key=azure_oai_key,  
            api_version="2023-12-01-preview"
            )       
        

        function_map = {
            "1": function1,
            "2": function2,
            "3": function3,
            "4": function4
        }

        while True:
            print('1: Validate PoC\n' +
                  '2: Company chatbot\n' +
                  '3: Developer tasks\n' +
                  '4: Use company data\n' +
                  '\'quit\' to exit the program\n')
            command = input('Enter a number:')
            if command.strip() in function_map:
                function_map[command](client, azure_oai_model)
            elif command.strip().lower() == 'quit':
                print('Exiting program...')
                break
            else :
                print("Invalid input. Please enter number 1, 2, 3, 4, or 5.")

    except Exception as ex:
        print(ex)

# Task 1: Validate PoC
def function1(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 1: Validate PoC", "sample-text.txt")
    
    # Build messages to send to Azure OpenAI model. (Add code here)
    messages=[
             {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": inputText}
        ]
    

    # Define argument list (Add code here)
    apiParams = {
        "messages": messages,
    }
    

    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection. (Add code here)
    # Use the call name and **apiParams to reference our argument list
    response = aiClient.chat.completions.create(
        model= aiModel,
        max_tokens=5000,
        messages=messages
    )
    

    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response

# Task 2: Company chatbot
def function2(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 2: Company chatbot", "sample-text.txt")
    
    # Build messages to send to Azure OpenAI model. (Add code here)
    messages=[
            {"role": "system", "content": "You are a helpful AI bot who answers user questions in both English and Spanish. and make sure 'Each response must be in a casual tone and end with 'Hope that helps! Thanks for using Contoso, Ltd.'"},
            {"role": "user", "content": inputText}
        ]
    

    # Define argument list (Add code here)
    apiParams = {
        "messages": messages,
    }
    

    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection. (Add code here)
    # Use the call name and **apiParams to reference our argument list
    response = aiClient.chat.completions.create(
            model= aiModel,
            max_tokens=1000,
            temperature = 0.5,
            messages=messages
    )
    

    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response

# Task 3: Developer tasks
def function3(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 3: Developer tasks", "sample-text.txt")

    # Define file paths
    legacy_code_path = "C:\\files\\legacyCode.py"
    fibonacci_path = "C:\\files\\fibonacci.py"
    prompt_path = "C:\\files\\AzureOpenAIPoc\\Python\\sample-text.txt"

    # Prepare tasks
    tasks = {
        '1': {
            'file_path': legacy_code_path,
            'task_instructions': "Add comments to the following legacy code and generate documentation.\n---\n"
        },
        '2': {
            'file_path': fibonacci_path,
            'task_instructions': "Generate five unit tests for the function in the following code.\n---\n"
        }
    }

    # Read the base prompt from the sample-text.txt file
    with open(prompt_path, 'r', encoding='utf8') as prompt_file:
        base_prompt = prompt_file.read().strip()

    for key, task in tasks.items():
        with open(task['file_path'], 'r', encoding='utf8') as file:
            file_content = file.read()
        
        # Combine the base prompt with task instructions and file content
        prompt = (base_prompt + "\n" + task['task_instructions'] + file_content).strip()

        messages = [
            {"role": "user", "content": prompt}
        ]

    # Build messages to send to Azure OpenAI model. (Add code here)

    

    # Define argument list (Add code here)
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection. (Add code here)
    # Use the call name and **apiParams to reference our argument list
        # Submit request to Azure OpenAI
    response = aiClient.chat.completions.create(
            model=aiModel,
            max_tokens=1000,
            temperature=0.7,
            **apiParams
        )

    
    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return response 

# Task 4: Use company data
def function4(aiClient, aiModel):
    inputText = utils.getPromptInput("Task 4: Use company data", "sample-text.txt")
    
    # Build messages to send to Azure OpenAI model. (Add code here)
    messages=[
            {"role": "system", "content": "You are a helpful travel agent."},
            {"role": "user", "content": inputText}
        ]
    

    # Define connection and argument list (Add code here)
    apiParams = {
        "messages": messages,
    }
    

    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection. Will be the same as function1 (Add code here)
    # Use the call name and **apiParams to reference our argument list
    response = aiClient.chat.completions.create(
            model= aiModel,
            max_tokens=1000,
            temperature = 0.5,
            messages=messages
    )
    

    utils.writeLog("Response:\n", str(response))
    print("Response: " + response.choices[0].message.content + "\n")
    return

# Call main function. Do not modify.
if __name__ == '__main__': 
    main()



#sampletext file prompt for task - 3
"""
You are an AI assistant helping with code documentation and testing. Please complete the following tasks:

1. For legacy code, add comments and generate documentation.
2. For the Fibonacci function, generate five unit tests."""
