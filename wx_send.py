import sys, os, getopt, time, datetime
from wxpy import *


def filesExist(fileList):
    for i, aFile in enumerate(fileList):
        if not os.path.exists(aFile):
            print("warning: the {}th file, {}, doesn't exist.".format(i + 1, aFile))
            return False
    return True

def readFile(filename):
    infoList = []
    with open(filename, "rb") as f:
        for line in f.readlines():
            infoList.append(line.strip())
    return infoList

def main(argv):
    now = datetime.datetime.now()
    dayDelta = datetime.timedelta(days = 0)
    h = 0
    m = 16
    fileList = []
    messageList = []
    user = ""
    group = ""
    try:
        opts, args = getopt.getopt(argv,"d:h:m:f:t:u:g:")
    except getopt.GetoptError:
        print ('wx_send.py -d <today(0) or tomorrow(1)> -h <hour 0-24> -m <minutes 0-59> -f <a file list> -t <a message list> -u <user name> -g <group name>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '--help':
            print ('wx_send.py -d <today(0) or tomorrow(1)> -h <hour 0-24> -m <minutes 0-59> -f <a file list> -t <a message list> -u <user name> -g <group name>')
            sys.exit()
        elif opt == "-d":
            dayDelta = datetime.timedelta(days = int(arg))
        elif opt == "-h":
            h = int(arg)
        elif opt == "-m":
            m = int(arg)
        elif opt == "-f":
            fileList = readFile(arg)
            if not filesExist(fileList):
                sys.exit()
        elif opt == "-t":
            messageList = readFile(arg)
        elif opt == "-u":
            user = arg
        elif opt == "-g":
            group = arg
    if user == "" and group == "":
        print("please specify a user or group")
        sys.exit()
    bot = Bot()
    if user != "":
        userList = bot.friends().search(user)
        try:
            userObj = ensure_one(userList)            
        except Exception as e:
            print(e)
            sys.exit(2)
    if group != "":
        groupList = bot.groups().search(group)
        try:
            groupObj = ensure_one(groupList)
        except Exception as e:
            print(e)
            sys.exit(2)        
    aTime = now.replace(hour = h, minute=m)
    aTime = aTime + dayDelta
    while datetime.datetime.now() < aTime:
        time.sleep(20)
    for aFile in fileList:
        try:
            if user != "":
                userObj.send_file(aFile.decode("utf-8"))
            if group != "":
                groupObj.send_file(aFile.decode("utf-8"))
        except Exception as e:
            print(e)
            print(aFile)
    for aMessage in messageList:
        try:
            if user != "":
                userObj.send(aMessage.decode("utf-8"))
            if group != "":
                groupObj.send(aMessage.decode("utf-8"))
        except Exception as e:
            print(e)
            print(aMessage)

if __name__ == "__main__":
    main(sys.argv[1:])