import os

from simple_salesforce import SalesforceLogin
from flask import Flask

instance_url = os.environ.get("SF_INSTANCE_URL")
consumer_key = os.environ.get("SF_CONSUMER_KEY")
private_key_path = os.environ.get("SF_PRIVATE_KEY_PATH")
username = os.environ.get("SF_USERNAME")
domain = os.environ.get("SF_DOMAIN")

app = Flask(__name__)

def get_access_token():
    access_token, _ = SalesforceLogin(
        domain=domain,
        instance_url=instance_url,
        username=username,
        privatekey_file=private_key_path,
        consumer_key=consumer_key,
    )
    return access_token

@app.route("/")
def login():
    try:
        access_token = get_access_token()
    except Exception as e:
        return {
            "error_message": str(e),
        }, 500
    return {
        "access_token": access_token,
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))