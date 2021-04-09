import argparse
import configparser
import getpass
import onetimesecret
import pyperclip


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ots.exe",
        description="""Create a OneTimeSecret and copy its link to the clipboard.

Credentials will be prompted for if not provided.

An INI config-file generator will be offered to retain credentials for future use.

Do not share your onetimesecret API key.""",
        formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
            prog, max_help_position=37
        ),
    )
    parser.add_argument(
        "-e",
        "--email",
        default=None,
        help="(str) Account info (email address) for onetimesecret.com",
    )
    parser.add_argument(
        "-a", "--apikey", default=None, help="(str) API key from onetimesecret.com"
    )
    parser.add_argument(
        "-s", "--secret", default=None, help="(str) The secret to share"
    )
    parser.add_argument(
        "-p",
        "--password",
        default=None,
        help="(str) The password to lock the secret (default is none)",
    )
    parser.add_argument(
        "-t",
        "--ttl",
        type=int,
        default=None,
        help="(int) Maximum time to live of the secret, in seconds (default 3600)",
    )

    args = parser.parse_args()
    secret = args.secret
    password = args.password
    ttl = args.ttl

    config = configparser.ConfigParser()
    try:
        config.read("ots_creds.ini")
    except Exception:
        pass

    try:
        email = config["OTS"]["email"]
    except Exception:
        email = args.email
    try:
        apikey = config["OTS"]["apikey"]
    except Exception:
        apikey = args.apikey
    if email is None or apikey is None:
        email = input("OneTimeSecret email: ")
        apikey = input("OneTimeSecret API key: ")

        generate = input("Generate ots_creds.ini? Insecure, but convenient. yes/no > ")

        if generate.lower() in "yes":
            config = configparser.ConfigParser()
            config["OTS"] = {
                "email": email,
                "apikey": apikey,
            }
            with open("ots_creds.ini", "w") as configfile:
                config.write(configfile)

    o = onetimesecret.OneTimeSecret(email, apikey)

    if secret is None:
        secret = input("Secret: ")
    if password is None:
        password = getpass.getpass("Password: ")
        if len(password) == 0:
            password = None
    if ttl is None:
        ttl = input("TTL (s): ")
        if len(ttl) == 0:
            ttl = 3600

    secret = o.share(secret, passphrase=password, ttl=ttl)

    print(f"\nhttps://onetimesecret.com/secret/{secret['secret_key']}")
    pyperclip.copy(f"https://onetimesecret.com/secret/{secret['secret_key']}")
