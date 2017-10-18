import falcon
import json
from s1search_config import S1SHandler

employees = []

class Resource(object):
	def on_post(self, request, response):
		"""Handles POST requests"""
		
		sent_data = json.loads(request.stream.read())

		employees.append({
			sent_data.get("name"): len(employees)
		})

		print employees
		
		response.status = falcon.HTTP_200

		data = {
			"response" : ("employee %s inserted" % sent_data.get("name"))
		}

		response.body = json.dumps(data)

	def on_get(self, request, response):
		response.status = falcon.HTTP_200
		response.body = json.dumps({"employees": employees})

app = falcon.API()

app.add_route('/employees', Resource())