# Deliberately pseudo-code so that you don't make this mistake

### CLIENT-SIDE CODE ###

# User credentials
id = 'mozilla'
secret = '3964a356-d631-4a58-8a8a-0ccad3d273a4'

# Parameters to send: action=create&id=mozilla&name=my-new-photo
params = { 'action': 'create', 'id': id, 'name': 'my-new-photo' }

# Create the message authentication code and append to the POST parameters
message = params + { 'secret': secret }
params += { 'mac' : hashlib.md5(message).hexdigest() }

# Make the POST request
requests.post('http://api.example.com/v4', data=params)

### SERVER-SIDE CODE ###

# Get the challenge MAC from the request
challenge_mac = params.delete('mac')

# Get the ID from the request, and their secret from the database
id = params.get('id')
secret = db.get(id, 'secret')

# Calculate the MAC the same way the client did
message = params + { 'secret': secret }
calculated_mac = hashlib.md5(message).hexdigest()

# Compare the two MACs
if challenge_mac == calculated_mac:
  do_stuff()
  return(200) # OK
else:
  return(403) # Not authorized