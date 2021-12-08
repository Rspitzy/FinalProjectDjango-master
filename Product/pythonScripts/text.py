#import smtplib
from twilio.rest import Client


### this worked at one point two years ago, decided to switch to twilio as backup because it stopped working
# def text_user(product):
#
#     email = "textfromprogram1234@gmail.com"
#     pas = "Ieatkale88"
#     sms_gateway = '8609935146@messaging.tmomail.com'
#     smtp = "smtp.gmail.com"
#     port = 587
#     server = smtplib.SMTP(smtp,port)
#     server.starttls()
#     server.login(email,pas)
#     body = product
#     server.sendmail(email,sms_gateway,body)
#     server.quit()

def send_text(p_name, price, url, phone):

    # print(p_name + " " + phone)
    # account_sid = 'AC8022637cf613dfdc639b416a968675e6'
    # auth_token = 'ff27caf85a5aea82ccc767d42a49323b'
    # client = Client(account_sid, auth_token)
    #
    text = 'Product: ' + p_name + ' Price: ' + price + ' url: ' + url
    #
    # message = client.messages.create(
    #
    #     body=text,
    #     to='+18609935146'
    #     #to='+1' + phone
    # )
    #
    # print(message.sid)
    account_sid = 'AC8022637cf613dfdc639b416a968675e6'
    auth_token = 'a28f9f4040318f653bbadf303bfe9e4d'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG606481978a26f8d924c9bc597547c16c',
        body=text,
        #to='+18609935146'
        to='+1'+ phone
    )

    print(message.sid)