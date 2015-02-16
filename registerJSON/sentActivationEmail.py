#
import smtplib  
import UsernameAndPassword

def sendActivationUsingMandrill(recipient, message):
    """
    Takes in a loginUsername and loginPassword (used to login into Gmail SMTP
    Also takes in a recipient (to send notification to) and a message
    """

    if recipient == None or recipient == '' or '@' not in recipient or '.' not in recipient:
        raise AssertionError("Recipient email address it not valid")

    sender = 'notify@coinsniff.com'
    receivers = [recipient]

    message = 'From:'+sender+'\r\nTo:'+recipient+'\r\nSubject: CoinSniff Activation \n\n' + message


    try:
       smtpObj = smtplib.SMTP('smtp.mandrillapp.com:587')
       smtpObj.starttls()
       smtpObj.login(UsernameAndPassword.mandrillUsername, UsernameAndPassword.mandrillPassword)
       smtpObj.sendmail(sender, receivers, message)
    except smtplib.SMTPException:
       raise smtplib.SMTPException("Cannot connected to smtp")


def sendActivationEmail(recipient, activationID):
    message = "Hello,\nPlease confirm your email by clicking this link.\nhttp://coinsniff.com/activate/"+str(activationID)
    sendActivationUsingMandrill(recipient, message)
