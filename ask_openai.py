import openai
import logging

class AskOpenAi():

    def __init__(self, api_type, api_base, api_version, api_key, deployment_id, MAX_TOKENS):
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_version = api_version
        openai.api_key = api_key
        self.deployment_id = deployment_id
        self.MAX_TOKENS = MAX_TOKENS

    def ask(self, system_message, sample):
        try:
            response = openai.ChatCompletion.create(
                engine = self.deployment_id,
                messages = [system_message, sample],
                request_timeout = 180,
                temperature = 0.7,
                max_tokens = int(self.MAX_TOKENS),
                top_p = 0.95,
                frequency_penalty = 0,
                presence_penalty = 0,
                stop = None
            )
            return response
        except Exception as e:
            #self.error_openai_api(e)
            return None
        
    def error_openai_api(self, e):
        logging.warning(f"APIError: {e}")       