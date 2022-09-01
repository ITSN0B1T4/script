import os, sys, time
def ani(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
correctuser = "DEVS"
correctpwd = "COMMUNITY"
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def logo ():
  os.system("clear")
  os.system("""echo '  ░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗░█████╗░██╗░░░██╗
  ██╔══██╗██║░██╔╝╚██╗██╔╝██║░░░██║██╔══██╗██║░░░██║
  ███████║█████═╝░░╚███╔╝░╚██╗░██╔╝███████║██║░░░██║
  ██╔══██║██╔═██╗░░██╔██╗░░╚████╔╝░██╔══██║██║░░░██║
  ██║░░██║██║░╚██╗██╔╝╚██╗░░╚██╔╝░░██║░░██║╚██████╔╝
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░
----------------------------------------------------
  ╔════════════════════════════════════════════════╗
  ║            [✓] GITHUB : ITZAKX21               ║
  ║            [✓] FACEBOOK : AKX.THE.PSYCHO       ║
  ║            [✓] TELEGRAM : AKXVAU               ║
  ║            [✓] INSTAGRAM : AKXVAU              ║
  ║            [✓] EMAIL : ADMIN@ITZAKX.ML         ║
  ╚════════════════════════════════════════════════╝
----------------------------------------------------'|lolcat""")

def login ():
  logo ()
  user = str(input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m ENTER USERNAME :\033[1;34;40m "))
  if user == correctuser:
    pwd = str(input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m ENTER PASSWORD :\033[1;34;40m "))
    if pwd == correctpwd:
      logo ()
    else:
      ani("\n\t\033[1;30;31m</> PLEASE ENTER CORRECT PASSWORD </>")
      time.sleep(2)
      login ()
  else:
    ani("\n\t\033[1;30;31m</> PLEASE ENTER CORRECT USERNAME </>")
    time.sleep(2)
    login ()
 
login ()
