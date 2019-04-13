#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import smtplib
import commands, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

USER = "user"
PASS = "password"
FROM = "name@email.com"
TO = sys.argv[2]
subject = 'PASSWD Has Been Changed!'
texto = commands.getoutput('cat %s' % sys.argv[1])
texto += "\n\n Checking the integrity of /etc/passwd file.\n\n MindSecurity@2018"

msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = subject
msg.attach(MIMEText(texto))

try:
    gm = smtplib.SMTP('smtp.gmail.com:587')
    gm.ehlo()
    gm.starttls()
    gm.login(USER, PASS)
    gm.sendmail(FROM, TO, msg.as_string())
    gm.close()
except Exception, erro:
    errorMsg = "The email has not been sent.\n Error: %s" % erro
    print '%s' % errorMsg
else:
    print 'E-mail sent.'
