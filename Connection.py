import splunklib.client as client
import splunklib.results as results
from splunklib.binding import AuthenticationError

HOST = '127.0.0.1'
PORT = '8000'
USERNAME = 'darsh'
PASSWORD = 'p@ssw0rd'
try:
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
except Exception as e:
    print(str(e))