# datapod-for-python-nuxt

This is a simple datapod template for a local site that displays data from a JSON file, which is created by a Python script that parses a text file.

- repo: https://github.com/edwardtanguay/datapod-python-nuxt
- live: https://datapod-python-nuxt.vercel.app

## Compatibility

-   ✔️ tested on Windows
-   ✔️ tested on Ubuntu

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

- `npm run cp` - create page
- `npm run pd` - parse data 
- `npm run gh` - GitHub commit log
- `npm run backup` - backup site in ../BACKUP folder (as .zip file without node_modules)

## Run Jupyter notebooks example

-   `cd dev`
-   `python -m ipykernel install --user --name=dpodsitevenv --display-name "Python (Dpod site)"`
-   `jupyter lab`

- other useful commands:
  - `jupyter kernelspec list`
  - `jupyter kernelspec uninstall dpodvenv`

## Testing (beta)

-   `npm test` (runs all pytests)

## Create HTML documentation for qtools (beta)

-   cd scripts
-   `pdoc qtools --output-dir docs`
-   see scripts/docs/index.html

## More Datapod templates and sites

https://datapod-tanguay-eu.vercel.app
