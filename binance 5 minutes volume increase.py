from binance.client import Client

# client = Client('put here your API key', 'put here your API secret')

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
def runmeglobal():

	cumulative = { "ADABTC":0,
					"ADXBTC":0,
					"AEBTC":0,

					"AIONBTC":0,
					"AMBBTC":0,
					"APPCBTC":0,

					"ARKBTC":0,
					"ARNBTC":0,
					"ASTBTC":0,

					"BATBTC":0,
					"BCCBTC":0,
					"BCDBTC":0,

					"BCPTBTC":0,
					"BLZBTC":0,
					"BNBBTC":0,

					"BNTBTC":0,

					"BQXBTC":0,
					"BRDBTC":0,
					"BTGBTC":0,

					"BTSBTC":0,
					"CDTBTC":0,
					"CHATBTC":0,

					"CMTBTC":0,
					"CNDBTC":0,
					"CTRBTC":0,

					"DASHBTC":0,
					"DGDBTC":0,
					"DLTBTC":0,

					"DNTBTC":0,
					"EDOBTC":0,
					"ELFBTC":0,

					"ENGBTC":0,
					"ENJBTC":0,
					"EOSBTC":0,

					"ETCBTC":0,
					"ETHBTC":0,
					"EVXBTC":0,

					"FUELBTC":0,
					"FUNBTC":0,
					"GASBTC":0,

					"GTOBTC":0,
					"GVTBTC":0,
					"GXSBTC":0,

					"HSRBTC":0,
					"ICNBTC":0,
					"ICXBTC":0,

					"INSBTC":0,
					"IOSTBTC":0,
					"IOTABTC":0,

					"KMDBTC":0,
					"KNCBTC":0,
					"LENDBTC":0,

					"LINKBTC":0,
					"LRCBTC":0,
					"LSKBTC":0,

					"LTCBTC":0,
					"LUNBTC":0,
					"MANABTC":0,

					"MCOBTC":0,
					"MDABTC":0,
					"MODBTC":0,

					"MTHBTC":0,
					"MTLBTC":0,
					"NANOBTC":0,

					"NAVBTC":0,
					"NCASHBTC":0,
					"NEBLBTC":0,
					"NEOBTC":0,

					"NULSBTC":0,
					"OAXBTC":0,
					"OMGBTC":0,

					"ONTBTC":0,

					"OSTBTC":0,
					"PIVXBTC":0,
					"POABTC":0,

					"POEBTC":0,
					"POWRBTC":0,

					"PPTBTC":0,
					"QSPBTC":0,
					"QTUMBTC":0,

					"RCNBTC":0,
					"RDNBTC":0,
					"REQBTC":0,

					"RLCBTC":0,
					"RPXBTC":0,
					"SALTBTC":0,

					"SNGLSBTC":0,
					"SNMBTC":0,
					"SNTBTC":0,

					"STEEMBTC":0,
					"STORJBTC":0,
					"STORMBTC":0,

					"STRATBTC":0,

					"SUBBTC":0,
					"TNBBTC":0,
					"TNTBTC":0,

					"TRIGBTC":0,
					"TRXBTC":0,
					"VENBTC":0,

					"VIABTC":0,
					"VIBBTC":0,
					"VIBEBTC":0,

					"WABIBTC":0,

					"WANBTC":0,

					"WAVESBTC":0,
					"WINGSBTC":0,

					"WTCBTC":0,

					"XEMBTC":0,

					"XLMBTC":0,
					"XMRBTC":0,

					"XRPBTC":0,
					"XVGBTC":0,
					"XZCBTC":0,

					"YOYOBTC":0,
					"ZECBTC":0,

					"ZILBTC":0,

					"ZRXBTC":0}


	def runme():	

		# Works only with Python 2.7


		import time

		print ("Counting 15 sec")
		import sys
		for i in range(15,0,-1):
		    time.sleep(1)
		    sys.stdout.flush()



		tickers = client.get_ticker()
		unicodedlist = unicode (tickers)
		


		coins = ["ADABTC",
				"ADXBTC",
				"AEBTC",

				"AIONBTC",
				"AMBBTC",
				"APPCBTC",

				"ARKBTC",
				"ARNBTC",
				"ASTBTC",

				"BATBTC",
				"BCCBTC",
				"BCDBTC",

				"BCPTBTC",
				"BLZBTC",
				"BNBBTC",

				"BNTBTC",

				"BQXBTC",
				"BRDBTC",
				"BTGBTC",

				"BTSBTC",
				"CDTBTC",
				"CHATBTC",

				"CMTBTC",
				"CNDBTC",
				"CTRBTC",

				"DASHBTC",
				"DGDBTC",
				"DLTBTC",

				"DNTBTC",
				"EDOBTC",
				"ELFBTC",

				"ENGBTC",
				"ENJBTC",
				"EOSBTC",

				"ETCBTC",
				"ETHBTC",
				"EVXBTC",

				"FUELBTC",
				"FUNBTC",
				"GASBTC",

				"GTOBTC",
				"GVTBTC",
				"GXSBTC",

				"HSRBTC",
				"ICNBTC",
				"ICXBTC",

				"INSBTC",
				"IOSTBTC",
				"IOTABTC",

				"KMDBTC",
				"KNCBTC",
				"LENDBTC",

				"LINKBTC",
				"LRCBTC",
				"LSKBTC",

				"LTCBTC",
				"LUNBTC",
				"MANABTC",

				"MCOBTC",
				"MDABTC",
				"MODBTC",

				"MTHBTC",
				"MTLBTC",
				"NANOBTC",

				"NAVBTC",

				"NCASHBTC",

				"NEBLBTC",
				"NEOBTC",

				"NULSBTC",
				"OAXBTC",
				"OMGBTC",

				"ONTBTC",

				"OSTBTC",
				"PIVXBTC",

				"POABTC",

				"POEBTC",

				"PPTBTC",

				"POWRBTC",

				"QSPBTC",
				"QTUMBTC",

				"RCNBTC",
				"RDNBTC",
				"REQBTC",

				"RLCBTC",
				"RPXBTC",
				"SALTBTC",

				"SNGLSBTC",
				"SNMBTC",
				"SNTBTC",

				"STEEMBTC",
				"STORJBTC",

				"STORMBTC",

				"STRATBTC",

				"SUBBTC",
				"TNBBTC",
				"TNTBTC",

				"TRIGBTC",
				"TRXBTC",
				"VENBTC",

				"VIABTC",
				"VIBBTC",
				"VIBEBTC",

				"WABIBTC",

				"WANBTC",

				"WAVESBTC",
				"WINGSBTC",

				"WTCBTC",

				"XEMBTC",

				"XLMBTC",
				"XMRBTC",

				"XRPBTC",
				"XVGBTC",
				"XZCBTC",

				"YOYOBTC",
				"ZECBTC",

				"ZILBTC",
				
				"ZRXBTC"]

		counter = len(coins)
		print ("Number of coins ", counter)

		#-------------------------------------------------------------------------
		import re
		# Imports regular expression to be used to search volumes wth decimals

		coinsinitivolumes ={}
		# Empty dictionary of coin-volume pair

		for x in range(0, counter):
			pairposition = unicodedlist.find(coins[x])
			VolumePosition=unicodedlist[pairposition:].find("quoteVolume")
			# Run the loop and find each coin pair.
			newposition = (pairposition + VolumePosition + 15)
			# Approximately 95 characters from pair is the value of the volume (24 hours volume)
			coinvolume = unicodedlist[newposition:newposition+17]
			tempcoinvalue = re.findall( r'\d+\.*\d*', coinvolume )
			# Clean text from actual value
			coinvolume = tempcoinvalue
			# Temporary assignment
			tempvaluepairforupdateofdictionary = {coins[x]: coinvolume}
			# Create pair of coin/value
			coinsinitivolumes.update(tempvaluepairforupdateofdictionary)
			# Update dictionary
		#--------------------------------------------------------------
		coinsinitvalues ={}
		for x in range(0, counter):
			coinsinitvalues[x] = (coins[x]+"initvalue")
		# Create initial value of coin pair

		for x in range(0, counter):
			coinsinitvalues[x] = coinsinitivolumes.get(coins[x])
			# Get each coin volume
			converttostring = ''.join(coinsinitvalues[x])
			# Create a sequence
			coinsinitvalues[x] = float(converttostring)
			# Create floating point value
		#--------------------------------------------------------------
		import time

		print ("Counting 5 minutes")
		import sys
		for i in range(300,0,-1):
		    time.sleep(1)

		    sys.stdout.flush()
		# # ------------------------------------------------------------
		tickers = client.get_ticker()
		unicodedlist = unicode (tickers)

		#----------------------------------
		coinsnewvolumes ={}
		# Empty dictionary of coin-volume pair

		for x in range(0, counter):
			pairposition = unicodedlist.find(coins[x])
			VolumePosition=unicodedlist[pairposition:].find("quoteVolume")
			# Run the loop and find each coin pair.
			newposition = (pairposition + VolumePosition + 15)
			# Approximately 95 characters from pair is the value of the volume (24 hours volume)
			coinvolume = unicodedlist[newposition:newposition+17]
			tempcoinvalue = re.findall( r'\d+\.*\d*', coinvolume )
			coinvolume = tempcoinvalue
			tempvaluepairforupdateofdictionary = {coins[x]: coinvolume}
			coinsnewvolumes.update(tempvaluepairforupdateofdictionary)
		#----------------------------------------

		coinsaftervalues ={}
		for x in range(0, counter):
			coinsaftervalues[x] = (coins[x]+"aftervalue")

		for x in range(0, counter):
			coinsaftervalues[x] = coinsnewvolumes.get(coins[x])
			converttostring = ''.join(coinsaftervalues[x])
			coinsaftervalues[x] = float(converttostring)
		#---------------------------------------------------------

		changes ={}
		for x in range(0, counter):
			changes[x] = (((coinsaftervalues[x] / coinsinitvalues[x])-1)*100)

		#-----------------------------------------------------------


		sortlist ={}
		for x in range(0, counter):
			sortlist[x] = [{'change':changes[x]}, {'coin':coins[x]}]
			# Sort the list
			
			# **********************************************************************************************************
			cumulative[coins[x]]=cumulative[coins[x]]+changes[x]
			# **********************************************************************************************************
	

		import operator
		from operator import attrgetter
		import timeit

		sorted_x = sorted(cumulative.items(), key=operator.itemgetter(1))


		for a,b in sorted_x:
			print (a,b)



	for x in range(0,12):
		print x, "times run"
		runme()

for x in range(0,1200):
	print "reset function"
	runmeglobal()

