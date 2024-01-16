import requests

# Function to get access token from Turvo API


def get_turvo_access_token(client_id, client_secret, api_key):
    auth_url = 'https://publicapi.turvo.com/v1/oauth/token'
    headers = {'x-api-key': api_key}
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        # Include other necessary parameters as required by Turvo's API
    }
    response = requests.post(auth_url, headers=headers, data=data)
    return response.json().get('access_token')

# Function to get shipment IDs from Turvo


def get_shipment_ids(access_token):
    shipments_url = 'https://publicapi.turvo.com/v1/shipments'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(shipments_url, headers=headers)
    shipments = response.json()

    # Extract and return shipment IDs from the response
    return [shipment['id'] for shipment in shipments]


# Replace with your actual credentials and API key
client_id = 'your_client_id'
client_secret = 'your_client_secret'
api_key = 'your_api_key'

# Example usage
token = get_turvo_access_token(client_id, client_secret, api_key)
shipment_ids = get_shipment_ids(token)
print(shipment_ids)
