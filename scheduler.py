import datetime
import time
import threading
import requests

def call_api(url, data):
    response = requests.post(url, json=data)
    print(f"API response status code for {url}: {response.status_code}")

def thread_function(url, data, trigger_time):
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == trigger_time.hour and current_time.minute == trigger_time.minute:
            call_api(url, data)
        time.sleep(60)  # Check every minute

# Define API endpoints and data
api_data = [
    {"url": "https://api1.example.com/endpoint",
     "data": {"key1": "value1"}, "trigger_time": datetime.time(9, 0)},
    {"url": "https://api2.example.com/endpoint",
     "data": {"key2": "value2"}, "trigger_time": datetime.time(13, 30)},
    {"url": "https://api3.example.com/endpoint",
     "data": {"key3": "value3"}, "trigger_time": datetime.time(18, 0)}
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