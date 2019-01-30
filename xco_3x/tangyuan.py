#!/usr/bin/env python
#coding=utf-8

from xco import XCO
import requests

####################################################################################

class ServiceActuator:

	@staticmethod
	def execute(serviceURI, arg):
		try:
			_data = arg.toString()
			_headers = {
				'content-type'	: 'application/xco; charset=utf-8',
				'User-Agent'	: 'tangyuan-python',
				'Connection'	: 'close'
			}
			r = requests.post(serviceURI, data = _data, headers = _headers)
			_xml = r.text
			return XCO.fromXML(_xml)
		except Exception as e:
			raise e


####################################################################################
