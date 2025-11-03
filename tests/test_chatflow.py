import requests
import json
import os

BASE = os.environ.get("AI_TEST_BASE", "http://localhost:5000")

def test_health():
    r = requests.get(f"{BASE}/health", timeout=5)
    assert r.status_code == 200
    j = r.json()
    assert j.get("status") == "ok"

def test_flow_basic():
    flow = {
        "name": "basic_greeting_flow",
        "steps": [
            {"user": "Hi", "expected_bot": "Hello! How can I help you today?"},
            {"user": "What is your name", "expected_bot": "I am TestBot, your testing assistant."},
            {"user": "Tell me a joke", "expected_bot": "Sorry, I didn't understand that. Could you rephrase?"}
        ]
    }
    for step in flow["steps"]:
        r = requests.post(f"{BASE}/chat", json={"message": step["user"]}, timeout=5)
        assert r.status_code == 200
        j = r.json()
        got = j.get("response", "")
        assert got == step["expected_bot"], f"Expected '{step['expected_bot']}', got '{got}'"
