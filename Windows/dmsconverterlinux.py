while True:
	try:
		latdegrees = int(input("Input Latitude Degrees: "))
		latminutes = int(input("Input Latitude Minutes: "))
	except ValueError:
		print("\n[ERROR] Integer Numbers Only\n")
		continue
	while True:
		try:
			latseconds = float(input("Input Latitude Seconds: "))
		except ValueError:
			print("\n[ERROR] Decimals Numbers Only\n")
			continue
		break
	while True:
		try:
			longdegrees = int(input("\nInput Longitude Degrees: "))
			longminutes = int(input("Input Longitude Minutes: "))
		except ValueError:
			print("\n[ERROR] {}Decimals Numbers Only\n\n")
			continue
		break
	while True:
		try:
			longseconds = float(input("Input Longitude Seconds: "))
			break
		except ValueError:
			print("\n[ERROR] Decimals Numbers Only\n")
			continue
	lat = latdegrees + float(latminutes/60) + float(latseconds/3600)
	long = longdegrees + float(longminutes/60) + float(longseconds/3600)
	print("\nLatitude:",lat)
	print("\nLongitude:",long,"\n\n",)
	continue
