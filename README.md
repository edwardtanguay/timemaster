# timemaster

This app parses a timesheet.txt file and generates a JSON file with the parsed data for a report on how much time is spent in various projects.

- repo: https://github.com/edwardtanguay/timemaster

## Set up backend

-   (root directory of this project)
-   `python -m venv .venv`
-   (Linux/Mac) `source .venv/bin/activate`
-   (Windows with bash) `source .venv/Scripts/activate`
-   (Windows command line) `.venv\Scripts\activate`
-   `pip install -r requirements.txt`

## Set up frontend

- `npm i`
- `npm run dev`

## npm scripts

- `npm run pd` - parse data (parses timesheet.txt to timedays.json)
- `npm run gh` - GitHub commit log
- `npm run backup` - backup site in ../BACKUP folder (as .zip file without node_modules)

