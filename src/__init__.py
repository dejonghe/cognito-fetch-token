#!/usr/bin/env python
import argparse

from pycognito import Cognito


def main():
    parser = argparse.ArgumentParser(description='Login and make request to api')
    parser.add_argument("-c", "--pool", help="The congito user pool id to login to", required=True)
    parser.add_argument("-a", "--app", help="The congito user pool app id to use", required=True)
    parser.add_argument("-s", "--secret", help="The congito user pool app id to use", required=True)
    parser.add_argument("-u", "--user", help="Username", required=True)
    parser.add_argument("-p", "--password", help="Password", required=True)
    args = parser.parse_args()

    u = Cognito(args.pool, args.app, client_secret=args.secret, username=args.user)
    u.authenticate(password=args.password)
    print("==================Login Data==================")
    print(f"id_token: {u.id_token}")
    print(f"refresh_token: {u.refresh_token}")
    print(f"access_token: {u.access_token} \n")

if __name__ == "__main__":
   main()
