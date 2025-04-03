from msal import PublicClientApplication
import json

# Configuration (Replace with your values)
CLIENT_ID = "<YOUR_CLIENT_ID>"
TENANT_ID = "<YOUR_TENANT_ID>"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read"]  # Change scopes based on your needs
TOKEN_FILE = "token.json"


def authenticate():
    
    """Authenticate user with Office 365 and return an access token."""
    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY)
    
    # Load token if it exists
    try:
        with open(TOKEN_FILE, "r") as f:
            token_data = json.load(f)
        accounts = app.get_accounts()
        if accounts:
            result = app.acquire_token_silent(SCOPES, account=accounts[0])
            if result:
                return result["access_token"]
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # No saved token, proceed with interactive login

    # Interactive authentication (User will log in)
    result = app.acquire_token_interactive(scopes=SCOPES)
    if "access_token" in result:
        with open(TOKEN_FILE, "w") as f:
            json.dump(result, f)
        return result["access_token"]

    raise Exception("Authentication failed")