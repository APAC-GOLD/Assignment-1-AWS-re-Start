from fastapi import FastAPI, HTTPException, status
from typing import Dict, List

app = FastAPI()

# Sample below
# messages: Dict[str, str] = {
#     "message_1": "Hello, World!",
#     "message_2": "This is a saved message",
# }

messages: Dict[str, str] = {}


# Part 3.1. POST api (10 marks)
# ====================================================================================
# This intends to create a simple message
# Implement the POST /message API with a query parameter taking in str as message:
# - Save the message content (value) and message id (key) into dictionary `messages`
# - The key of the dict should be message_{index}, eg. `message_1`, `message_2`
# - Automatically increment the index value somehow
# - Ensure that you can avoid overwriting and existing key when calling this POST API
# - If the message is saved successfully, check to status code 200
@app.post("/message")
def create_message(message: str):
    # ========================================================================
    global index
    index = 1
    key = f"message_{index}"
    while key in messages:
        index += 1
        key = f"message_{index}"
    messages[key] = message
    index += 1
    return {"status": "success"}


print(messages)

# ========================================================================
#pass


# Part 3.2. GET all messages api (3 marks)
# ====================================================================================
# Return all saved messages, with code 200
# If there is no message, return code 404
@app.get("/")
def get_all_messages() -> dict:
    # ========================================================================
    if not messages:
        raise HTTPException(status_code=404, detail="No message (404)")
    return {"status": 200, "messages": messages}

    # ========================================================================
    #pass


# Part 3.3. GET single messages api, given a message_key (5 marks)
# ====================================================================================
# Get a message content, given a message key, eg. GET /message/message_1
# If a key does not exist, return code 404
@app.get("/message/{key}")
def get_message(key: str) -> str:
    # ========================================================================
    if key not in messages:
        raise HTTPException(status_code=404, detail="Key Does Not Exist")
    return messages[key]

    # ========================================================================
    #pass


# Part 3.4. PATCH single messages api, give message_key and new_message (5 marks)
# ====================================================================================
# Update message content, given a message key,
# - eg. PATCH /message/message_1 and also provide query string variable `message`
# - If a message key does not exist, return code 404
# - If a message key indeed exist, override, and return the updated value
@app.patch("/message/{key}")
def update_message(key: str, new_message: str) -> str:
    # ========================================================================
    if key not in messages:
        raise HTTPException(status_code=404, detail="Message Key Does Not Exist")
    messages[key] = new_message
    return new_message
    # ========================================================================
    #pass


# Part 3.5. DELETE single message given message_key (3 marks)
# ====================================================================================
# Delete message key and value, given a message_key,
# - eg. DELETE /message/message_1
# - If a message key does not exist, return code 404
# - If a message key indeed exist, delete, and return the message value (similar to pop)
@app.delete("/message/{key}")
def delete_message(key: str) -> str:
    # ========================================================================
    if key not in messages:
        raise HTTPException(status_code=404, detail="Message Key Does Not Exist")
    message = messages.pop(key)
    return message
    # ========================================================================
    #pass
