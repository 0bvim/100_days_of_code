import platform
import time
import os

def cls():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

logo = r"""
  ________                              _________ 
 /  _____/ __ __   ____   ______ ______ \_____   \
/   \  ___|  |  \_/ __ \ /  ___//  ___/    /   __/
\    \_\  \  |  /\  ___/ \___ \ \___ \    |   |   
 \______  /____/  \___  >____  >____  >   |___|   
        \/            \/     \/     \/    <___>   
"""

big1 = r"""
 /$$     /$$                        /$$      /$$ /$$          
|  $$   /$$/                       | $$  /$ | $$|__/          
 \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$ 
  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$
   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$
    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$
    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$
    |__/  \______/  \______/       |__/     \__/|__/|__/  |__/
"""

big2 = r"""
$$\     $$\                         $$\      $$\ $$\           
\$$\   $$  |                        $$ | $\  $$ |\__|          
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ |$$\ $$$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$ |$$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |$$ |  $$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |$$ |  $$ |
    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |$$ |$$ |  $$ |
    \__|   \______/  \______/       \__/     \__|\__|\__|  \__|
"""

big3 = r"""
 __      __                          __       __  __           
|  \    /  \                        |  \  _  |  \|  \          
 \$$\  /  $$______   __    __       | $$ / \ | $$ \$$ _______  
  \$$\/  $$/      \ |  \  |  \      | $$/  $\| $$|  \|       \ 
   \$$  $$|  $$$$$$\| $$  | $$      | $$  $$$\ $$| $$| $$$$$$$\
    \$$$$ | $$  | $$| $$  | $$      | $$ $$\$$\$$| $$| $$  | $$
    | $$  | $$__/ $$| $$__/ $$      | $$$$  \$$$$| $$| $$  | $$
    | $$   \$$    $$ \$$    $$      | $$$    \$$$| $$| $$  | $$
     \$$    \$$$$$$   \$$$$$$        \$$      \$$ \$$ \$$   \$$
"""

big4 = r"""
 __      __                         __       __  __           
/  \    /  |                       /  |  _  /  |/  |          
$$  \  /$$/______   __    __       $$ | / \ $$ |$$/  _______  
 $$  \/$$//      \ /  |  /  |      $$ |/$  \$$ |/  |/       \ 
  $$  $$//$$$$$$  |$$ |  $$ |      $$ /$$$  $$ |$$ |$$$$$$$  |
   $$$$/ $$ |  $$ |$$ |  $$ |      $$ $$/$$ $$ |$$ |$$ |  $$ |
    $$ | $$ \__$$ |$$ \__$$ |      $$$$/  $$$$ |$$ |$$ |  $$ |
    $$ | $$    $$/ $$    $$/       $$$/    $$$ |$$ |$$ |  $$ |
    $$/   $$$$$$/   $$$$$$/        $$/      $$/ $$/ $$/   $$/ 
"""

def big_seq():
	cls()
	print(big1)
	time.sleep(0.3)
	cls()
	print(big2)
	time.sleep(0.3)
	cls()
	print(big4)
	time.sleep(0.3)
	cls()
	print(big3)
