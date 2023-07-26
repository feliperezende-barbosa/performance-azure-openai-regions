class Instance():

    def __init__(self, api_type = "", api_base = "", api_version = "", api_key = "", deployment_id = "", max_tokens = 0, region = ""):
        self._api_type = api_type
        self._api_base = api_base
        self._api_version = api_version
        self._api_key = api_key
        self._deployment_id = deployment_id
        self._max_tokens = max_tokens
        self._region = region

    def __get_api_type__(self):
        return self._api_type
    
    def __get_api_base__(self):
        return self._api_base
    
    def __get_api_version__(self):
        return self._api_version
    
    def __get_api_key__(self):
        return self._api_key
    
    def __get_deployment_id__(self):
        return self._deployment_id
    
    def __get_max_tokens__(self):
        return self._max_tokens
    
    def __get_region__(self):
        return self._region
    
    def __set_api__(self, api_type):
        self._api_type = api_type

    def __set_api_base__(self, api_base):
        self._api_base = api_base

    def __set_api_version__(self, api_version):
        self._api_version = api_version

    def __set_api_key__(self, api_key):
        self._api_key = api_key

    def __set_deployment_id__(self, deployment_id):
        self._deployment_id = deployment_id

    def __set_max_tokens__(self, max_tokens):
        self._max_tokens = max_tokens

    def __set_region__(self, region):
        self._region = region



