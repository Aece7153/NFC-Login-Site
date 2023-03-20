def login(username,password):
    username = username
    f = open('Users/Usernames_Passwords', "r")
    for x in f.readlines():
        fields = x.split(";")
        Name = fields[0]
        Hash = fields[1]
        if username == Name and password.encode('utf-8'):
            return "True"
        else:
            return "False"