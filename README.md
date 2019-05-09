# Simple Nexmo Sender

Use this by your own caution! Here is my suggestion: Read the source code before you use it.

## Requirements

1. Python 3
2. nexmo (`pip install nexmo`)

## Steps

1. Prepare the csv file (hard-coded `targets.csv`)
2. Set environment variable
	* `SMS_FROM`: any string
	* `NEXMO_API_KEY`: get it from your Nexmo dashboard
	* `NEXMO_API_SECRET`: get it from your Nexmo dashboard
	``` bash
	# bash example
	export SMS_FROM="My Company"
	export NEXMO_API_KEY="1qaz2wsx"
	export NEXMO_API_SECRET="123qweasdzxc"
	```
3. Run `main.py` CAREFULLY!
	* `python3 main.py`
