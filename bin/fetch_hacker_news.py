import requests
import json
from datetime import datetime
import os

# Splunk HEC configuration
splunk_url = "http://localhost:8088/services/collector/event"
splunk_token = os.getenv("SPLUNK_HEC_TOKEN")

headers = {
    "Authorization": f"Splunk {splunk_token}",
    "Content-Type": "application/json",
}

# API URLs
jobstories_url = "https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty"
item_url_template = "https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"

# Fetch job stories
try:
    response = requests.get(jobstories_url)
    response.raise_for_status()
    job_story_ids = response.json()  # This will be a list of job story IDs

    for story_id in job_story_ids:
        item_url = item_url_template.format(id=story_id)
        item_response = requests.get(item_url)
        item_response.raise_for_status()
        item_data = item_response.json()

        # Format the time to a human-readable format
        formatted_time = datetime.fromtimestamp(item_data["time"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Prepare the data entry
        entry = {
            "title": item_data["title"],
            "time": formatted_time,
            "url": item_data.get("url", ""),  # Use .get to avoid KeyError,
        }

        # Prepare the payload to send to Splunk as a separate event
        payload = {
            "event": entry,
            "sourcetype": "hacker_news_jobstories",  # You can set a specific sourcetype
        }

        # Send the event to Splunk
        splunk_response = requests.post(
            splunk_url, headers=headers, data=json.dumps(payload)
        )
        splunk_response.raise_for_status()  # Raise an error for bad responses
        print("Data sent to Splunk successfully:", splunk_response.json())

except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
