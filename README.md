# Instagram Follower Count
## Overview
This Python script uses Instagrapi, an unofficial Instagram API, to analyze your Instagram followers. It provides two key functionalities:

Lists non-verified users whom you are following but who are not following you back.
Lists users who are following you, but you are not following back.

## Disclaimer
This script interacts with Instagram through an unofficial API (Instagrapi), which may be against Instagram's terms of service. Use it responsibly and at your own risk. Misuse may lead to your Instagram account being banned or penalized.

## Prerequisites
Python 3.x
Instagrapi package

## Installation
To use this script, you need to install the Instagrapi package. You can install it using pip:

pip install instagrapi

## Usage
Clone or download this repository.

Open the script in your preferred text editor.

Replace 'username' and 'password' in the cred.txt

Run the script using Python:

python main.py

## Options

You can choose whether you want to filter out Non-Verified Users or not.
There is a block in the code that you can change to let you be able to do that.

## Features
Non-Verified Users Not Following Back: Identifies non-verified users that you follow but who do not follow you back.
Users You Don't Follow Back: Finds users who follow you, but you are not following.

## Security Note
Your Instagram credentials are required to run this script. Please make sure of the security of your account credentials. Using environment variables or other secure methods to handle credentials is recommended.
