import json
import re

from qtools import *

class Project:
	def __init__(self, minutes, name):
		self.suuid = qstr.generate_short_uuid(),
		self.minutes = minutes
		self.name = name

class TimeDay:
	def __init__(self, date, projects):
		self.suuid = qstr.generate_short_uuid(),
		self.date = date
		self.projects = projects

def parse() -> None:
	lines = qfil.get_lines_from_file("../data/timesheet.txt")

	days = []
	for i in range(0, len(lines)):
		line = lines[i].strip()
		if re.match(r"^-\s\d{4}-\d{2}-\d{2}$", line):
			date = line.replace("- ", "")
			projects = [
				Project(60, "Project A"),
				Project(120, "Project B"),
			]
			projects_dicts = [p.__dict__ for p in projects]
			day = TimeDay(
				date=date,
				projects=projects_dicts
			)
			
			days.append(day.__dict__)

	try:
		json_data = json.dumps(days, indent=4)

		with open("../parseddata/days.json", 'w') as json_file:
			json_file.write(json_data)
		
		qcli.message("Successfully updated days.json")

	except Exception as err:
		qcli.message(f"Error: {err}", "error")