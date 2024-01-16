import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.exceptions import RequestException

# Function to get access token
def get_access_token(client_id, client_secret, tenant_id):
    try:
        token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        token_r = requests.post(token_url, data=token_data)
        token_r.raise_for_status()
        return token_r.json().get('access_token')
    except RequestException as e:
        print(f"Error obtaining token: {e}")
        return None

# Function to create a folder in Outlook
def create_folder(access_token, folder_name, parent_folder_id=None):
    try:
        url = 'https://graph.microsoft.com/v1.0/me/mailFolders'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        payload = {'displayName': folder_name}
        if parent_folder_id:
            payload['parentFolderId'] = parent_folder_id
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Error creating folder: {e}")
        return None

# Function to move an email to a specific folder
def move_email(access_token, message_id, destination_folder_id):
    try:
        url = f'https://graph.microsoft.com/v1.0/me/messages/{message_id}/move'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        payload = {'destinationId': destination_folder_id}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Error moving email: {e}")
        return None
