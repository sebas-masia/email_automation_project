# Email Automation Project

## Overview
This project automates the organization of emails in Microsoft Outlook based on shipment IDs retrieved from the Turvo API. It periodically checks for new emails, parses their subjects for shipment IDs, and sorts them into corresponding folders.

## Features
- Retrieves shipment IDs from Turvo API.
- Creates folders in Outlook for each shipment ID.
- Monitors incoming emails and sorts them based on IDs.

## Prerequisites
- Python 3.x
- Access to Turvo API and Microsoft Graph API.
- Azure Active Directory credentials for Outlook API.

## Setup and Installation
1. Clone the repository:
   `git clone [repository_url]`
2. Navigate to the project directory:
   `cd email_automation_project`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Set up your credentials for Turvo and Outlook APIs in respective scripts.

## Configuration
Update the turvo_api.py and outlook_api.py with the necessary credentials and API keys.

## Running the Application
Execute the main script to start the email automation process:
   `python src/email_organizer.py`

## Testing
Run the test suite using:
   `python -m unittest`

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
- Sebastian Masia

## License
This project is licensed under the LICENSE - see the LICENSE.md file for details.

## Acknowledgments
- Team members or contributors
- External libraries or APIs used
