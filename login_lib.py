import time
p = {"zac": '5642', "alexa": '2293', "lexi": '9080', "jack": '7684'}
# p1=(username,password)
#global a
#a='false'
def login(username,password):
    #username = input("Enter your username:")
    #password = input("enter password:")
    if (username, password) in p.items():
        #print("Welcome", username)
        #a = 'true'
        return True

    else:

        #print("access denied")
        return False
        login()