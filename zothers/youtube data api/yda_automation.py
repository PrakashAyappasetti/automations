import googleapiclient
import google_auth_oauthlib
import os

def get_youtube_client():
    api_key = 'AIzaSyDErzkPCy77To6Z20BfMyajzW53HcAlM0I'
    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    # scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    # credentials = flow.run_console()

    # from the Youtube DATA API
    # youtube_client = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    
print(get_youtube_client())
