import pytest
import unittest
from fastapi.testclient import TestClient
from .main import app
from .main import messages

client = TestClient(app)


@pytest.fixture
def client():
    yield TestClient(app)


def test_sample(client: TestClient):
    assert True


# ========================================================================


# TEST CREATE
def test_create_message(client: TestClient):
    messages.clear()
    global index
    index = 1
    test_message = "Hello, World!"
    response = client.post("/message/?message=Hello, World!")

    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    assert "message_1" in messages
    assert messages["message_1"] == test_message


# TEST GET ALL
def test_get_all_messages(client: TestClient):
    response = client.post("/message/?message=welovepython")
    response = client.post("/message/?message=we love Priya and Kat")
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["messages"] == {
        "message_1": "Hello, World!",
        "message_2": "welovepython",
        "message_3": "we love Priya and Kat",
    }


# TEST GET
def test_get_message(client: TestClient):
    response = client.post("/message/?message=welovepython")
    assert response.status_code == 200
    response = client.get("/message/message_2")
    assert response.status_code == 200

    response = client.get("/message/message_1")
    assert response.status_code == 200


# TEST UPDATE
def test_update_message(client: TestClient):
    response = client.post("/message/?message=welovepython")
    assert response.status_code == 200
    response = client.patch("message/message_1?new_message=somethinggood")
    assert response.status_code == 200


# TEST DELETE
def test_delete_message(client: TestClient):
    response = client.post("/message/?message=welovepython")
    assert response.status_code == 200
    response = client.delete("message/message_2")
    assert response.status_code == 200


# ATT NICK: TESTING CONTINUED (BONUS)
# ========================================================================

# Test and return the number of "messages" stored in the temporary log
def test_message_count(client: TestClient):
    # Assuming messages is a dictionary storing your messages
    message_count = len(messages)
    print(f"There are {message_count} messages in the log.")
    assert message_count > 0  # or any other condition you want to check
    return messages


# post bad payload
def test_post_bad_payload(client: TestClient):
    response = client.post("/message/", json={"message_0": 637})
    assert response.status_code == 422  # "bad payload error"
    # used to compare output before/ after testing (below)
    print(messages)


def test_404_non_messages(client: TestClient):
    # does not exist in Dict
    response = client.get("/message/message_11")
    assert response.status_code == 404
    # create new message
    # do not use/overwright historical messages OR ids
    response = client.post("/message/?message=LOVE_Python_Too!")
    assert response.status_code == 200

    # get and delete messages


def test_delete_messages_and_get(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    response = client.delete("message/message_1")
    response = client.delete("message/message_2")
    response = client.delete("message/message_3")
    response = client.delete("message/message_4")
    response = client.delete("message/message_5")
    response = client.delete("message/message_6")
    return messages


print(messages)


# 404 message does not exist
def test_404_delete_no_message(client: TestClient):
    response = client.delete("message/message_10")
    assert response.status_code == 404
    # used to compare output before/ after testing (above)
    print(messages)


class TestApp(unittest.TestCase):
    def setUp(self):
        messages.clear()
        self.index = 1

    def test_sample(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
