import json, os, time, logging
import ask_openai as ask
from dotenv import load_dotenv

#Loading environment variables
load_dotenv()

#Initialize Azure OpenAI parameters. Most of these parameters are defined in the .env file
api_type='azure'  
api_version = os.environ.get("API_VERSION")
max_tokens = int(os.environ.get("AZURE_OPENAI_MAXTOKENS"))
temperature = float(os.environ.get("AZURE_OPENAI_TEMPERATURE"))
timeout = int(os.environ.get("AZURE_OPENAI_TIMEOUT"))
az_openai_regions = os.environ.get("AZURE_OPENAI_REGIONS")
regions = json.loads(az_openai_regions) 


#Number of runs to be executed. Adjust according to your needs
RUNS = 5

#Define a default system message. You can adjust this message to your needs depending on the test type
system_message = {"role":"system","content":"You are an AI assistant that helps people find information."}

#Sample messages that will be used as prompts to measure the model's response time
samples = [  
    {"role": "user", "content": "Qual é a capital do Brasil?"},  
    {"role": "user", "content": "Como funciona a fotossíntese?"},  
    {"role": "user", "content": "Quem escreveu o livro 'Dom Quixote'?"},  
    {"role": "user", "content": "Quais são os três estados físicos da água?"},  
    {"role": "user", "content": "Qual é a fórmula química da água?"},  
    {"role": "user", "content": "Qual é a distância média entre a Terra e a Lua?"},  
    {"role": "user", "content": "Quem é conhecido como o pai da computação?"},  
    {"role": "user", "content": "Quais são os cinco reinos biológicos?"},  
    {"role": "user", "content": "Quais são as sete maravilhas do mundo antigo?"},  
    {"role": "user", "content": "Quem pintou a Mona Lisa?"},
    {"role": "user", "content": "Gerar um código em C# para consumir a api do openai: https://beta.openai.com/docs/api-reference/completions/create"}    
]  

#variable to get the value of the data and time of the execution
now = time.strftime("%d-%m-%Y %H-%M-%S")
log_file = now + ".log"

#Init the parameters of the log file to generate a csv file (; separator)
logging.basicConfig(level=logging.INFO, filename=f"./Logs/{log_file}", filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
logging.info(f";Status;Region;Sample;Response_openai_s;Request_Duration_s;Prompt Size;Completion Size")

#Loop to execute the number of runs desired
for i in range(RUNS):
    
    #Loop to iterate over the regions
    for region, data in regions.items():  
        print(f"Processing {region} region")

        #Initiate the Azure OpenAI API for the region
        az_openai = ask.AskOpenAi(deployment_id=data["DEPLOYMENT_NAME"],  
                                         api_base=data["ENDPOINT"],  
                                         api_version=api_version,  
                                         api_key=data["API_KEY"],
                                         api_type=api_type,
                                         max_tokens=max_tokens,
                                         temperature=temperature,
                                         timeout=timeout)

        #Iterate over the samples
        for sample in samples:
            print(f"Processing execution #{i + 1} with sample of type {sample}")

            # Call the completion API for the sample and region and register the duration of the request
            start = time.time()
            
            response = az_openai.ask(system_message, sample)  
            
            end = time.time()  
      
            duration = end - start  

            #Check if the response succeed to log the details
            if response != None:
                #Log success with additional performance details 
                logging.info(f";SUCCESS;{region};{sample};{response.response_ms/1000};{duration};{response.usage.prompt_tokens};{response.usage.completion_tokens}")  
            else:  
                logging.error(f";ERROR;{region};{sample};NaN;{duration};NaN;NaN")  
  
            time.sleep(0.5)  

print("Process completed.")