class GoogleAuth:
    def login(self, username, password):
        self.user=username
        self.pas=password
        print(f"Logging in with Google: {self.user}")

    def logout(self):
        print("Logging out from Google.")

class FacebookAuth:
    def login(self,username,password):
        self.user=username
        self.pas=password
        print(f"Logging in with Facebook: {self.user}")

    def logout(self):
        print("Logging out from Facebook.")

class Authenticator:
    def __init__(self, auth_method):
        self.auth_method = auth_method  
    def login(self, username, password):
        self.auth_method.login(username, password)

    def logout(self):
        self.auth_method.logout()


if __name__ == "__main__":
    google_auth = Authenticator(GoogleAuth())
    google_auth.login("umanju@gmail.com", "password123")
    google_auth.logout()

    print()

    facebook_auth = Authenticator(FacebookAuth())
    facebook_auth.login("manju78@gmail.com", "password456")
    facebook_auth.logout()
