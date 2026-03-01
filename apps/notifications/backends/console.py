class ConsoleSMSBackend:
    """
    Development SMS backend.
    Prints SMS messages to the console instead of sending them.
    """
    def send(self, recipient, message, sender_id=None):
        print(
            f"\n{'='*50}\n"
            f"SMS (Console Backend)\n"
            f"To: {recipient}\n"
            f"From: {sender_id or 'Ilimi'}\n"
            f"Message: {message}\n"
            f"{'='*50}\n"
        )
        return {'status': 'success', 'message_id': 'console-dev', 'recipient': recipient}