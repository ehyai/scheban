# -*- coding: utf-8 -*-
import sys
from slackbot.bot import respond_to
sys.path.append('..')
from google_calendar import events2text


@respond_to('今後の予定を教えて')
def respond_schedule(message):

    calendar_id = '78bdbb2eqlt3ur3ui32tn932e4@group.calendar.google.com'  # Cさん

    reply_message = events2text(calendar_id=calendar_id)
    #reply_message = events2text(calendar_id_A = calendar_id_A, calendar_id_B = calendar_id_B, calendar_id_C = calendar_id_C)
    message.reply(reply_message)