from ..sendonemail import NotifyEmail
from ..sendonteams import NotifyMsTeams
def main():
     messages = []
     messages.append("New adaptive card")
     messages.append("New method of message on teams channel")
     notifyt = NotifyMsTeams("dba-only",messages,"Title - Testing card")
     notifye = NotifyEmail("Title - Testing card",messages,"vthelu")
     print ("notifyt response:{}, notifye response{}".format(notifyt, notifye))


if __name__ == "__main__":
     main()