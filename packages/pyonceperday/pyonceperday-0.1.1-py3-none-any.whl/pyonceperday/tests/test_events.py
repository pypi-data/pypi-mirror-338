import pytest
from  ..events import Event, Occurance, is_occurance_overlapping, Days
from ..exceptions import OverMaxDurantion, OverRepeatLimit
from datetime import datetime
import pytz

def test_creates_single_event():
  event = Event("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), 30)
  results = event.create_occurances()
  assert len(results) == 1
  assert results[0].end == datetime(2025, 4, 3, 13, 30, tzinfo=pytz.UTC)

def test_creates_single_multiday_event():
  event = Event("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), 30)
  event.days = [ Days.SATURDAY, Days.SUNDAY ]
  results = event.create_occurances()
  assert len(results) == 2
  assert results[0].start == datetime(2025, 4, 5, 13, 0, tzinfo=pytz.UTC)
  assert results[0].end == datetime(2025, 4, 5, 13, 30, tzinfo=pytz.UTC)
  assert results[1].start == datetime(2025, 4, 6, 13, 0, tzinfo=pytz.UTC)
  assert results[1].end == datetime(2025, 4, 6, 13, 30, tzinfo=pytz.UTC)

def test_creates_repeated_events():
  event = Event("test", datetime(2025, 4, 7, 13, 0, tzinfo=pytz.UTC), 30)
  event.repeat = True
  event.repeat_number_of_weeks = 2
  event.days = [Days.MONDAY, Days.WEDNESDAY, Days.FRIDAY]
  results = event.create_occurances()
  assert len(results) == 9
  assert results[0].start == datetime(2025, 4, 7, 13, 0, tzinfo=pytz.UTC)
  assert results[1].start == datetime(2025, 4, 9, 13, 0, tzinfo=pytz.UTC)
  assert results[2].end == datetime(2025, 4, 11, 13, 30, tzinfo=pytz.UTC)
  assert results[3].start == datetime(2025, 4, 14, 13, 0, tzinfo=pytz.UTC)
  assert results[4].end == datetime(2025, 4, 16, 13, 30, tzinfo=pytz.UTC)
  assert results[5].start == datetime(2025, 4, 18, 13, 0, tzinfo=pytz.UTC)
  assert results[6].start == datetime(2025, 4, 21, 13, 0, tzinfo=pytz.UTC)
  assert results[7].end == datetime(2025, 4, 23, 13, 30, tzinfo=pytz.UTC)
  assert results[8].end == datetime(2025, 4, 25, 13, 30, tzinfo=pytz.UTC)



def test_occurance_overlap():
  oc1 = Occurance("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), datetime(2025, 4, 3, 13, 15, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 13, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 13, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is False

  oc1 = Occurance("test", datetime(2025, 4, 3, 13, 20, tzinfo=pytz.UTC), datetime(2025, 4, 3, 13, 30, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 13, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 13, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is True

  oc1 = Occurance("test", datetime(2025, 4, 3, 13, 16, tzinfo=pytz.UTC), datetime(2025, 4, 3, 13, 20, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 13, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 15, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is True

  oc1 = Occurance("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), datetime(2025, 4, 3, 15, 00, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 13, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 14, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is True

  oc1 = Occurance("test", datetime(2025, 4, 3, 9, 0, tzinfo=pytz.UTC), datetime(2025, 4, 3, 9, 30, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 9, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 10, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is True

  oc1 = Occurance("test", datetime(2025, 4, 3, 10, 0, tzinfo=pytz.UTC), datetime(2025, 4, 3, 10, 30, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 9, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 9, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is False

  oc1 = Occurance("test", datetime(2025, 4, 3, 8, 0, tzinfo=pytz.UTC), datetime(2025, 4, 3, 9, 30, tzinfo=pytz.UTC))
  oc2 = Occurance("test2", datetime(2025, 4, 3, 9, 15, tzinfo=pytz.UTC), datetime(2025, 4, 3, 9, 30, tzinfo=pytz.UTC))
  results = is_occurance_overlapping(oc1, oc2)
  assert results is True


def test_max_duration_constant():
  with pytest.raises(OverMaxDurantion):
    event = Event("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), 260)


def test_max_duration_constant2():
  event = Event("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), 60)
  with pytest.raises(OverMaxDurantion):
    event.duration = 300

  
def test_max_repeat_constant():
  with pytest.raises(OverRepeatLimit):
    event = Event("test", datetime(2025, 4, 3, 13, 0, tzinfo=pytz.UTC), 10)
    event.repeat = True
    event.repeat_number_of_weeks = 5

