import os
import uuid
from urlparse import urljoin

from django.conf import settings
from django.core.urlresolvers import reverse

from twilio.rest import TwilioRestClient


def send_sms(to_number, message_text):
    """
        Send an SMS message 'message_text' to a telephone
        number in 'to_number'
    """
    message = _get_client().messages.create(
        body=message_text,
        to=to_number,
        from_=settings.TW_FROM_NUMBER,
    )
    return message.sid


def make_call(to_number, audio_url):
    """
    Make a call to the number at 'to_number' and play the MP3 specified
    in 'audio_url'.
    """
    name = str(uuid.uuid4())

    # Write out the XML with the URL of the audio
    _write_twiml(name, audio_url)
    callback_url = urljoin(
        settings.TW_ROOT_URL,
        reverse("info", kwargs={'uuid': name})
    )

    call = _get_client().calls.create(
        to=to_number,
        from_=settings.TW_FROM_NUMBER,
        url=callback_url,
        method="GET",
        fallback_method="GET",
        status_callback_method="GET",
        record="false"
    )
    return call.sid


def _write_twiml(name, audio_url):
    # Generate XML file, save with name
    with open(os.path.join("/tmp", name + ".xml"), "w") as f:
        doc = """
            <?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Play loop="1">{}</Play>
            </Response>
        """.format(audio_url)
        f.write(doc.strip())


def _get_client():
    return TwilioRestClient(settings.TW_ACCOUNT_SID, settings.TW_AUTH_TOKEN)
