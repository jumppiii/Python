import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Barrel Duty')
label1.config(font=('helvetica', 14))
canvas1.create_window(205, 25, window=label1)

label2 = tk.Label(root, text='Monday')
label2.config(font=('helvetica', 10))
canvas1.create_window(205, 62, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(205, 80, window=entry1)

label3 = tk.Label(root, text='Tuesday')
label3.config(font=('helvetica', 10))
canvas1.create_window(205, 102, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(205, 120, window=entry2)

label4 = tk.Label(root, text='Wednesday')
label4.config(font=('helvetica', 10))
canvas1.create_window(205, 142, window=label4)

entry3 = tk.Entry(root)
canvas1.create_window(205, 160, window=entry3)

label5 = tk.Label(root, text='Thursday')
label5.config(font=('helvetica', 10))
canvas1.create_window(205, 182, window=label5)

entry4 = tk.Entry(root)
canvas1.create_window(205, 200, window=entry4)

label6 = tk.Label(root, text='Friday')
label6.config(font=('helvetica', 10))
canvas1.create_window(205, 222, window=label6)

entry5 = tk.Entry(root)
canvas1.create_window(205, 240, window=entry5)

label7 = tk.Label(root, text='Extra notes')
label7.config(font=('helvetica', 10))
canvas1.create_window(205, 262, window=label7)

entry6 = tk.Entry(root)
canvas1.create_window(205, 280, window=entry6)


def send_email():
    import smtplib
    import datetime
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    dt = datetime.datetime.now()
    week_number = str(dt.strftime("%W"))

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()

    msg = MIMEMultipart()
    msg['From'] = 'BarrelDuty@dnb.no'
    recipients = ['dominic.james.cleary.de.vibe@dnb.no', 'terje.olsen@dnb.no']
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = 'Barrel Duty week ' + week_number
    message = 'Barrel Duty' \
              '\n\nMonday: ' + e1 + '\nTuesday: ' + e2 + "\nWednesday: " + e3 + "\nThursday: " + e4 + "\nFriday: " + e5
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.dnb.no', 25)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()

    mailserver.sendmail('BarrelDuty@dnb.no', recipients, msg.as_string())

    mailserver.quit()


button1 = tk.Button(text='Send barrel duty list', command=send_email, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 320, window=button1)

root.mainloop()
