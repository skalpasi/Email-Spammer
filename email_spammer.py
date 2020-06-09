import smtplib
import getpass

def spam(to, content, mail, password, count):
    server = smtplib.SMTP('smtp.gmail.com',  587)
    server.ehlo()
    server.starttls()
    server.login(mail,password)
    for i in range(int(count)):
        server.sendmail(mail, to, content)
        print('Sent '+str(i+1),'out of '+str(count))
    server.close()
if __name__ == '__main__':
    try:
        print('\nPYTHON E-MAIL SPAMMER!')
        print('..............................')
        print('Login to your gmail account')
        print('..............................')
        mail = input("Email: ")
        password = getpass.getpass(prompt='Password: ')
        try:
            print('\n..............................')
            print('Succesfully logged in!')
        except Exception as e:
            print('..............................')
            print(e)
            print('Failed to login')
        print('..............................')
        subject = input('Subject: ')
        message = input('Mesage: ')
        content = 'Subject: {}\n\n{}'.format(subject, message)
        to = input('To: ')
        print('\n..............................')
        count = input('Count: ')
        spam(to, content, mail, password, count)
        print('..............................')
        print('Done!')
    except Exception as e:
        print('..............................')
        print(e)
        print('Unable to send the mail')