import openai
import logging

class AskOpenAi():
    """
    A class to interact with OpenAI's chat API.

    Attributes:
    -----------
    api_base : str
        The base URL for the API.
    api_version : str
        The version of the API to use.
    api_key : str
        The API key to authenticate with.
    deployment_id : str
        The ID of the deployment to use.
    api_type : str, optional
        The type of API to use (default is "azure").
    max_tokens : int, optional
        The maximum number of tokens to generate in the response (default is 250).
    temperature : float, optional
        The sampling temperature to use (default is 0.7).
    timeout : int, optional
        The maximum time to wait for a response from the API, in seconds (default is 180).
    """

    def __init__(self, api_base, api_version, api_key, deployment_id, api_type="azure", max_tokens=250, temperature=0.7, timeout=180):
        """
        Initializes a new instance of the AskOpenAi class.

        Parameters:
        -----------
        api_base : str
            The base URL for the API.
        api_version : str
            The version of the API to use.
        api_key : str
            The API key to authenticate with.
        deployment_id : str
            The ID of the deployment to use.
        api_type : str, optional
            The type of API to use (default is "azure").
        max_tokens : int, optional
            The maximum number of tokens to generate in the response (default is 250).
        temperature : float, optional
            The sampling temperature to use (default is 0.7).
        timeout : int, optional
            The maximum time to wait for a response from the API, in seconds (default is 180).
        """
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_version = api_version
        openai.api_key = api_key
        self.deployment_id = deployment_id
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.temperature = temperature

    def ask(self, system_message, sample):
        """
        Sends a message to the OpenAI chat API and returns the response.

        Parameters:
        -----------
        system_message : str
            The message to send to the API as the system message.
        sample : str
            The message to send to the API as the user message.

        Returns:
        --------
        response : dict
            The response from the API, as a dictionary.
        """
        try:
            response = openai.ChatCompletion.create(
                engine=self.deployment_id,
                messages=[system_message, sample],
                request_timeout=self.timeout,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            return response
        except Exception as e:
            #self.error_openai_api(e)
            return None
        
    def error_openai_api(self, e):        
        """
        Logs an error message when an exception is raised by the OpenAI API.

        Parameters:
        -----------
        e : Exception
            The exception that was raised.
        """
        logging.warning(f"APIError: {e}")

