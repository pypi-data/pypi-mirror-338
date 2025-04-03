import pytest
import sendnotifications
from sendnotifications.sendonteams import NotifyMsTeams
from sendnotifications.sendonemail import NotifyEmail



def test_sendnotifications():
     messages = []
     messages.append("New adaptive card")
     messages.append("New method of message on teams channel")
     notifyt = NotifyMsTeams("dba-only",messages,"Title - Testing card")
     notifye = NotifyEmail("Title - Testing card",messages,"vthelu")
     print ("notifyt response:{}, notifye response{}".format(notifyt,notifye))


if __name__ == "__main__":
     pytest.main()