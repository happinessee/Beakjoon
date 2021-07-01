import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2216792091655-2231529462418-t7qBRPN5xN0W42Wsm0LqhBhn"
 
post_message(myToken, "#projec", "")
