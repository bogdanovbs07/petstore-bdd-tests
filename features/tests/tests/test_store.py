from pytest_bdd import when

@when('I send a POST request to "/store/order" with a valid order body', target_fixture="response")
def send_post_order(api_client):
    session, base_url = api_client
    body = {"id": 2001, "petId": 1001, "quantity": 1, "status": "placed", "complete": True}
    return session.post(f"{base_url}/store/order", json=body)
