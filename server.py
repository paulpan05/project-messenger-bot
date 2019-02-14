import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAEL1wbf0fEBAJSCmMWBLVKGWaLsiZB2uq6GQRPjiO7d7Lx7tYvGgQZCZCNLrPwBACO3VkuRv1OUqSWBGs2OiZCQ2dliIRgtVYf03HaDI4OIx4GjmMfTnbZBkOe5LU43df0DFfBRyA2xg8iu0yV7XArSJjSuSWVYeYX1ciZArbEwZDZD"
VERIFICATION_TOKEN = "F3C5FF563AAD96338F62ABBF12681C6732A797C092FBA29B658DF41C68A4EC09"
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
# Webhook validation
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Success!", 200
    
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                # Echo Bot
                if messaging_event.get('message'):
                    if messaging_event['message'].get('text'):
                      # Retrieve the message
                      response = messaging_event['message']['text']
                      # Echo the message
                      bot.send_text_message(sender_id, response)
    return 'OK', 200

def log(message):
    from pprint import pprint
    pprint(message)
    sys.stdout.flush()

if __name__ == "__main__":
	app.run()
