from TwitterFunctions import *


#gets user info from the bot account, grabs mentions from the last 10 minutes, puts tweet ID's into a list, and iterates over
#that list to reply to every mention
user = GetUser()
listOfMentions = ShowMentions(user)
tweetText = GetTweetText(user)
if listOfMentions != None:
    #prints contents of all @s to console, and then replies to all @s with a copy-paste of the @ tweet's contents

    #**Find a way to deal with tweets that it's already replied to. It throws errors rn, which works but isn't great**
    #**There must be a way to flag a tweet as having already been replied to**
    print(listOfMentions)
    for i in range(0, len(tweetText)):
        print(tweetText[i])
        x = tweetText[i]
        print("the tweet text '" + x + "' has been stored as a variable")
    for i in range(0,len(listOfMentions)):
        currID = listOfMentions[i]
        LikeTweet(currID)
        Reply(tweetText[i],currID)






