from datetime import timedelta, datetime, date
import pytz
from .exceptions import OverMaxDurantion, OverRepeatLimit
from enum import Enum

MAX_DURATION = 120 
MAX_REPEAT_WEEKS = 4

class Days(Enum):
  MONDAY = 1
  TUESDAY = 2
  WEDNESDAY = 3
  THURSDAY = 4
  FRIDAY = 5
  SATURDAY = 6
  SUNDAY = 7

class Event:
  def __init__(self, name, dt, duration):
    self.name = name
    self.start_datetime = dt
    if duration > MAX_DURATION:
      raise OverMaxDurantion("Max duration is two hours")
    self.duration = duration
    self.repeat = False
    self.repeat_number_of_weeks = 0
    weekday = self.start_datetime.isoweekday()
    self.days = [Days(weekday)]
  
  def __setattr__(self, name, value):
    if name == "repeat_number_of_weeks":
      if value > MAX_REPEAT_WEEKS:
        raise OverRepeatLimit("Event can only repeat for a max of 4 weeks")
        
    if name == "duration":
      if value > MAX_DURATION:
        raise OverMaxDurantion("Max duration is two hours")
    
    self.__dict__[name] = value


  def create_occurances(self):
    calendar_info = self.start_datetime.isocalendar()
    print(calendar_info)
    results = []
    for day in self.days:
      start_date = datetime.fromisocalendar(calendar_info.year, calendar_info.week, day.value)
      start_date = start_date.replace(hour=self.start_datetime.hour, minute=self.start_datetime.minute, tzinfo=pytz.UTC)
      event_occurance = Occurance(self.name, start_date, start_date + timedelta(minutes=self.duration))
      results.append(event_occurance)
    if self.repeat == True:
      calendar_info = self.start_datetime.isocalendar()
      for x in range(1, self.repeat_number_of_weeks + 1):
        print(x)
        for day in self.days:
          print(day)
          repeated_startdateime = datetime.fromisocalendar(calendar_info.year, calendar_info.week + x, day.value)
          repeated_startdateime = repeated_startdateime.replace(hour=self.start_datetime.hour, minute=self.start_datetime.minute, tzinfo=pytz.UTC)
          new_occurance = Occurance(self.name, repeated_startdateime, repeated_startdateime + timedelta(minutes=self.duration))
          results.append(new_occurance)
      print(results)
    return results

class Occurance:
  def __init__(self, name, start, end):
    self.name = name
    self.start = start
    self.end = end
  
  def __repr__(self):
    return f"Occurance at {self.start.month} {self.start.day}, {self.start.year} {self.start.hour}:{self.start.minute} to {self.end.hour}:{self.end.minute}"

def is_occurance_overlapping(test_occurance, occurance):
  if test_occurance.start.year == occurance.start.year and test_occurance.start.month == occurance.start.month and test_occurance.start.day == occurance.start.day:
    # let's see if we are overlapping
    # does my test start time begin after the end of the occurance? 
    if test_occurance.start > occurance.end:
      return False
    beginning_start_delta = test_occurance.start - occurance.start
    real_time = beginning_start_delta.total_seconds() / 60
    # test event starts after occurance begins
    if real_time > 0:
      return True
    # starting right when another event start
    elif real_time == 0:
      return True
    # start time is before the start of the occurance
    elif real_time < 0:
      pass
    
    # see if the test_occurance end time is the start of the occurance
    if test_occurance.end == occurance.start:
      return False
    if test_occurance.end < occurance.start:
      return False
    beginning_end_delta = test_occurance.end - occurance.end
    real_time = beginning_end_delta.total_seconds() / 60

    return True
  return False