import pytest
from pytest_bdd import scenarios, when, then, parsers

scenarios("../features/petstore.feature")

@when(parsers.parse('I send a GET request to "{path}"'), target_fixture="response")
def send_get(api_client, path):
    session, base_url = api_client
    return session.get(f"{base_url}{path}")

@when(parsers.parse('I send a DELETE request to "{path}"'), target_fixture="response")
def send_delete(api_client, path):
    session, base_url = api_client
    return session.delete(f"{base_url}{path}")

@when(parsers.parse('I send a GET request to "{path}" with params status={status}'), target_fixture="response")
def send_get_with_params(api_client, path, status):
    session, base_url = api_client
    return session.get(f"{base_url}{path}", params={"status": status})

@when('I send a POST request to "/pet" with a valid pet body', target_fixture="response")
def send_post_pet(api_client):
    session, base_url = api_client
    body = {"id": 1001, "name": "doggie-bdd", "photoUrls": ["https://example.com/photo.jpg"], "status": "available"}
    return session.post(f"{base_url}/pet", json=body)

@when('I send a PUT request to "/pet" with an updated pet body', target_fixture="response")
def send_put_pet(api_client):
    session, base_url = api_client
    body = {"id": 1001, "name": "doggie-bdd-updated", "photoUrls": ["https://example.com/photo.jpg"], "status": "sold"}
    return session.put(f"{base_url}/pet", json=body)

@then(parsers.parse("the response status code should be {status_code:d}"))
def check_status(response, status_code):
    assert response.status_code == status_code, \
        f"Expected {status_code}, got {response.status_code}: {response.text}"
