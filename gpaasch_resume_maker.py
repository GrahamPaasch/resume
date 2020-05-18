# use "python -m IPython" for testing
import json
import docx

with open('gpaasch_2020_resume.json') as f:
    resume = json.loads(f.read())

document = docx.Document()

paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
prior_paragraph = paragraph.insert_paragraph_before('Lorem ipsum')

document.add_heading('The REAL meaning of the universe')
document.add_heading('The role of dolphins', level=2)

paragraph.style = 'List Bullet'

document.save('gpaasch_2020_resume.docx')