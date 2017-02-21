# -*- coding: utf-8 -*-
import sys

import datetime # datetimeモジュールのインポート
import locale   # import文はどこに書いてもOK(可読性などの為、慣例でコードの始めの方)

from slackbot.bot import respond_to
sys.path.append('..')
#from google_calendar import events2text
from google_calendar import Myevents2text

#from google calendar import get_upcoming_events
#from google_calendar import extract_datetime

@respond_to('今後の予定を教えて')
def respond_schedule(message):

    #calendar_id = '78bdbb2eqlt3ur3ui32tn932e4@group.calendar.google.com'  # Cさん
    calendar_id = 'dud65mi8acau7db6v129rs5un0@group.calendar.google.com'  # Cさん

    #reply_message = events2text(calendar_id=calendar_id)
    #reply_message = events2text(calendar_id_A = calendar_id_A, calendar_id_B = calendar_id_B, calendar_id_C = calendar_id_C)
    #message.reply(reply_message)

@respond_to('(\d+)日')
def respond_schedule(message,something):
    # 現在の月 d.month
    d = datetime.datetime.today()
    print('1.%s月%s日\n' % (d.month, something))

    calendar_id = 'dud65mi8acau7db6v129rs5un0@group.calendar.google.com'  #授業

    reply_message = Myevents2text(calendar_id=calendar_id,mymonth=d.month,myday=something)
    message.reply(reply_message)
    #if(Myevents2text(calendar_id=calendar_id,mymonth=d.month,myday=something) == True):
        #message.reply('%s日には%dという授業があるよ' % something, )

    #else:
        #message.reply('%s日には授業はないよ' % something)