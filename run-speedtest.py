#!/usr/bin/python

import speedtest
import time
import os
from prometheus_client import start_http_server, Summary, Gauge

sleepDur = 60
if os.environ.get("DURATION") != None:
  sleepDur = int(os.environ.get("DURATION"))

servers = []
if os.environ.get("SERVERS") != None:
  servers = os.environ.get("SERVERS").split(",")

# If you want to test against a specific server
# servers = [1234]

s = speedtest.Speedtest()

#results_dict = s.results.dict()
#print results_dict

g_download = Gauge('download_speed', 'Download speed', labelnames=["server_id", "server_name"])
g_upload = Gauge('upload_speed', 'Upload speed', labelnames=["server_id", "server_name"])

def process_request(t):
  s.get_servers(servers)
  s.get_best_server()
  s.download()
  s.upload()
  results_dict = s.results.dict()
  svr_id = results_dict["server"]["id"]
  svr_name = results_dict["server"]["name"] + ' - ' + results_dict["server"]["sponsor"]
  g_download.labels(server_id=svr_id, server_name=svr_name).set(results_dict["download"])
  g_upload.labels(server_id=svr_id, server_name=svr_name).set(results_dict["upload"])
#  print results_dict["upload"]
#  print results_dict["download"]
  time.sleep(t)
  
if __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(9104) 
  # Generate some requests.
  while True:
    process_request(sleepDur)
