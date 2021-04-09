# onetimesecret-cli
command-line interface for onetimesecret.com

Python compiled to exe with [Nuitka](https://github.com/Nuitka/Nuitka).

Uses https://github.com/utter-step/py_onetimesecret, modified for Python3.

```
usage: ots.exe [-h] [-e EMAIL] [-a APIKEY] [-s SECRET] [-p PASSWORD] [-t TTL]

Create a OneTimeSecret and copy its link to the clipboard.

Credentials will be prompted for if not provided.

An INI config file generator will be offered to retain credentials for future use.

Do not share your onetimesecret API key.

optional arguments:
  -h, --help                        show this help message and exit
  -e EMAIL, --email EMAIL           (str) Account info (email address) for onetimesecret.com
  -a APIKEY, --apikey APIKEY        (str) API key from onetimesecret.com
  -s SECRET, --secret SECRET        (str) The secret to share
  -p PASSWORD, --password PASSWORD  (str) The password to lock the secret (default is none)
  -t TTL, --ttl TTL                 (int) Maximum time to live of the secret, in seconds (default 3600)
