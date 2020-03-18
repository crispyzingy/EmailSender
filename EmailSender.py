#!python3
# Enter your email-id and password, also insert 'from' and 'to' addresses and your message in the below code

import smtplib

conn = smtplib.SMTP(
    "smtp.gmail.com", 587
)  # smtp server: domain name of email server, port number

print(conn.ehlo())  # starts the connection, 250 means success

print(conn.starttls())  # starts tls connection to secure password

print(conn.login("username@gmail.com", "password"))  # email-id, password

"""from address, to address, body.
1st \n ends the subject, 2nd \n ends the header
blank dictionary {}: success"""
print(
    conn.sendmail(
        "username@gmail.com",
        "username@gmail.com",
        "Subject: So long...\n\nDear Arbaaz,\nSo long, and thanks for all the fish.\n\n-Arbaaz",
    )
)

print(conn.quit())
