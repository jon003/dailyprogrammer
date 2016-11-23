#!/usr/bin/python

''' Calculate button flair based on a file of users: time pressed '''

"""
The value of the countdown at the instant that someone presses the button determines 
the flair that they obtain on the subreddit. 

For example, if the counter is at 53.04 seconds, then I would obtain a 53 flair, 
as that is the number of seconds (rounded down). 

After a person presses the button, the countdown resets from 60.00 seconds. 

Today's challenge is simple - you'll be given a list of users in no particular order, 
and told at which time each user pressed the button; you'll need to work out which 
flair each user gets.  

You can assume that the countdown never runs to zero for this 
challenge, and that no two users will press the button at exactly the same moment.

Algorithm:
Read the first line of the file.  This is how many users to calculate scores for
Loop over # of users:
 read the string from the file
 split the string into the user, and the time
 round the time
 calculate the score (60 seconds, minus the time)
 output the user and the score.
"""

# Notes
# Rounding: 
#  print "%d" % round(53.04)

from sys import argv

script, filename = argv

file = open(filename)

# read the usercount in.  strip out the trailing newline.
usercount = file.readline()
usercount = usercount.rstrip('\n')

lines = file.readlines()

for line in lines:
  line = line.rstrip('\n')
  (user, score) = line.split(':')
  score = float(score)
  score = int(score)
#  score = round(score)
  if score > 60:
    score = score - 60
  score = 60 - score

  print "%s: %s" %  (user, score)

