def test_predict_success(client):
    payload = {
        "age": 40,
        "annual_income": 80000,
        "vehicle_age": 6,
        "past_claims": 1,
        "accident_severity": 4,
        "policy_tenure": 5,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json()["estimated_claim_amount"] > 0


def test_predict_validation_error(client):
    payload = {
        "age": 15,              # invalid (<18)
        "annual_income": -100,  # invalid
        "vehicle_age": 1,
        "past_claims": 0,
        "accident_severity": 3,
        "policy_tenure": 2,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
