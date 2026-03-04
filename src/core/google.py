'''
    Eli Mares
'''

'''
def calendar():
    # Call the Calendar API
    now = datetime.now(timezone.utc or pytz.utc)
    events_result = calendar_service.events().list(
        calendarId='rti648k5hv7j3ae3a3rum8potk@group.calendar.google.com',
        timeMin=now.isoformat(),
        maxResults=10,
        singleEvents=True,
        orderBy='startTime',
    ).execute()
    events = events_result.get('items', [])

    final_events = "<br>"

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        fin_date = parser.parse(start)
        try:
            delta = fin_date - now
        except:
            d = datetime.utcnow()
            delta = fin_date - d

        formatted = format_timedelta(delta) if delta > timedelta(0) else "------"

        final_events += (
            """<div class='calendar-event-container-lvl2'><span class='calendar-text-date'> """
            + formatted +
            """ </span><br>"""
        )
        final_events += (
            "<span class='calendar-text' id='calendar'>"+
            ''.join(event['summary'])+
            "</span></div>"
        )
        final_events += "<hr style='border: 1px #B0197E solid;'>"

    event_list = {'data': final_events}
    return jsonify(event_list)

'''