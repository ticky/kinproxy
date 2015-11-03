from icalendar import Calendar, vDate
import datetime
from pytz import timezone

def process_calendar(calendarFile):
  calendar = Calendar.from_ical(calendarFile.read())
  calendarName = calendar.decoded('X-WR-CALNAME')

  print 'Processing Calendar "%s"' % calendarName

  tzinfo = timezone(calendar.decoded('tzid'))

  for component in calendar.walk('VEVENT'):
    startDate = component.decoded('dtstart')

    if type(startDate) is not datetime.date and startDate.tzinfo is not None:
      startDateLocal = startDate.astimezone(tzinfo)

      endDate = component.decoded('dtend')
      endDateLocal = endDate.astimezone(tzinfo)

      if startDateLocal.hour == 9 and startDateLocal.minute == 0 and endDateLocal.hour == 17 and endDateLocal.minute == 0:
        print 'This event looks like a full-day thing!'
        component['dtstart'] = vDate(startDateLocal.date()).to_ical()
        component['dtend'] = vDate(endDateLocal.date() + datetime.timedelta(days=1)).to_ical()

      else:
        print 'This event doesn\'t look like a full-day thing!'

  print 'Processed Calendar "%s"' % calendarName

  return calendar

def test():
  print '\n\n%s' % process_calendar(open('example/calendar.ics','rb')).to_ical()

if __name__ == '__main__':
  test()
