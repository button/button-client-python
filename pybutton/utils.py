from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import hmac
import hashlib


def is_webhook_authentic(webhook_secret, request_body, sent_signature):
    '''Used to verify that requests sent to a webhook endpoint are from Button
    and that their payload can be trusted. Returns True if a webhook request
    body matches the sent signature and False otherwise.

    Args:
        webhook_secret (string): Your webhooks's secret key.  Find yours at
            https://app.usebutton.com/webhooks.

        request_body (string): UTF8 encoded byte-string of the request body

        sent_signature (string): "X-Button-Siganture" HTTP Header sent with the
            request.

    Returns:
        (bool) Whether or not the request is authentic
    '''

    encoded_sent_signature = sent_signature.encode('utf8')

    computed_signature = hmac.new(
      webhook_secret.encode('utf8'),
      request_body.encode('utf8'),
      hashlib.sha256
    ).hexdigest()

    if hasattr(hmac, 'compare_digest'):
        return hmac.compare_digest(
            computed_signature,
            encoded_sent_signature
        )

    return computed_signature == encoded_sent_signature
