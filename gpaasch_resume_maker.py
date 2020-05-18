# use "python -m IPython" for testing
import json
import docx

with open('gpaasch_2020_resume.json') as f:
    resume = json.loads(f.read())

document = docx.Document()

document.add_heading(resume['basics']['name'], 0)

document.save('gpaasch_2020_resume.docx')