"""instagram.py

A Code to Detect Instagram Accounts Not Following Back
Input 2 json files listing following and followers as
downloaded from the Instagram account settings page.
Output will print a list of usernames for accounts not following back.

How to download the json files:
1. Go to "Accounts Center" then "Your information and permissions".
2. Click "Download your information".
3. Click "Download or transfer information".
4. Click your accounts, and choose all or some as wanted.
5. Scroll to "Connections" and click "Followers and following".
6. "Download to device" and include all time for the date range.
7. Change format to JSON.
8. Wait for download to finish, with an email notification.
9. Download information and sort files to "Desktop" or other folder.

By Annika Feng April 2025
Updated by Annika Feng December 2025"""

#import libraries needed
import pandas as pd
import json

#open following file
file = 'Desktop/following.json' #or other file location/name
with open(file) as train_file:
    dict_train = json.load(train_file)
    
train = pd.DataFrame.from_dict(dict_train, orient='index')
train.reset_index(level=0, inplace=True)

following = pd.DataFrame(train)
following = pd.DataFrame.stack(following)

following = following.tolist()
len(following)

#create list of following
following2 =[]

for each in range(1, len(following)):
    variable = following[each]['string_list_data'][0]['href'] #changed from value, 2025
    following2.append(variable[29:]) #changed from no index, 2025

#print(following2) #if needed

#open followers file
file = 'Desktop/followers_1.json' #or other file location/name

with open(file) as train_file:
    followers = json.load(train_file)

#create list of followers
followers2 = []

for each in range(0, len(followers)):
    variable = followers[each]['string_list_data'][0]['value']
    followers2.append(variable)

#print(followers2) #if needed

#check which followers are not following back
nonmutuals = []

for each in following2:
    if each not in followers2:
        nonmutuals.append(each)
        print(each)

print(len(nonmutuals))
