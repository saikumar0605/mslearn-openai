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
        
        40802968
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
    prompt = "You are a helpfull ai bot who answers the user questions in both English and Spanish. Each response must be in a casual tone and ends with 'Hope that helps! Thanks for using Contoso, Ltd.' "
    messages=[
            {"role": "system", "content": prompt},
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
    
    # Build messages to send to Azure OpenAI model. (Add code here)
    messages=[
            {"role": "", "": inputText}
        ]
    

    # Define argument list (Add code here)
    apiParams = {
        "messages": messages,
    }
    
    utils.writeLog("API Parameters:\n", apiParams)

    # Call chat completion connection. (Add code here)
    # Use the call name and **apiParams to reference our argument list
    response = ""

    
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
