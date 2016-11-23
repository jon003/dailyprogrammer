""" Caesar cipher encoder/decoder from: https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/ """

from sys import argv

script, input = argv

print input.encode('rot13')
