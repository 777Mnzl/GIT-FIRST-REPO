import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('#email you are gonna send','#password here')
subject='Testing a mail sent through python'
body = 'this is a body sent fromm the python code in VSCODE'
message = 'subject:{}\n\n{}'.format(subject,body)
listaddress = ['#emails you are going to send to']
ob.sendmail('#email you sent from',listaddress, message)
print('send mail')
ob.quit()

