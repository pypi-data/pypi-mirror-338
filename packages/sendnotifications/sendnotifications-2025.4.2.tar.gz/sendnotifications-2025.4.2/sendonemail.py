import json

import boto3


class NotifyEmail:
    """Core NotifyEmail Class.
       Usage:

        Import sendnotifications
        messages = []
        messages.append("Test")
        messages.append("Test1")
        notify = NotifyEmail("Title - Testing card",messages,"vthelu")

        Parameters:
             title: str - Subject
             messages:str - Stack of messages
             recipient: str - Recepient Team Identifier

       Send Messages to subscribed email address"""
    topic_name = "sendnotification-sharedlib-sns-notify-email-events"

    def __init__(self, title: str, message_body: str, recepient: str):
        self.send_message_to_email(title, message_body, recepient)

    def send_message_to_email(self, title: str, message_body: str, recepient: str):
        client = boto3.client("sns")
        topic = client.create_topic(Name=self.topic_name)["TopicArn"]
        message_attr = {'Team': {'StringValue': recepient, 'DataType': 'String'}}
        response = client.publish(TargetArn=topic, Message=json.dumps(message_body), Subject=title,
                                  MessageAttributes=message_attr)
        print(response)

# def main():
#     messages = []
#     messages.append("New adaptive card")
#     messages.append("New method of message on teams channel")
#
#     notify = NotifyEmail("Title - Testing card",messages,"vthelu")
#
# if __name__ == "__main__":
#     main()
