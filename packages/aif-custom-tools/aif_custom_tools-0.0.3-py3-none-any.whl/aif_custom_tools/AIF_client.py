import requests
import json

class AIFLLMClient:
    def __init__(self, auth_url, client_id, client_secret, scope, subscription_key):
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.subscription_key = subscription_key
        self.token = self.get_access_token()

    def get_access_token(self):
        response = requests.post(
            self.auth_url,
            data={"grant_type": "client_credentials", "scope": self.scope},
            auth=(self.client_id, self.client_secret),
        )
        response.raise_for_status()
        return response.json()['access_token']

    def call_custom_model_api(self, apiURL,model_name, input_prompt, temperature, top_p, max_tokens, response_format, presence_penalty, frequency_penalty):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.token}",
            "Ocp-Apim-Subscription-Key": self.subscription_key
        }

        input_body = {
            "messages": [
                {
                    "role": "user",
                    "content": input_prompt
                }
            ],
            "model_name": model_name,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "response_format": response_format
        }

        payload = json.dumps(input_body)
        response = requests.post(apiURL, data=payload, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()

    def run_embedding_model(self, url, input_text):
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = json.dumps({"input": input_text})
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        return response.json()