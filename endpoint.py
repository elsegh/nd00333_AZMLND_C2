import requests
import json
import os
import ssl

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
# scoring_uri = ''

scoring_uri = 'http://4b064133-a240-49e9-9709-f6da8c69a306.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'GJeFy5E2rd2h9Tzc45taXCYdoI2scZhM'

# Two sets of data to score, so we get two results back "
data={
"Inputs":{   
 "data": [
          {       
            "age": 17,
	    "job": "blue-collar",
	    "marital": "married",
	    "education": "university.degree",
            "default": "no",
	    "housing": "yes",
            "loan": "yes",
	    "contact": "cellular",
	    "month": "may",
	    "duration": 971,
            "campaign": 1,
	    "pdays": 999,
	    "previous": 1,
	    "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.price.idx": 92.893,
	    "cons.conf.idx": -46.2,
	    "euribor3m": 1.299,
	    "nr.employed": 5099.1          
          },
          {
            "age": 87,
	    "job": "blue-collar",
	    "marital": "married",
	    "education": "university.degree",
	    "default": "no",
	    "housing": "yes",
	    "loan": "yes",
	    "contact": "cellular",
	    "month": "may",
	    "duration": 471,
            "campaign": 1,
            "pdays": 999,
	    "previous": 1,
	    "poutcome": "failure",
	    "emp.var.rate": -1.8,
	    "cons.price.idx": 92.893,
       	    "cons.conf.idx": -46.2,
	    "nr.employed": 5099.1,
            "euribor3m": 1.299
          }
	  ]
 }
 }
# 
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


