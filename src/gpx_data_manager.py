import os
import requests
import logging
from typing import Optional
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Strava API credentials
CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
REDIRECT_URI = os.getenv('STRAVA_REDIRECT_URI')

# Strava API endpoints
AUTHORIZE_URL = "https://www.strava.com/oauth/authorize"
TOKEN_URL = "https://www.strava.com/oauth/token"
UPLOAD_URL = "https://www.strava.com/api/v3/uploads"

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_access_token() -> str:
    """Handle OAuth2 authentication to get access token."""
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=['activity:write'])
    authorization_url, state = oauth.authorization_url(AUTHORIZE_URL)

    # Direct user to Strava for authorization
    logging.info("Go to the following URL to authorize: %s", authorization_url)
    redirect_response = input("Paste the full redirect URL here: ")

    # Fetch the access token from Strava
    token = oauth.fetch_token(
        TOKEN_URL,
        authorization_response=redirect_response,
        client_secret=CLIENT_SECRET
    )

    logging.info("Access Token: %s", token['access_token'])
    return token['access_token']

def upload_gpx_file(access_token: str, gpx_file_path: str, activity_name: Optional[str] = "Morning Ride") -> None:
    """Upload the GPX file to Strava."""
    headers = {'Authorization': f'Bearer {access_token}'}

    with open(gpx_file_path, 'rb') as gpx_file:
        files = {
            'file': (gpx_file_path, gpx_file),
            'data_type': (None, 'gpx'),
            'name': (None, activity_name),
        }
        response = requests.post(UPLOAD_URL, headers=headers, files=files)

        if response.status_code == 201:
            logging.info("GPX file uploaded successfully!")
        else:
            logging.error("Failed to upload GPX file. Error: %s", response.json())

if __name__ == "__main__":
    try:
        # Get the access token
        access_token = get_access_token()

        # Path to your GPX file
        gpx_file_path = "../activities/Morning_Ride.gpx"

        # Upload the GPX file
        upload_gpx_file(access_token, gpx_file_path)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
