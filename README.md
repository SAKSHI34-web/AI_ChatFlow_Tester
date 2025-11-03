# AI ChatFlow Tester

Automated validation and testing scaffold for conversational AI systems.
This is a starter project skeleton including:
- A small Flask backend simulating a chatbot API.
- A static frontend to run manual conversation tests.
- Sample conversational flow JSON and automated pytest tests.
- Scripts to run tests and package the project.

## Quick start (Linux / macOS)
1. Create a virtualenv:
   python3 -m venv venv
   source venv/bin/activate

2. Install backend requirements:
   pip install -r backend/requirements.txt

3. Run the backend:
   python backend/app.py

4. Open `frontend/index.html` in your browser to use the manual dashboard.

5. Run automated tests:
   ./run_tests.sh

## Project structure
- backend/          -> Flask server implementing chatbot & API test endpoints
- frontend/         -> Static dashboard (HTML + JS) for manual testing
- flows/            -> Sample conversation flows (JSON)
- tests/            -> Pytest tests that exercise flows and API validation
- scripts/          -> Helper scripts
- README.md         -> This file

## Notes
This is a template. Replace simulated backend endpoints with real chatbot API endpoints and update tests to point at the correct URLs.
