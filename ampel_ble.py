

from bluepy import btle		# bluepy
#import bluetooth			# bluez
#from bluetooth.ble import DiscoveryService		# ble over bluez, not working

import logging

import time 	# sleeps and other necessary tools
import logging 	# an attempt to make debuggin easier 
#import datetime	# necessary for implementing timestamps

#logging.basicConfig(level=logging.DEBUG)		# enable debug messages
separator = "---------------------------------------------------"	# to separate debugging messages
terminator = ';'

# parameters used for getDescription and getValueText
COMPLETE_LOCAL_NAME = 9		# position 8 contains the name of the device

LED_CHAR_HANDLE = 0X2a
TEST_CHAR_HANDLE = 0X30


class ampel_ble(btle.Peripheral):			# inherits from the class defining a generic BLE Peripheral
	
	# class variables # 
	
	mac_addr = None			# contains mac address
	services = None			# list of the services
	connected = False		# to be sure we're in connected before requesting data
	dev_id = None			# when using multiple devices, to make easy to refer to them. (1,2,3...)	
	firmware_ver = None;	# we can also read the firmware version at the ampel device
	
	
	
	
	
	
	
	## constructor ##
	
	# The constructor of the class can be called without any parameters
	# giving the possibility to perform a scan to find the MAC addresses,
	# and assign them after it.
	
	
	def __init__(self, mac_addr = None, dev_id = None):
		if(mac_addr == None):
			logging.debug("Constructor Without mac address method called")
		else:
			logging.debug("Constructor WITH specific MAC was called")
			self.mac_addr = mac_addr
		
		self.dev_id = dev_id			# to control number of devices each execution. 
			
		logging.debug(separator)


	## destructor ##
	
	def __del__(self):
		pass
	
		## methods ##	
	
	def scan_for_macs(self): 	# not sure if necessary 
		logging.debug("scan_for_macs method was called")
		logging.debug(separator)
		
		ampel_mac_list = []
		
		for device_found in btle.Scanner(0).scan(1):
			print("readed MAC:   " + str(device_found.addr))
			for entry in device_found.getScanData():
				print (entry)
			mac_addr = "80:7d:3a:ba:1e:46"			# only for testing purposes, delete
			if(device_found.getValueText(COMPLETE_LOCAL_NAME) == "AmpelBLE"):
				print("Ampel found!!!")
				print("With MAC address: "+device_found.addr+ "\n\n")
				
				ampel_mac_list.append(device_found.addr)				# all MACs corresponding to an Ampel will be saved

		return(ampel_mac_list)		# return a list with the macs of all devices of type ampel_ble
	
	def set_mac_addr(self,mac_addr):
		logging.debug("set_mac_addr method was called")
		logging.debug(separator)
		self.mac_addr = mac_addr
		
	def get_mac_addr(self):
		logging.debug("get_mac_addr method was called")
		logging.debug(separator)
		return(self.mac_addr)
		
		
	def get_services(self):
		logging.debug("get_services method was called")
		logging.debug(separator)
		self.services = bluetooth.find_service(address = self.mac_addr)
		logging.debug("Services contained at the current device")	
			
	def print_services(self):
		logging.debug("print_services method was called")
		logging.debug(separator)

		for service in self.services:
			print(separator)
			print("Service Name: %s"    % service["name"])
			print("    Host:        %s" % service["host"])
			print("    Description: %s" % service["description"])
			print("    Provided By: %s" % service["provider"])
			print("    Protocol:    %s" % service["protocol"])
			print("    channel/PSM: %s" % service["port"])
			print("    svc classes: %s "% service["service-classes"])
			print("    profiles:    %s "% service["profiles"])
			print("    service id:  %s "% service["service-id"])
			print("")
	
	
	
	
