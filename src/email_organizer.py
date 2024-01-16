from turvo_api import get_turvo_access_token, get_shipment_ids
from outlook_api import get_access_token, create_folder, move_email
import time


def main():
    # Turvo API credentials
    turvo_client_id = 'your_turvo_client_id'
    turvo_client_secret = 'your_turvo_client_secret'
    turvo_api_key = 'your_turvo_api_key'

    # Outlook API credentials
    outlook_client_id = 'your_outlook_client_id'
    outlook_client_secret = 'your_outlook_client_secret'
    outlook_tenant_id = 'your_outlook_tenant_id'

    # Authenticate with Turvo API
    turvo_token = get_turvo_access_token(
        turvo_client_id, turvo_client_secret, turvo_api_key)

    # Authenticate with Outlook API
    outlook_token = get_access_token(
        outlook_client_id, outlook_client_secret, outlook_tenant_id)

    # Retrieve shipment IDs from Turvo
    shipment_ids = get_shipment_ids(turvo_token)

    # Create a folder in Outlook for each shipment ID
    for shipment_id in shipment_ids:
        folder_name = f'Shipment-{shipment_id}'
        create_folder(outlook_token, folder_name)

    # Implement logic to monitor incoming emails and sort them
    # Note: This part of the code depends on how you access and manage emails in Outlook
    # It might involve continuously checking for new emails and parsing their subjects
    # to match them with shipment IDs, then moving them to the corresponding folders.

    while True:
        try:
            # Function to fetch new emails
            new_emails = fetch_new_emails(outlook_token)
            for email in new_emails:
                email_subject = email['subject']
                for shipment_id in shipment_ids:
                    if shipment_id in email_subject:
                        move_email_to_folder(
                            outlook_token, email['id'], f'Shipment-{shipment_id}')
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(300)  # Wait for 5 minutes before checking again


if __name__ == "__main__":
    main()
