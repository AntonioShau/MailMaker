#####################################################################
#Crear direcciones de correo electronico a partir de una lista con  #
#nombres y apellidos de distintos usuarios, se tomaran las tres     #
#primeras letras del nombre, las 3 primeras letras del apellido     #
#y se le agregara el "@" con el dominio "dominio".                  #
#####################################################################

namesList = [
    "Enrique Perez",
    "Fabiola Rodriguez",
    "Francisco Diaz",
    "Luis Martinez",
    "Monica Duarte",
    "Carolina Sanches",
    "Miguel Velez",
    "Jesus Ramos",
    "Abelardo Orta",
    "Alfredo Romo",
    "Teresa Medina"
]

dominio = "@dominio.com"

def mailMaker(names):
    mailList = []
    for name in names:
        mail = (((name.split()[0][:3])) + (name.split()[1][:3]) + dominio)
        mailList.append(mail.lower())
    return mailList

MailList = mailMaker(namesList)

userMail = {}
for k, v in zip(namesList, MailList):
    userMail[k] = v

for i in userMail:
    print(i, "->", userMail[i])