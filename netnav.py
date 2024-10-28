import urllib.request
import json

# Get IMDSv2 session token
token_req = urllib.request.Request("http://169.254.169.254/latest/api/token", method="PUT")
token_req.add_header("X-aws-ec2-metadata-token-ttl-seconds", 60)
with urllib.request.urlopen(token_req) as f:
	token = f.read().decode()

# Put interesting metadata into a dictionary
interesting_metadata = {}
for item_key in ["instance-id", "local-ipv4", "placement/region", "placement/availability-zone", "placement/availability-zone-id"]:
	metadata_req = urllib.request.Request(f'http://169.254.169.254/latest/meta-data/{item_key}')
	metadata_req.add_header("X-aws-ec2-metadata-token", token)
	
	with urllib.request.urlopen(metadata_req) as f:
		item_value = f.read().decode()
	
	interesting_metadata[item_key] = item_value

# Dump the dictionary to a file
with open("/var/www/html/index.html", "w") as f:
	json.dump(interesting_metadata, f)