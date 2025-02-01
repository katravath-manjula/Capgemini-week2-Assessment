#  Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        pass
class EmailNotification(Notification):
    def __init__(self,message):
        self.m=message
    def send(self):
        print(f"email  has been sended! {self.m}")

class SmsNotification(Notification):
    def __init__(self):
        super().__init__()

    def send(self):
        print(f"sms  has been sended")

email_ob = EmailNotification("Hello, this is an email!")
sms_ob = SmsNotification()


email_ob.send()
sms_ob.send()

 
        
        