import requests
import datetime
import base64
from urllib.parse import urlparse
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

# Configuration
API_KEY_ID = 'ff352204-5e82-4293-99bc-4d7cbee508ed'
PRIVATE_KEY_PATH = 'kalshi_private.key'
BASE_URL = 'https://trading-api.kalshi.com/trade-api/v2'

def load_private_key(key_path):
    with open(key_path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

def create_signature(private_key, timestamp, method, path):
    """Create the request signature."""
    # Strip query parameters before signing
    path_without_query = path.split('?')[0]
    message = f"{timestamp}{method}{path_without_query}".encode('utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

def get(private_key, api_key_id, path, base_url=BASE_URL):
    """Make an authenticated GET request to the Kalshi API."""
    timestamp = str(int(datetime.datetime.now().timestamp() * 1000))
    sign_path = urlparse(base_url + path).path
    signature = create_signature(private_key, timestamp, "GET", sign_path)

    headers = {
        'KALSHI-ACCESS-KEY': api_key_id,
        'KALSHI-ACCESS-SIGNATURE': signature,
        'KALSHI-ACCESS-TIMESTAMP': timestamp
    }

    return requests.get(base_url + path, headers=headers)

# Load private key
private_key = load_private_key(PRIVATE_KEY_PATH)
print("Private Key: ", private_key)
# Get balance
response = get(private_key, API_KEY_ID, "/portfolio/balance")

print(f"Your balance: ${response.json()}")