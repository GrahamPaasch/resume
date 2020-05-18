# use "python -m IPython" for testing
import json
import docx

with open('gpaasch_2020_resume.json') as f:
    resume = json.loads(f.read())

document = docx.Document()
align_center = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

my_text = document.add_paragraph()
my_text.alignment = align_center
my_name_title = my_text.add_run(resume['basics']['name'] + '\n', 'Title Char')

my_text.add_run(
    resume['basics']['email']
    + ' | '
    + resume['basics']['phone']
    + ' | '
    + resume['basics']['website']
    + ' | '
    + resume['basics']['location']['address']
    + '\n'
)

my_text.add_run('--------------------------------------------------------------------------\n')

document.save('gpaasch_2020_resume.docx')