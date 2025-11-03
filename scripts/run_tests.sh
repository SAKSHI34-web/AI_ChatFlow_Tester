
set -e
echo "Running pytest tests against backend at ${AI_TEST_BASE:-http://localhost:5000}"
pytest -q
