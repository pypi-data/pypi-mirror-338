import requests
import json
import logging


class DiscordNotifier:
    def __init__(self, webhook_url):
        """Initializes the DiscordNotifier with the webhook URL."""
        self.webhook_url = webhook_url

    def send_message(self, message, level="info"):
        """Sends a message to Discord."""
        color_map = {
            "info": 3066993,  # Blue
            "warning": 16776960,  # Yellow
            "error": 15158332,  # Red
        }

        payload = {
            "embeds": [
                {
                    "title": "Notification",
                    "description": message,
                    "color": color_map.get(level, 3066993),  # Default to blue
                }
            ]
        }

        try:
            response = requests.post(
                self.webhook_url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            logging.info(f"Discord message sent: {message}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send Discord message: {e}")
