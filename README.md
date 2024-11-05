# Hacker News Jobs Splunk Dashboard

This repo contains the file structure and script to allow the most recent HackerNews job postings to be collected via API and sent to a Splunk Dashboard.

## Setup

1. Download,  install, and setup Splunk Enterprise on you local system: https://www.splunk.com/
2. Request a Develop license from Splunk, which you should receive via email.
3. Create a new App in your Splunk UI
4. Create a new Dashboard in your Splunk app
5. Obtain an HEC token from the Splunk settings UI
6. Export the HEC token to your virtual environment
7. Paste the [/bin/fetch_hacker_news.py](/bin/fetch_hacker_news.py) from this repo into the same location in your $SPLUNK_HOME/etc/apps/ directory where the App you've just created will be located.
8. Create a new panel in your Splunk Dashboard with this as the search input: index=* sourcetype=hacker_news_jobstories

<br>

![image](https://raw.githubusercontent.com/xanderstevenson/hacker-news-jobs-splunk-dashboard/main/images/Hacker_News_Dashboard.png)
