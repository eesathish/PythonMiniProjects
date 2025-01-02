import pywhatkit

# Get phone number and message
mobile = input('Enter Mobile No of Receiver (with country code) : ')
message = input('Enter Message you want to send : ')

# Send the message instantly
pywhatkit.sendwhatmsg_instantly(mobile, message)
