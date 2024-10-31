
import docx2txt
import smtplib
import pandas as pd
import os
print('login to your email')
try:
    sender = input('Enter email address\n')
    sender_password = input('Enter password\n')
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.ehlo()
    server.login(sender, sender_password)
    print('logged in,succesfully')
except:
    print('wrong emailid or password')
    print('try again')
# changing directory to where excel file is located
os.chdir('C:/Users/Deepu/Desktop/EMAILIDS')
print('directory changed')
# reading excel file
try:
    email_list = pd.read_excel(input('Enter excel fine name\n')+'.xlsx')
    print('data read from excel spreadsheet')
except:
    print('NO such file')
    exit()
    
emails = email_list['email']
print('total no. of emails in a excel sheet are')
print(len(emails)-1)
# reading a message
msg = docx2txt.process('surfexpo.docx')
# reading subject
subject = input("Enter subject\n")
body = "Subject:{}\n\n{}".format(subject, msg)
print(body)
count = 0
sent = 0
for email in emails:
    count = count+1
    print('emails checked', +count)
    import re
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        if sent < 1900:
            server.sendmail(sender, email, body.encode('utf-8'))
            print("messages delivered")
            sent = sent+1
            print("emails sent", +sent)

    else:
        print("invalid emails")
print('total number of valid emails sent=', +count)
server.quit()
