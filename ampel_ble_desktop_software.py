

# Code for the central device that controls all the ble ampels.
# Requirements:
# - It should be able to communicate with at least 8 devices.
# - Will have functionality set up the 

#import bluetooth			# bluez for python

from ampel_ble import *		# library with the definition of the ampel ble class
import time


macA = "80:7d:3a:Ba:12:86"
macB = "80:7d:3a:ba:1e:46"

# testing functionality of btle Peripheral class for better understanding #

time.sleep(.01)

per = btle.Peripheral("80:7d:3a:Ba:12:86")

time.sleep(.01)

print(per)

#per.connect("80:7d:3a:Ba:12:86")
print("\nSERVICES\n")
services = per.getServices()
for service in services:
	print(service)
	
print("\nCHARACTERISTICS\n")
characteristics = per.getCharacteristics()
for characteristic in characteristics:
	print(characteristic)

time.sleep(.01)


# print("\nDESCRIPTORS\n")
# descriptors = per.getDescriptors()
# for descriptor in descriptors:
	# print(descriptor)
	
time.sleep(.01)
	
print("\nSTART READING CHARACTERISTICS\n")
char_val = per.readCharacteristic(LED_CHAR_HANDLE)
print(char_val)

time.sleep(.01)


print("\nSTART WRITING CHARACTERISTICS\n")
for i in range(0,20):
	val = bytes("0x31", 'utf-8')
	per.writeCharacteristic(LED_CHAR_HANDLE,val, withResponse = True)
	time.sleep(.01)
	val = bytes("0x30", 'utf-8')
	per.writeCharacteristic(LED_CHAR_HANDLE,val, withResponse = True)
	time.sleep(.01)


# i = 1;
# for characteristic in characteristics:
	# char_val = per.readCharacteristic(i)
	# print("Attribute " + str(i))
	# print(char_val)
	# i = i+1;
# test constructor #
a1 = ampel_ble()


# test scan for Ampel devices #

mac_list = a1.scan_for_macs()						# scans for ampels and return their mac addresses.
print("\nscan finished")
print("list of the MACs of the ampel devices found:")
print(mac_list)
print("\n\n")

# test get/set mac addr

print("setting MAC address to the first of the scanned that matches with name AmpelBLE")
a1.set_mac_addr(mac_list[0])						# use the mac of the first ampel found 
a1mac = a1.get_mac_addr()
print("The mac address of the device is: " + a1mac)





# test get/set services ???


