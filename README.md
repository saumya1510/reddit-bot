# reddit-bot
Skeleton for Reddit Bot awaiting a purpose. For now, it just reads comments with the text - "What?" and replies with - "He said " + text of the parent comment.


## Running the bot:
1. Create a Reddit Account
2. Go to Preferences -> App -> Create an App -> Fill in the Details:
    * Name: Name of the bot
    * Select "script"
    * Add a description
    * Add ```http://localhost:8080``` as redirect url
3. Create App
4. Save the client ID and secret Key for authentication in praw.ini as shown below. 

## praw.ini 
```
  [zctabot]
  username: reddit-username
  password: reddit-password
  client_id: client ID
  client_secret: client secret key
```
