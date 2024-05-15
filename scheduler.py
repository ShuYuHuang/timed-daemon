import datetime
import time
import threading
import requests

def call_api(url, data):
    response = requests.post(url, json=data)
    print(f"API response status code for {url}: {response.status_code}, {response.json()}")

def thread_function(url, data, trigger_time):
    while True:
        current_time = datetime.datetime.now()
        # if current_time.hour == trigger_time.hour and current_time.minute == trigger_time.minute:
        if current_time.second == trigger_time.second:
            call_api(url, data)
        time.sleep(1)  # Check every minute

# Define API endpoints and data
api_data = [
    {"url": "http://0.0.0.0:8000/call_api",
     "data": {"key": "value1"}, "trigger_time": datetime.time(0, 0, 10)},
    {"url": "http://0.0.0.0:8000/call_api",
     "data": {"key": "value2"}, "trigger_time": datetime.time(0, 0, 20)},
    {"url": "http://0.0.0.0:8000/call_api",
     "data": {"key": "value3"}, "trigger_time": datetime.time(0, 0, 30)}
]

# Create and start a thread for each API
threads = []
for api in api_data:
    thread = threading.Thread(target=thread_function, args=(api["url"], api["data"], api["trigger_time"]))
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Main thread can continue with other tasks or sleep indefinitely
while True:
    time.sleep(10)