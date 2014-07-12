# request example

# http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import requests
import json
import cloudmessage

def makeHttpCall(cm):
	url = 'http://api-http.littlebitscloud.cc/v2/devices/00e04c1e0e1e/output'
	payload = {
		'percent': cm.percent,
		'duration_ms': cm.duration_ms
	}
	headers = {
		'Content-type': 'application/json',
		'Authorization': 'Bearer 6f157aa0b6863433a1f58e2b9eda96626f449bdf1309f787fd72e0fc27e69534',
		'Accept': 'application/vnd.littlebits.v2+json'
	}

	r = requests.post(url, data=json.dumps(payload), headers=headers)

	r.raise_for_status()

#	print r.text
#	print r.headers	


