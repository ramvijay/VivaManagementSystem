import gspread
import pandas as pd
import json
from oauth2client.client import SignedJwtAssertionCredentials
from VivaManagementSystem.models import Faculty
from VivaManagementSystem.models import Student
from VivaManagementSystem.models import Course
#-------------------Donot change the code above this line---------------------------------

def update_faculty_records():
    SECRETS_FILE = 'data/VivaManagementSystem-f7cde54a5c9e.json'
    FILEURL = "https://docs.google.com/spreadsheets/d/1nlYqgnmxiLfkGiIEyBUZ4IlFOVTrwok4WUMBHFFl84c/edit#gid=1604066109"
    SCOPE = ['https://spreadsheets.google.com/feeds']
    JSON_KEY = json.load(open(SECRETS_FILE))
    credentials = SignedJwtAssertionCredentials(JSON_KEY['client_email'], \
                                                JSON_KEY['private_key'], SCOPE)
    gc = gspread.authorize(credentials)
    # Open up the workbook based on the spreadsheet name
    workbook = gc.open_by_url(FILEURL)
    # Get the first sheet
    sheet = workbook.sheet1
    # Extract all data into a dataframe
    faculty_data = pd.DataFrame(sheet.get_all_records())
    num_db_records = len(Faculty.objects.all())
    try:
        # Append rows to the Database
        for index, row in faculty_data.loc[num_db_records:].iterrows():
             model = Faculty()
             model.title = row['Title']
             model.name = row['Full Name']
             model.designation = row['Designation']
             model.short_name = row['Short Name used in Department']
             model.employee_id = row['Employee ID']
             model.core_competency = row['Core Competency']
             model.is_guide = 0
             model.students_allocated = 0
             model.email_id = row['E-mail ID']
             model.areas_of_interest = row['Area of Interest for project guidance']
             model.phone_number = row['Phone number']
             model.save()
    except:
        pass

def update_student_records():
    SECRETS_FILE = 'data/VivaManagementSystem-f7cde54a5c9e.json'
    STUDENTS_FILEURL = "https://docs.google.com/spreadsheets/d/1FG3kkhmmZDooNyqCbNyRFHeTP0xYD1RqUssXFN_u9NU/edit#gid=1592165263"
    ''' Extracts all the values from the first sheet of the given URL and
     returns a ListOfList with every value as a string '''
    SCOPE = ['https://spreadsheets.google.com/feeds']
    JSON_KEY = json.load(open(SECRETS_FILE))
    credentials = SignedJwtAssertionCredentials(JSON_KEY['client_email'], \
                                                JSON_KEY['private_key'], SCOPE)
    gc = gspread.authorize(credentials)
    # Open up the workbook based on the spreadsheet name
    workbook = gc.open_by_url(STUDENTS_FILEURL)
    # Get the first sheet
    sheet = workbook.sheet1
    # Extract all data into a dataframe
    student_data = pd.DataFrame(sheet.get_all_records())
    num_db_records = Student.objects.all().count()
    course_details = list(Course.objects.all().values('course_id', 'course_name'))
    course_dict = dict(zip([str(x['course_name']) for x in course_details], [int(x['course_id']) for x in course_details]))
    semester = {'VII' : 7, 'IV' : 4,'X' : 10}
    try:
        # Append rows to the Database
        for index, row in student_data.loc[num_db_records:].iterrows():
            model = Student()
            model.roll_no = row['Roll Number']
            model.course_id = course_dict[row['MSc Programme']]
            model.semester = semester[row['Semester']]
            model.name = row['Name (as per college record)']
            model.email_id = row['Your E-Mail ID']
            model.phone_number = row['Mobile Number']
            model.project_category = row['Project Category']
            model.organization_name = row['Name of the Organization']
            model.postal_address = row['Short URL for Google Map / Location of the Organization']
            model.address_short_url = row['Full Postal Address of the Organization']
            model.mentor_name = row['Name of the Mentor']
            model.mentor_designation = row["Mentor's Designation / Team / BU name"]
            model.mentor_email_id = row['Email of the Mentor']
            model.domain_key_word = row["Project's Domain Key words"]
            model.project_title = row['Tentative Project Title']
            model.join_date = row['Joined Date']
            model.save()
    except IndexError:
        pass
