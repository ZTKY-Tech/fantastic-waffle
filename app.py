from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/incoming", methods=["POST"])
def handle_incoming_message():
    # Retrieve the incoming message data
    message_data = request.form.get("Body")
    sender_number = request.form.get("From")

    # Process the message and generate a response
    response_message = "Thank you for your message! You said: {}".format(message_data)

    # Create a TwiML response with the generated message
    twiml_response = "<Response><Message>{}</Message></Response>".format(response_message)

    return twiml_response, 200, {'Content-Type': 'application/xml'}

if __name__ == "__main__":
    app.run(debug=True)
