import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "yehor.kosiachkin@gmail.com"
    password = "cewo cpjd vuoa rmqu"
    reciever = "yehor.kosiachkin@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
