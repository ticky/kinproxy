from flask import Flask, request, Response
import urllib2
from calendarprocessor import process_calendar
app = Flask(__name__)

@app.route('/')
def get_processed_calendar():
  kintoken = request.args.get('token', '')

  if kintoken == '':
    return 'No token supplied', 403

  try:
    calendarFile = urllib2.urlopen(urllib2.Request(
      'https://app.kinhr.com/app/api/dataexports/calendarsubscription/kinhr.ics?token=%s' % kintoken,
      headers={'User-Agent': 'kincalendarproxy/1.0'}
    ))
  except urllib2.HTTPError, e:
    print e
    return 'Could not fetch calendar', 500

  calendar = process_calendar(calendarFile)

  return Response(calendar.to_ical().replace('\r\n', '\n').strip(), mimetype='text/calendar')

if __name__ == '__main__':
  app.run(debug=True)
