import http.client
import json

import urllib3

from .channels import NotifyChannels as nc
class NotifyMsTeams:
    """Core NotifyMSTeam Class.
    Usage:

     from
     messages = []
     messages.append("Test")
     messages.append("Test1")
     notify = NotifyMsTeams("homes-analytics-alerts",messages,"Test Title",1,"warn")

     Parameters:
          channel: str - Channel name
          messages:str - Stack of messages
          header_text: str - Title / Subject
          messagetype:str - 0 - Direct Mesage , 1 - Adapative Card (default)
          color:str = "good" - Alert Type , good , warn, attn

         e.g "dba-only",messages,"Test Title",1,"warn"
             "dba-only",messages,"Test Title"

    Send Messages to webhook url"""
    idx = 1
    channel = "dba-test-notifications"

    webhook_mapper = {
        0: {"workflow_name": "informational direct message workflow",
            "message_type": "Direct Message",
            "webhook": nc.webhook[channel]},
        1: {"workflow_name": "informational adaptive card",
            "message_type": "Preformed Adaptive Card",
            "webhook": nc.webhook[channel]},
    }

    workflow_name = webhook_mapper[idx]["workflow_name"]
    message_type = webhook_mapper[idx]["message_type"]
    webhook = webhook_mapper[idx]["webhook"]
    header_text = f""
    message = ""

    def __init__(self, channel: str = "dba-test-notifications", messages: str = "", header_text: str = None,
                 color: str = "good",
                 messagetype: str = 1) -> None:
        """Construct webhook object.:
        Args:
                channel: Teams webhook URL to send all cards (messages) to.
                messagetype: 0 - "driect message" / 1 - "adaptive card"
                color: "good" / "attention" / "warning"

        Returns:
                None.

        Raises:
                None.
        """
        message = ""
        self.channel = channel
        self.message = messages
        self.header_text = header_text
        if messagetype == 0:
            print("Direct message")
            if color == "good":
                color = "2DC72D"
            elif color == "warn":
                color = "f6b26b"
            elif color == "attn":
                color = "e06666"
            for msg in messages:
                message = message + msg + '<br>'
            response = self.send_message_to_ms_teams(self.webhook, header_text, message, color)

        elif messagetype == 1:
            print("Preformed adaptive card")

            if color == "warn":
                color = "warning"
            elif color == "attn":
                color = "attention"
            else:
                color = "good"
            for msg in messages:
                msg = msg.replace("<h6>", "**bold**").replace("</h6>", "").replace("<br>", "\n\n")
                message = message + msg + '\n\n'
            webhook = self.webhook['uri']
            adaptive_card = self.create_adaptive_card(header_text, message, color)
            response = self.send_adaptive_card_to_ms_teams(webhook, adaptive_card)
        print(response)

    def create_adaptive_card(self, header_text: str, message_body: str, color: str = "good") -> dict[
        str, str | list[dict[str, str | bool] | dict[str, str | bool]]]:
        try:

            '''
            create and return an adaptive card
            '''
            adaptive_card = {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.2",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": header_text,
                        "style": "heading",
                        "size": "Large",
                        "weight": "bolder",
                        "wrap": True,
                        "color": color
                    },
                    {
                        "type": "TextBlock",
                        "weight": "default",
                        "wrap": True,
                        "size": "default",
                        "text": message_body
                    },
                ]
            }
            self.header_text = header_text
            self.message = message_body
            return adaptive_card
        except:
            return None

    def send_adaptive_card_to_ms_teams(self, webhook: str, adaptive_card: dict[
        str, str | list[dict[str, str | bool] | dict[str, str | bool]]]) -> http.client.responses:
        try:
            '''
            send an adaptive card to an MS Teams channel using a webhook
            '''
            http = urllib3.PoolManager()
            payload = json.dumps(
                {
                    "type": "message",
                    "attachments": [
                        {"contentType": "application/vnd.microsoft.card.adaptive", "content": adaptive_card}]
                }
            )
            headers = {"Content-Type": "application/json"}
            response = http.request("POST", webhook, body=payload, headers=headers)
            print("response status:", response.status)
            return response
            if response.status >= 300:
                print(response)

        except:
            print('Status Code: {}'.format(response.status_code))
            print('Response: {}'.format(response.content))

    def send_message_to_ms_teams(self, webhook, title: str, message_body: str, theme: str = "2DC72D") -> http.client.responses:
        try:

            '''
            send a simple text message to an MS Teams channel using a webhook
    
            The webhook receives a simple message,
            the Power Automate workflow creates an adaptive card and posts to MS Teams
            Ensure that the Power Automate workflow has been so configured.
            '''
            http = urllib3.PoolManager()
            payload = json.dumps(
                {
                    "@context": "http://schema.org/extensions",
                    "type": "MessageCard",
                    "title": title,
                    "summary": "This workflow accepts a direct message rather than a preformed adaptive card",
                    "text": message_body,
                    "themeColor": theme
                }
            )
            headers = {"Content-Type": "application/json"}
            response = http.request("POST", webhook, body=payload, headers=headers)
            return response
            print("response status:", response.status)
            if response.status >= 300:
                print(response)

        except:
            print('Status Code: {}'.format(response.status_code))
            print('Response: {}'.format(response.content))



# def main():
#     messages = []
#     messages.append("New adaptive card")
#     messages.append("New method of message on teams channel")
#     notify = NotifyMsTeams("dba-only",messages,"Title - Testing card")
#
# if __name__ == "__main__":
#     main()
