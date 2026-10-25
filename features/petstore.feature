Feature: Petstore API BDD Tests

  Scenario: 1. Get pet by valid ID returns 200
    When I send a GET request to "/pet/1"
    Then the response status code should be 200

  Scenario: 2. Get pet by invalid ID returns 404
    When I send a GET request to "/pet/999999999"
    Then the response status code should be 404

  Scenario: 3. Find pets by status available returns 200
    When I send a GET request to "/pet/findByStatus" with params status=available
    Then the response status code should be 200

  Scenario: 4. Find pets by invalid status returns 400
    When I send a GET request to "/pet/findByStatus" with params status=invalid
    Then the response status code should be 400

  Scenario: 5. Create a new pet returns 200
    When I send a POST request to "/pet" with a valid pet body
    Then the response status code should be 200

  Scenario: 6. Update an existing pet returns 200
    When I send a PUT request to "/pet" with an updated pet body
    Then the response status code should be 200

  Scenario: 7. Delete a pet returns 200
    When I send a DELETE request to "/pet/1"
    Then the response status code should be 200

  Scenario: 8. Get store inventory returns 200
    When I send a GET request to "/store/inventory"
    Then the response status code should be 200

  Scenario: 9. Place an order returns 200
    When I send a POST request to "/store/order" with a valid order body
    Then the response status code should be 200

  Scenario: 10. Get order by invalid ID returns 404
    When I send a GET request to "/store/order/999999999"
    Then the response status code should be 404
