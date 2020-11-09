import os
from flask import Flask, render_template, request, abort, Blueprint
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant, IpMessagingGrant
from twilio.rest import Client
from twilio.base.exceptions import TwilioException, TwilioRestException


chat_route = Blueprint('chat_route',__name__)

twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')

try:
    twilio_client = Client()
except TwilioException:
    twilio_client = None


def get_chatroom(name):
    if twilio_client is None:
        return
    for conversation in twilio_client.conversations.conversations.list():
        if conversation.friendly_name == name:
            return conversation

    # a conversation with the given name does not exist ==> create a new one
    return twilio_client.conversations.conversations.create(
        friendly_name=name)

@chat_route.route('/chat')
def chat_index():
    return render_template('chat/index.html')


@chat_route.route('/chat/login', methods=['POST'])
def chat_login():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    conversation = get_chatroom(os.environ.get('CHATROOM', 'My Room'))
    conversation_sid = ''
    if conversation:
        try:
            conversation.participants.create(identity=username)
        except TwilioRestException as ex:
            # do not error if the user is already in the conversation
            if ex.status != 409:
                raise
        conversation_sid = conversation.sid

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room='My Room'))
    if conversation:
        token.add_grant(IpMessagingGrant(
            service_sid=conversation.chat_service_sid))

    return {'token': token.to_jwt().decode(),
            'conversation_sid': conversation_sid}

