"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

talk_times = {}
longest_talker = None
longest_talk_time = 0

for call in calls:
    if call[0] not in talk_times:
        talk_times[ call[0] ] = 0
    if call[1] not in talk_times:
        talk_times[ call[1] ] = 0
    talk_times[ call[0] ] += int( call[3] )
    talk_times[ call[1] ] += int( call[3] )

for talker, time in talk_times.items():
    if time > longest_talk_time:
        longest_talker = talker
        longest_talk_time = time

print( "{0} spent the longest time, {1} seconds, on the phone during September 2016.".format( 
    longest_talker, longest_talk_time ) )