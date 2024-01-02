import pytest
import sqlite3
import unittest
from fastapi.testclient import TestClient
from .main import app


@pytest.fixture
def client():
    yield TestClient(app)


def test_sample(client):
    assert True


# ========================================================================
# TEST POST API
def test_post_owner_200_api(client):
    response = client.post(
        "/owners/",
        json={
            "first_name": "Mickey",
            "last_name": "Mouse",
            "national_id": "SHJDK432432",
        },
    )
    assert response.status_code == 200


# TEST GET BY OWNER KEY
def test_get_by_owner_key(client):
    response = client.get("/owners-full-details/1")
    assert response.status_code == 200


# TEST POST CAR
def test_post_car_200_api(client):
    response = client.post(
        "/cars/",
        json={
            "plate_number": "HAS531",
            "brand": "Toyota",
            "model": "Vitz",
            "year": 2012,
            "owner_id": 1,
            "id": 1,
        },
    )
    assert response.status_code == 200


# TEST GET CAR
def test_get_car(client):
    response = client.get("/cars-full-details/1")
    assert response.status_code == 200


# TEST PATCH BY MESSAGE KEY
def test_patch_by_message_key(client):
    response = client.patch(
        "/cars/1",
        json={"plate_number": "UWB-920"},
    )
    assert response.status_code == 200


# ATT NICK: TESTING CONTINUED (BONUS)
# ========================================================================
# If a message key indeed exist, delete, and return the message value (similar to pop)
def test_POP_by_message_key(client):
    response = client.patch(
        "/cars/1",
        json={"plate_number": "UWB-920"},
    )
    assert response.status_code == 200
    # Extract the message value
    message_value = response.json().pop("message", None)
    return message_value


# Find the number of records in the SQLight DB for Licence Plate "HAS531"
def test_vehicle_plate_records():
    conn = sqlite3.connect("vtnz.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM car WHERE plate_number = 'HAS531'")
    record_count = c.fetchone()[0]

    assert record_count > 0
    print(record_count)

    conn.close()


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_sample(self):
        self.assertTrue(True)

    def test_post_owner_200_api(self):
        response = self.client.post(
            "/owners/",
            json={
                "first_name": "Mickey",
                "last_name": "Mouse",
                "national_id": "SHJDK432432",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_get_by_owner_key(self):
        response = self.client.get("/owners-full-details/1")
        self.assertEqual(response.status_code, 200)

    def test_post_car_200_api(self):
        response = self.client.post(
            "/cars/",
            json={
                "plate_number": "HAS531",
                "brand": "Toyota",
                "model": "Vitz",
                "year": 2012,
                "owner_id": 1,
                "id": 1,
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_get_car(self):
        response = self.client.get("/cars-full-details/1")
        self.assertEqual(response.status_code, 200)

    def test_patch_by_message_key(self):
        response = self.client.patch(
            "/cars/1",
            json={"plate_number": "UWB-920"},
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
