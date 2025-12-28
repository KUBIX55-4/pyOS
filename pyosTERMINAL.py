print ("pyos: os made in python" )
print ("instaling")
import time
import os
print("seting up")
os.chdir("C:/")
os.chdir("pyOS")
uptime = False
start_time = time.time()
if os.path.exists("sysinfo/name.status"):
    with open('sysinfo/name.status', 'r') as f:
        name = f.read()
else:
    name = input("name: ") 
    with open('sysinfo/name.status', 'w') as f:
        f.write(name)
if os.path.exists("sysinfo/password.status"):
    with open('sysinfo/password.status', 'r') as f:
        rpass = f.read()
    loginscr = True
    while loginscr:
        password = input("password: ")
        if password == rpass:
            loginscr = False
        else:
            print("incorect password try again")
else:
    password = input("password: ") 
    with open('sysinfo/password.status', 'w') as f:
        f.write(password)
while True:
   comand = input("pyos::"+name+">")
   if comand=="infofetch":
      print(r"             ___  ___   ver: pyOS v0.0.6 saveinsafe")
      print(r"  _ __ _  _ / _ \/ __|  user: "+name)
      print(r" | '_ \ || | (_) \__ \ ")
      print(r" | .__/\_, |\___/|___/ ")
      print(r" |_|   |__/            ")
   elif comand=="shutdown":
      exit() 
   elif comand=="help":
      print("commands:")
      print("infofetch -shows pyOS version")
      print("shutdown -shutsdown pyOS")
      print("echo -echos what u sais")
      print("clear -clears scren")
      print("int -instals command")
      print("dir -shows all files in directory")
      print("cd -opens directory")
      print("sd -shows what directory you are in")
   elif comand.startswith("echo "):
      print(comand[5:])
   elif comand=="clear":
      os.system('cls')
   elif comand.startswith("int "):
      atint = comand[4:]
      if atint == "uptime":
         uptime = True
   elif comand == "uptime" and uptime == True:
      now = time.time()
      diff = int(now - start_time)
      days = diff // 86400
      diff %= 86400
      hours = diff // 3600
      diff %= 3600
      minutes = diff // 60
      seconds = diff % 60
      print(f"uptime: {days}d {hours}h {minutes}m {seconds}s")
   elif comand == "dir":
      os.system('dir')
   elif comand.startswith("cd"):
      dirtgo = (r"/"+comand[3:])
      os.chdir(dirtgo)
   elif comand.startswith("sd"):
      print(os.getcwd())  
   elif comand.startswith("filenew"):
      fileXD = (comand[7:])
      try:
           with open(fileXD, 'x', encoding='utf-8') as f:
               print("file got created sucesfuly")
      except FileExistsError:
           print("ERROR: FILE EXIST")
   elif comand.startswith("fileshow"):
      fileXD = (comand[8:])
      try:
          with open(fileXD, 'r', encoding='utf-8') as file:
              zawartosc = file.read()
              print(zawartosc)
      except FileNotFoundError:
          print("ERROR: FILE NOT FOUND")
   elif comand.startswith("filedel"):
      fileXD = (comand[8:])
      try:
          os.remove(fileXD)
          print("file got deleted sucesfuly")
      except FileNotFoundError:
          print("ERROR: FILE NOT FOUND")
   else:
      print("no command: "+comand+" found")
