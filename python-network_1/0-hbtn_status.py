#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

req = 'https://alu-intranet.hbtn.io/status'
response = requests.get(req)

print ("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
    