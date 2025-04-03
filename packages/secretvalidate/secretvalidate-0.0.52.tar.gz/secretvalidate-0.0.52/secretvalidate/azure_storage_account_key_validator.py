from azure.storage.blob import BlobServiceClient
from secretvalidate.env_loader import (
    get_secret_active,
    get_secret_inactive,
    get_secret_inconclusive,
)
import base64
import re
import requests
import os


def extract_connection_string(text):
    pattern = r"(DefaultEndpointsProtocol=https;AccountName=(?P<AccountName>\w+);AccountKey=(?P<AccountKey>[\w+/]+==);EndpointSuffix=core\.windows\.net)"
    match = re.search(pattern, text)
    if match:
        string = match.group(1)
        if "BlobEndpoint" not in string:
            return match.group(1)
        pattern = r"(DefaultEndpointsProtocol.*?==)"
        blob_match = re.search(pattern, text)
        return blob_match.group(1)
    return


def build_connection_string(blob, secret):
    pattern1 = r"((?<=Microsoft\.Storage\/storageAccounts\/)[^\/]+)"
    match = re.search(pattern1, blob)
    if match:
        account_name = match.group(0)
        return f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={secret};EndpointSuffix=core.windows.net"

    return get_secret_inconclusive()


def validate_azure_storage_account_key(blob, secret, response):
    try:
        connection_string = None
        blob_type = blob["type"]

        if blob_type == "pull_request_comment":
            connection_string = build_connection_string(blob["blob"], secret)
        if blob_type == "commit":
            try:
                content = base64.b64decode(blob["blob"]).decode("utf-8")
            except UnicodeDecodeError:
                content = base64.b64decode(blob["blob"]).decode("latin-1")
            connection_string = extract_connection_string(content)
        if blob_type == "local_validation":
            connection_string = blob["connection_string"]

        container_name = "dummy"
        if not connection_string or "Inconclusive" in connection_string:
            return f"{get_secret_inconclusive()}: Unable to form or extract connection string"
        else:
            blob_client = BlobServiceClient.from_connection_string(connection_string)
            container_client = blob_client.get_container_client(container_name)
            # If we can list a blob, the key is valid
            blobs_list = container_client.list_blobs()
            for blob in blobs_list:
                print(blob.name)
                break
            return (
                get_secret_active()
                if response
                else "Azure Storage Account Key is valid"
            )
    except Exception as e:
        if "ErrorCode:AuthenticationFailed" in str(e) or "Failed to resolve" in str(e):
            return (
                get_secret_inactive()
                if response
                else "Azure Storage Account Key is invalid"
            )
        elif "ErrorCode:ContainerNotFound" in str(e) or "AuthorizationFailure":
            return (
                get_secret_active()
                if response
                else "Azure Storage Account Key is valid"
            )
        else:
            return (
                f"{get_secret_inconclusive()} validation: {e}"
                if response
                else f"Inconclusive validation: {e}"
            )


###########################
# Validate secret locally #
###########################


def validate_locally_with_account(account_name, secret):
    """
    Used for quick checks when developers report that revoked secrets have been reopened.
    Account name and secret can be retrieved from the GHAS alert
    """

    blob = {
        "type": "local_validation",
        "connection_string": f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={secret};EndpointSuffix=core.windows.net",
    }
    result = validate_azure_storage_account_key(blob, secret, True)
    return result


def validate_locally_with_url(alert_html_url, secret):
    """
    Used for quick checks when developers report that revoked secrets have been reopened.
    Uses alert URL can be retrieved from the GHAS alert
    """
    token = os.getenv("GH_TOKEN", "")
    HEADER = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "request",
    }
    try:
        url_path = alert_html_url.split("github.com/")
        owner, repo_name, _, _, alert_id = url_path[1].split("/")
        print(f"Retreiving locations_url")
        locations_res = requests.get(
            f"https://api.github.com/repos/{owner}/{repo_name}/secret-scanning/alerts/{alert_id}/locations",
            headers=HEADER,
        )
        locations_res.raise_for_status()
        locations_data = locations_res.json()

        print(f"Retrieving blob")
        blob_url = None
        loc_type = None
        try:
            for loc in locations_data:
                loc_type = loc["type"]
                if loc_type == "commit":
                    blob_url = loc["details"]["blob_url"]
                    break
                elif loc_type == "pull_request_comment":
                    blob_url = loc["details"]["pull_request_comment_url"]
                    break
                else:
                    print(f"Unhandled location type: {loc_type}")
                    return
        except IndexError:
            print(f"Secret URL not found in locations data")
        blob_res = requests.get(blob_url, headers=HEADER)
        blob_data = blob_res.json()

        if blob_data.get("message", "") == "Not Found":
            print(
                f"Blob not found: {loc_type} has probably been deleted. This secret will not be validated."
            )
            return
        blob = {
            "type": loc_type,
            "blob": blob_data["content"] if loc_type == "commit" else blob_data["body"],
        }

        result = validate_azure_storage_account_key(blob, secret, True)
        return result
    except KeyError as e:
        print(f"Error retrieving secret location: {e}")
    except requests.exceptions.RequestException as err:
        print(f"Error retrieving git blob: {err}")
        print(f"Error retrieving git blob: {blob_url}")


# validate_locally_with_account(account_name, secret)
# validate_locally_with_url(url, secret)
