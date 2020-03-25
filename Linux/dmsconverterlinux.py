#!/usr/bin/python3

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	LIGHTPURPLE = '\033[1;35m'
	BROWN = "\033[0;33m"
	PURPLE = "\033[1;34m"
	LIGHTGREEN = "\033[1;32m"
	CYAN = "\033[0;36m"
	LIGHTRED = "\033[1;31m"
	LIGHTCYAN = "\033[1;36m"
	LIGHTWHITE = "\033[1;37m"
	FAINT = "\033[2m"
	ITALIC = "\033[3m"
	BLINK = "\033[5m"
	NEGATIVE = "\033[7m"
	CROSSED = "\033[9m"
	PURPLE = "\x1b[35m"
	DARKGREY = "\x1b[90m"
	LIGHTYELLOW = "\x1b[93m"

while True:
	try:
		latdegrees = int(input("{}Input Latitude Degrees{}: ".format(colors.LIGHTGREEN,colors.LIGHTWHITE)))
		latminutes = int(input("{}Input Latitude Minutes{}: ".format(colors.LIGHTGREEN,colors.LIGHTWHITE)))
	except ValueError:
		print(colors.FAIL+"\n[ERROR] {}Integer Numbers Only\n".format(colors.LIGHTYELLOW),colors.END)
		continue
	while True:
		try:
			latseconds = float(input("{}Input Latitude Seconds{}: ".format(colors.LIGHTGREEN,colors.LIGHTWHITE)))
		except ValueError:
			print(colors.LIGHTRED+"\n[ERROR] {}Decimals Numbers Only\n".format(colors.LIGHTYELLOW),colors.END)
			continue
		break
	while True:
		try:
			longdegrees = int(input("\n{}Input Longitude Degrees{}: ".format(colors.LIGHTPURPLE,colors.LIGHTWHITE)))
			longminutes = int(input("{}Input Longitude Minutes{}: ".format(colors.LIGHTPURPLE,colors.LIGHTWHITE)))
		except ValueError:
			print(colors.LIGHTRED+"\n[ERROR] {}Decimals Numbers Only\n\n".format(colors.LIGHTYELLOW),colors.END)
			continue
		break
	while True:
		try:
			longseconds = float(input("{}Input Longitude Seconds{}: ".format(colors.LIGHTPURPLE,colors.LIGHTWHITE)))
			break
		except ValueError:
			print(colors.LIGHTRED+"\n[ERROR] {}Decimals Numbers Only\n".format(colors.LIGHTYELLOW),colors.END)
			continue
	lat = latdegrees + float(latminutes/60) + float(latseconds/3600)
	long = longdegrees + float(longminutes/60) + float(longseconds/3600)
	print("\nLatitude:"+colors.LIGHTCYAN,lat,colors.END)
	print("\nLongitude:"+colors.LIGHTCYAN,long,"\n\n",colors.END)
	continue
