from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'config/client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_upcoming_events(calendar_id='primary', max_results=10):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming {} events'.format(max_results))
    events_result = service.events().list(
        calendarId=calendar_id, timeMin=now, maxResults=max_results, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return []
    else:
        return events


def extract_datetime(datetime_text):
    ymd, time = datetime_text.split('T')
    year, month, date = ymd.split('-')
    hms, _ = time.split('+')
    hour, minute, second = hms.split(':')
    return year, month, date, hour, minute, second


def events2text(calendar_id='primary', max_results=0):
    events = get_upcoming_events(calendar_id, max_results)  #ここでmax_result件数を取ってくる
    text = ''
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        summary = event['summary']
        sy, smo, sd, sh, smi, ss = extract_datetime(start)
        ey, emo, ed, eh, emi, es = extract_datetime(end)
        text += '{}/{} {}:{}〜{}:{} {}\n'.format(smo, sd, sh, smi, eh, emi, summary)
        #月／日 開始時間:開始分～終了時間:終了分 授業名

    return text

#ここから自分の
def Myevents2text(calendar_id='primary', max_results=50 ,mymonth=0,myday=0):
    #その日のうちで一番速い授業の名前と開始時刻と開始分を調べる

    events = get_upcoming_events(calendar_id, max_results)  # ここでmax_result件数を取ってくる
    text = ''
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        summary = event['summary']
        sy, smo, sd, sh, smi, ss = extract_datetime(start)
        ey, emo, ed, eh, emi, es = extract_datetime(end)
        print('2-1.%s月%s日\n' % (mymonth, myday))
        print('2-2.%s月%s日\n' % (smo, sd))
        smo2="{0:02d}".format(mymonth)
        print('2-3.%s月%s日%s\n' % (smo, sd,summary))
        if (smo==smo2 and sd==myday):
            text += '%s月%s日は%s時%s分から%sという授業が始まるよ。' % (mymonth,sd,sh,smi,summary)
            return text

            #return smo, sd, summary
    text += '%s日には授業ないよ。'% myday
    return text
    #return False

    #sy, smo, sd, sh, smi, ss = extract_datetime(start)
    #開始時刻、開始分、授業名を返す
    # return sh, smi, summary


if __name__ == '__main__':
    import pprint

    #calendar_id = '7nojpgg81q5l83g8ph7u3v60qs@group.calendar.google.com' #Aさん
    #calendar_id = 'qjai2sr4f4cdkcg5teq5pfe494@group.calendar.google.com'  #Bさん
    #calendar_id = '78bdbb2eqlt3ur3ui32tn932e4@group.calendar.google.com' #Cさん
    calendar_id = 'dud65mi8acau7db6v129rs5un0@group.calendar.google.com'  # 授業

    pprint.pprint(get_upcoming_events(calendar_id=calendar_id))
    #pprint.pprint(get_upcoming_events(calendar_id_A=calendar_id_A,calendar_id_B=calendar_id_B,calendar_id_C=calendar_id_C))