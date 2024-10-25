import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from config import TEST_CASES, API_PREDICT_ENDPOINT

with open('api_latency.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Test Case #', 'Call Number', 'Time (seconds)'])

    for i, test_case in enumerate(TEST_CASES):
        for call in range(100):
            start_time = time.time()
            response = requests.post(API_PREDICT_ENDPOINT, json=test_case)
            end_time = time.time()
            response_time = end_time - start_time
            writer.writerow([f"{i + 1}", call + 1, response_time])

df = pd.read_csv('api_latency.csv')
average_latency = df.groupby('Test Case #')['Time (seconds)'].mean()
print(average_latency)

df.boxplot(by='Test Case #', column=['Time (seconds)'], grid=False)
plt.title('API Latency Boxplot by Test Case')
plt.xlabel('Test Case #')
plt.ylabel('Time (seconds)')
plt.savefig('latency_boxplot.png')
