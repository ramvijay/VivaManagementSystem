import gspread
import pandas as pd
import json
from oauth2client.client import SignedJwtAssertionCredentials
from VivaManagementSystem.models import Faculty
#-------------------Donot change the code above this line---------------------------------
def update_faculty_records():
    SECRETS_FILE = 'data/VivaManagementSystem-f7cde54a5c9e.json'
    fileURL = "https://docs.google.com/spreadsheets/d/1nlYqgnmxiLfkGiIEyBUZ4IlFOVTrwok4WUMBHFFl84c/edit#gid=1604066109"
    # --------------------Donot change the code below this line-----------------------------------
    ''' Extracts all the values from the first sheet of the given URL and
     returns a ListOfList with every value as a string '''
    SCOPE = ['https://spreadsheets.google.com/feeds']
    json_key = json.load(open(SECRETS_FILE))
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], \
                                                json_key['private_key'], SCOPE)
    gc = gspread.authorize(credentials)
    # Open up the workbook based on the spreadsheet name
    workbook = gc.open_by_url(fileURL)
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