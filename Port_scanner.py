#!/bin/python

			#Making a Port Scanner using python script
			
				# By Zein Rohail

import sys
import socket

from datetime import datetime as dt

				# Defining our target

if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1])	# Translate host name to IPv4
	
else:
	print("Invalid INPUT ")
	
				# Desigining Output
				
print("\n"+"-*" * 30)

print("\tScanning Target --> "+target)

print("\n\tTime started :: "+ str(dt.now()) )

print("-*" * 30)

try:
	for port in range (50,450): 		# Here you can enter Range what port you want to scan	***** Enter your desired range ***** 
	
		s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Here defining a variable (s) 
								    # which tells which IP (AF_NET) & port (SOCK_STREAM) 
								    # to connect
		
		socket.setdefaulttimeout(1)			    # This tells that after connection is made set default 
								    # timeout to 1 sec
	
		result = s.connect_ex((target,port))		    # Now this tells to connect to target which we at line 13 and through the port going through iteration of this loop.
	
		if result == 0:					    # Now if the port is open (0) is returned and port is not opened (1) is returned so it goes for the next port to check.
			print("\nPort {} is OPEN.".format(port))
			
	
		s.close()
	
except KeyboardInterrupt:					    # Here an exception would be used to exit program if a keyboard occours
	
	print("\n\n Exiting program...")
	sys.exit()
	
except socket.gaierror:						    # Here an exception would occour if no proper hostname is provided

	print("Error resolving Host name... ")
	sys.exit()
	
except socket.error:

	print("Can't Esablish connection to the Server...")
	sys.exit()
	
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# 				*DRAWBACKS*						|		*How to counter the Drawbacks*			|
# 											|								|
# 1. Scan one port at a time 								|		1.1. Use the concepts of multi-threading.	|
#											|								|
# 2. It can't do anything if a wrong input/argument is passed e.g 355.dhe.7fh.999	|		2.1. Better logic could be implemented.		|
#											|								|
#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Thanks for guiding Heath Adams.
