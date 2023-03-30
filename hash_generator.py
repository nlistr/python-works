import time
import hashlib

def generateHash():
  email = 'z.alajlan@toyou.io'.lower()
  phone = '9665531144221'
  key = '8Tyr4EDw!2sN'
  # Get the current timestamp as a string
  current_time = str(int(time.time()))
  # Print the current time
  print("Current time:", current_time)
  return hashlib.sha256((current_time + email + phone + key).encode()).hexdigest()

print(generateHash())