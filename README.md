Simple python script that captures volume snapshots every 5 minutes.  For day traders who want to watch which pair is gaining momentum.  It is cumulative, meaning that every 5 minutes it adds or subtracts to each pair. In its default configuration, it runs for an hour (12 five minute snapshots) and then resets
The pairs might be outdated. If Binance removes a pair, you will get an error. Check the pairs before you run it. Line 8-Line 169. Binance pairs with an initial value of 0 volume.
Line 200 – Line 267. Pairs traded on Binance. If you add/subtract some, do the same thing on lines 8-162.
Instructions.
I have tested it with Python 2.7. Obviously you need to have an account with Binance.
Line 3. Generate your API key and secret and put them on line 3.
Line 181. Delay between each snapshot countdown. By default, 15 seconds. You can change it accordingly.
Line 404. Delay in seconds, between each volume snapshot. Caution: You might get banned if you abuse the API. 5 minutes (300 seconds in line 404) works for me, but feel free to experiment.
Line 460. If you want to see volume decreases, change line 460 to 
sorted_x = sorted(cumulative.items(), key=operator.itemgetter(1), reverse=True)
Line 468. Runs 12 times. 12 times of 5 minute intervals = 1 hour. If you change this to zero it will simply calculate volume from the scratch (starting from zero). No cumulative effect.
Line 472. The default value of 1200 means it will run for 1200 hours before it stops. 
Am working on combining it with RSI in next version.

