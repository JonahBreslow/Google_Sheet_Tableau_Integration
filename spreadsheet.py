import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Test-9176086fefeb.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Test').sheet1

records = sheet.get_all_records()
print(records)
