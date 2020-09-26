import re

email_collector = ''' An email address is simply an address that can send and receive
 email messages in electronic mode on a particular network.
E-mail should be in the form of username@domain.com
prince@yahoo.in
An address consists of two parts.
vic@gmail.com
The part that comes before the @ symbol is called as
 no_work@gmail.com
 local-part which is often username
 ramesh.kumar123@gmail.com
 of the recipient and the part after the @ symbol is a domain 
 name that represents the administrative realm of the mailbox.
Here are the best examples of an email id:
nick@gmail.com



'''
j = 0
collect = re.findall(r"[a-zA-Z0-9._+%]+@+[a-zA-Z0-9._+%]+[.]+[A-Za-z.0-9]+",email_collector)
with open("email.txt","w") as f:
    for i in collect:
        f.write(f"Email is {i}\n")
        j += 1
        print(f"Emails are {i}\n")
    print(f"Total mails are {j}")


