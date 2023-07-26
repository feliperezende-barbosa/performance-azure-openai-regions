import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

import ask_openai as ask

system_message = {"role":"system","content":"You are an AI assistant that helps people find information."}

#Textos usados como exemplos para a performance de sintetização
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

logging.basicConfig(level=logging.INFO, filename=f"./Logs/{log_file}", filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
logging.info(f";Status;Region;Sample;Response_openai_s;Request_Duration_s;Prompt Size;Completion Size")

runs = 10

for i in range(runs):
    for sample in samples:
        print(f"Processando execução #{i + 1} com sample do tipo {sample}")    
        
        #call eastus region
        start = time.time()
        response_oai_east_us = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                            os.getenv("API_BASE_EASTUS"),
                                            os.getenv("API_VERSION_EASTUS"),
                                            os.getenv("API_KEY_EASTUS"),
                                            os.getenv("DEPLOYMENT_ID_EASTUS"),
                                            os.getenv("OPENAI_MAX_TOKENS")
                                            ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_east_us != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_eastus = response_oai_east_us.response_ms / 1000

            tokens_completion = response_oai_east_us.usage.completion_tokens
            tokens_prompt = response_oai_east_us.usage.prompt_tokens

            logging.info(f";SUCCESS;East US;{sample};{response_ms_eastus};{duration};{tokens_prompt};{tokens_completion}")
        else:        
            logging.error(f";ERROR;East US;{sample};NaN;{duration};NaN;NaN")        
        #finish eastus region

        #call uksouth region
        start = time.time()
        response_oai_uk_south = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                            os.getenv("API_BASE_UKSOUTH"),
                                            os.getenv("API_VERSION_UKSOUTH"),
                                            os.getenv("API_KEY_UKSOUTH"),
                                            os.getenv("DEPLOYMENT_ID_UKSOUTH"),
                                            os.getenv("OPENAI_MAX_TOKENS")
                                            ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_uk_south != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_uksouth = response_oai_uk_south.response_ms / 1000

            tokens_completion = response_oai_uk_south.usage.completion_tokens
            tokens_prompt = response_oai_uk_south.usage.prompt_tokens

            logging.info(f";SUCCESS;UK South;{sample};{response_ms_uksouth};{duration};{tokens_prompt};{tokens_completion}")
        else:
            logging.error(f";ERROR;UK South;{sample};NaN;{duration};NaN;NaN")        
        #finish uksouth region

        #call francecentral region
        start = time.time()
        response_oai_france_central = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                                    os.getenv("API_BASE_FRANCECENTRAL"),
                                                    os.getenv("API_VERSION_FRANCECENTRAL"),
                                                    os.getenv("API_KEY_FRANCECENTRAL"),
                                                    os.getenv("DEPLOYMENT_ID_FRANCECENTRAL"),
                                                    os.getenv("OPENAI_MAX_TOKENS")
                                                    ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_france_central != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_francen = response_oai_france_central.response_ms / 1000

            tokens_completion = response_oai_france_central.usage.completion_tokens
            tokens_prompt = response_oai_france_central.usage.prompt_tokens

            logging.info(f";SUCCESS;France Central;{sample};{response_ms_francen};{duration};{tokens_prompt};{tokens_completion}")
        else:
            logging.error(f";ERROR;France Central;{sample};NaN;{duration};NaN;NaN")
        #finish francecentral region

        #call canadaeast region
        start = time.time()
        response_oai_canada_east = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                                os.getenv("API_BASE_CANADAEAST"),
                                                os.getenv("API_VERSION_CANADAEAST"),
                                                os.getenv("API_KEY_CANADAEAST"),
                                                os.getenv("DEPLOYMENT_ID_CANADAEAST"),
                                                os.getenv("OPENAI_MAX_TOKENS")
                                                ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_canada_east != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_canadaeast = response_oai_canada_east.response_ms / 1000

            tokens_completion = response_oai_canada_east.usage.completion_tokens
            tokens_prompt = response_oai_canada_east.usage.prompt_tokens

            logging.info(f";SUCCESS;Canada East;{sample};{response_ms_canadaeast};{duration};{tokens_prompt};{tokens_completion}")
        else:
            logging.error(f";ERROR;Canada East;{sample};NaN;{duration};NaN;NaN")
        #finish canadaeast region

        #call northcentralus region
        start = time.time()
        response_oai_northcentralus = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                                    os.getenv("API_BASE_NORTHCENTRALUS"),
                                                    os.getenv("API_VERSION_NORTHCENTRALUS"),
                                                    os.getenv("API_KEY_NORTHCENTRALUS"),
                                                    os.getenv("DEPLOYMENT_ID_NORTHCENTRALUS"),
                                                    os.getenv("OPENAI_MAX_TOKENS")
                                                    ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_northcentralus != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_northcentralus = response_oai_northcentralus.response_ms / 1000

            tokens_completion = response_oai_northcentralus.usage.completion_tokens
            tokens_prompt = response_oai_northcentralus.usage.prompt_tokens

            logging.info(f";SUCCESS;North Central US;{sample};{response_ms_northcentralus};{duration};{tokens_prompt};{tokens_completion}")
        else:
            logging.error(f";ERROR;North Central US;{sample};NaN;{duration};NaN;NaN")
        #finish northcentralus region
        
        #call westeurope region
        start = time.time()
        response_oai_westeurope = ask.AskOpenAi(os.getenv("OPENAI_API_TYPE"),
                                                os.getenv("API_BASE_WESTEUROPE"),
                                                os.getenv("API_VERSION_WESTEUROPE"),
                                                os.getenv("API_KEY_WESTEUROPE"),
                                                os.getenv("DEPLOYMENT_ID_WESTEUROPE"),
                                                os.getenv("OPENAI_MAX_TOKENS")
                                                ).ask(system_message, sample)
        end = time.time()

        duration = end - start

        if response_oai_westeurope != None:
            #variable to get the value of converted milliseconds to seconds
            response_ms_westeurope = response_oai_westeurope.response_ms / 1000

            tokens_completion = response_oai_westeurope.usage.completion_tokens
            tokens_prompt = response_oai_westeurope.usage.prompt_tokens

            logging.info(f";SUCCESS;West Europe;{sample};{response_ms_westeurope};{duration};{tokens_prompt};{tokens_completion}")
        else:
            logging.error(f";ERROR;West Europe;{sample};NaN;{duration};NaN;NaN")
        #finish westeurope region
        
        time.sleep(1)

print("Processo finalizado.")