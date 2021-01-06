import smtplib
import creds

sender_email= "sender@gmail.com"
receiver_email = "receiver@gmail.com"

password = "Password"

message =" This is a test email sent with python"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(sender_email, password)
print('Login succesfull')
server.sendmail(sender_email, receiver_email, message)
print('Your email has been sent to', receiver_email)
    
