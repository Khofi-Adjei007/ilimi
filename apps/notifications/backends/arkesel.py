import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class ArkeselSMSBackend:
    """
    Production SMS backend using Arkesel API v2.
    https://developers.arkesel.com
    """

    API_URL = 'https://sms.arkesel.com/api/v2/sms/send'

    def send(self, recipient, message, sender_id=None):
        api_key = settings.ARKESEL_API_KEY
        sender = sender_id or settings.SMS_SENDER_ID

        # Normalize Ghana phone numbers to international format
        phone = self._normalize_phone(recipient)

        payload = {
            'sender': sender,
            'message': message,
            'recipients': [phone],
        }

        headers = {
            'api-key': api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(
                self.API_URL,
                json=payload,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            logger.info(f"SMS sent to {phone}: {data}")
            return {'status': 'success', 'data': data}

        except requests.exceptions.Timeout:
            logger.error(f"SMS timeout sending to {phone}")
            return {'status': 'error', 'message': 'SMS gateway timeout'}

        except requests.exceptions.RequestException as e:
            logger.error(f"SMS error sending to {phone}: {str(e)}")
            return {'status': 'error', 'message': str(e)}

    def _normalize_phone(self, phone):
        """Convert Ghana numbers to international format."""
        phone = phone.strip().replace(' ', '').replace('-', '')
        if phone.startswith('0'):
            return f'+233{phone[1:]}'
        if phone.startswith('233'):
            return f'+{phone}'
        return phone