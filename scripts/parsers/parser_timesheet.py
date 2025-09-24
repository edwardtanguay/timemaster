import json
import re

from qtools import *

class TimeDay:
	def __init__(self, suuid, day):
		self.suuid = suuid
		self.day = day

def parse() -> None:
	lines = qfil.get_lines_from_file("../data/timesheet.txt")

	timedays = []
	for i in range(0, len(lines)):
		line = lines[i].strip()
		if re.match(r"^-\s\d{4}-\d{2}-\d{2}$", line):
			day = line.replace("- ", "")
			timeday = TimeDay(
				suuid=qstr.generate_short_uuid(),
				day=day
			)
			
			timedays.append(timeday.__dict__)

	try:
		json_data = json.dumps(timedays, indent=4)

		with open("../parseddata/timedays.json", 'w') as json_file:
			json_file.write(json_data)
		
		qcli.message("Successfully updated timedays.json")

	except Exception as err:
		qcli.message(f"Error: {err}", "error")