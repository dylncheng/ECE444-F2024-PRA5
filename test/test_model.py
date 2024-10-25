import requests
from config import TEST_CASES, API_PREDICT_ENDPOINT

for i, test_case in enumerate(TEST_CASES):
    response = requests.post(API_PREDICT_ENDPOINT, json=test_case)
    print(f"Test Case {i+1}: {test_case['article']} | Prediction: {'True' if response.json()['prediction'] else 'False'}")