# gpx-data-manager

GPX Data Manager is a tool designed to help automate the process of uploading GPX files to Strava via the Strava API. This is the first phase of the project, which focuses on manually uploading GPX files to Strava after completing an activity, such as cycling or running.

Features

- Upload GPX files to Strava: Use the tool to upload GPS activity data (in GPX format) directly to your Strava account.
- OAuth2 Authentication: Securely authenticate with Strava using OAuth2, ensuring safe access to your account.
- Error Handling: Basic error handling ensures that failed uploads are logged and retried as needed.
- Command-Line Interface (CLI): Simple, easy-to-use CLI for uploading your GPX files.

Requirements

- Python 3.11
- A Strava Developer Account
- Strava API credentials (Client ID, Client Secret, Authorization Token) in a .env file as below:


```
STRAVA_CLIENT_ID=your_client_id
STRAVA_CLIENT_SECRET=your_client_secret
STRAVA_REDIRECT_URI=http://localhost:8080
```
