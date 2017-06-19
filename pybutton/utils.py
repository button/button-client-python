from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import hmac
import hashlib


def is_webhook_authentic(webhook_secret, request_body, sent_signature):
    '''Used to verify that requests sent to a webhook endpoint are from Button
    and that their payload can be trusted. Returns True if a webhook request
    body matches the sent signature and False otherwise.

    Args:
        webhook_secret (basestring): Your webhooks's secret key.  Find yours at
            https://app.usebutton.com/webhooks.

        request_body (basestring): UTF8 encoded byte-string of the request body

        sent_signature (basestring): "X-Button-Siganture" HTTP Header sent with
            the request.

    Returns:
        (bool) Whether or not the request is authentic
    '''

    computed_signature = hmac.new(
        as_bytes(webhook_secret),
        as_bytes(request_body),
        hashlib.sha256
    ).hexdigest()

    if hasattr(hmac, 'compare_digest'):
        return hmac.compare_digest(
            computed_signature,
            as_bytes(sent_signature, True)
        )

    return computed_signature == sent_signature


def as_bytes(v, only_py_2=False):
    '''Converts v to a UTF-8 byte string if unicode, else returns identity.

    Args:
        v (str|unicode): the string to convert

        only_py_2 (bool): If true, only converts to bytes if running in a
            python 2 interpretter

    Returns:
        (byte string): A byte string copy, UTF-8 enccoded
    '''

    python_version = sys.version_info[0]

    if only_py_2 and python_version != 2:
        return v

    should_encode = (
        python_version == 2 and isinstance(v, unicode) or
        python_version == 3 and isinstance(v, str)
    )

    if should_encode:
        return v.encode('utf8')

    return v
