# -*- coding: utf-8 -*-

import random

banner1 = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdyyo///+symNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmysossydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMmy+////::::::::/odMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/        `:dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNds++++///:::::::::::omMMMMMMMMMMMMMMMMMMMMMMMMMMMs`            oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNh+++///:::::::::::::::/dMMMMMMMMMMMMMMMMMMMMMMMMM+               oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNy//////:/:::::::::::::::/dMMMMMMMMMMMMMMMMMMMMMMMo                 mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMd++++/////::::::::::::::::/mMMMMMMMMMMMMMMMMMMMMMh                  oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMN+///////:::::::::::::::::::yNMMMMMMMMMMMMMMMMMMMM:                  .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMd++++++///:+ooooo+o:::+++++/+mMMMMMMMMMMMMMMMMMMMM`                   mMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMm++++++//://+++s/o:::/+/o:/+/mMMMMMMMMMMMMMMMMMMMm                    hMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMmss+////::+/.``--o::o+:`../+:mMMMMMMMMMMMMMMMMMMMd           OK       hMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMhsooy/////////////:::y://///::dMMMMMMMMMMMMMMMMMMMh                    dMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMsyoh+///////:::::::::+/:::::::dMMMMMMMMMMMMMMMMMMM+                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMy/oy+///////::::::::::s:::::::dMMMMMMMMMMMMMMMMMMMy.                  -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMmohsy///::::::::::::::/::::::/mMMMMMMMMMMMMMMMMMMMMy                  oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMmsoo+///////::::::::::::::::oNMMMMMMMMMMMMMMMMMMMMN`                 mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNmdm+/+/////::::::++/::::::yMMMMMMMMMMMMMMMMMMMMMM/                /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMd+++///:::::::::::::::yNMMMMMMMMMMMMMMMMMMMMMMy               `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMd+/////:::::::::::::sNMMMMMMMMMMMMMMMMMMMMMMMN.             `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmy++//:::::::::::+hNMMMMMMMMMMMMMMMMMMMMMMMMMm+.         .+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNyoo+//::::::/ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho/---/+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNyoosssoo+++++mNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMhys+///::::::::y:oh+yMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNdydoss/:::::::::::h:.-o-y+hs/yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMdyyo//hh:ys/::::::::::+ho..sdmhy::+ydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMhosso+omdmm/-y/+++/:///+o+--o:-dmNNm:.:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNh+//::/mNMNNo-y.``.-+ddhd+``.:y++sso++o++NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNo+oso+/:osys+oso:...+doo/h-oo+:::////::::dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMdd+++////+y++////:/++/hy/o/oyy::::::::::o::oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMyyo/////:::h+y//:::::::dsosyo-h:::::::::os+:/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMm/d+++//::::sds//:::::::y--md/`h-::::::::dy:::mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMN+/d++++//:::sdd++/::::::s:.md/`y::::::::/h::::oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMdoomssssoo+++hdsooooo++++ho/mds/doooooo++sh++ooomMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""

banner2 = """
    ██████  ▄▄▄       ██▓▄▄▄█████▓ ▄▄▄       ███▄ ▄███▓ ▄▄▄      
  ▒██    ▒ ▒████▄    ▓██▒▓  ██▒ ▓▒▒████▄    ▓██▒▀█▀ ██▒▒████▄    
  ░ ▓██▄   ▒██  ▀█▄  ▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄  
    ▒   ██▒░██▄▄▄▄██ ░██░░ ▓██▓ ░ ░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██ 
  ▒██████▒▒ ▓█   ▓██▒░██░  ▒██▒ ░  ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒
  ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░▓    ▒ ░░    ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░
  ░ ░▒  ░ ░  ▒   ▒▒ ░ ▒ ░    ░      ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░
  ░  ░  ░    ░   ▒    ▒ ░  ░        ░   ▒   ░      ░     ░   ▒   
        ░        ░  ░ ░                 ░  ░       ░         ░   
"""

banner3 = """
    _____  ____  ____  ______   ____  ___ ___   ____ 
   / ___/ /    ||    ||      | /    ||   |   | /    |
  (   \_ |  o  | |  | |      ||  o  || _   _ ||  o  |
   \__  ||     | |  | |_|  |_||     ||  \_/  ||     |
   /  \ ||  _  | |  |   |  |  |  _  ||   |   ||  _  |
   \    ||  |  | |  |   |  |  |  |  ||   |   ||  |  |
    \___||__|__||____|  |__|  |__|__||___|___||__|__|
                                                     
"""

banner4 = """
                                            ,----,                                             
                                          ,/   .`|                       ____                  
    .--.--.      ,---,         ,---,    ,`   .'  : ,---,               ,'  , `.   ,---,        
   /  /    '.   '  .' \     ,`--.' |  ;    ;     /'  .' \           ,-+-,.' _ |  '  .' \       
  |  :  /`. /  /  ;    '.   |   :  :.'___,/    ,'/  ;    '.      ,-+-. ;   , || /  ;    '.     
  ;  |  |--`  :  :       \  :   |  '|    :     |:  :       \    ,--.'|'   |  ;|:  :       \    
  |  :  ;_    :  |   /\   \ |   :  |;    |.';  ;:  |   /\   \  |   |  ,', |  '::  |   /\   \   
   \  \    `. |  :  ' ;.   :'   '  ;`----'  |  ||  :  ' ;.   : |   | /  | |  |||  :  ' ;.   :  
    `----.   \|  |  ;/  \   \   |  |    '   :  ;|  |  ;/  \   \'   | :  | :  |,|  |  ;/  \   \ 
    __ \  \  |'  :  | \  \ ,'   :  ;    |   |  ''  :  | \  \ ,';   . |  ; |--' '  :  | \  \ ,' 
   /  /`--'  /|  |  '  '--' |   |  '    '   :  ||  |  '  '--'  |   : |  | ,    |  |  '  '--'   
  '--'.     / |  :  :       '   :  |    ;   |.' |  :  :        |   : '  |/     |  :  :         
    `--'---'  |  | ,'       ;   |.'     '---'   |  | ,'        ;   | |`-'      |  | ,'         
              `--''         '---'               `--''          |   ;/          `--''           
                                                               '---'                           
                                                                                               
"""

banner5 = """
	        _  _  _  _          _        _  _  _  _  _  _  _  _   _        _           _        _          
      _(_)(_)(_)(_)_      _(_)_     (_)(_)(_)(_)(_)(_)(_)(_)_(_)_     (_) _     _ (_)     _(_)_        
     (_)          (_)   _(_) (_)_      (_)         (_)    _(_) (_)_   (_)(_)   (_)(_)   _(_) (_)_      
     (_)_  _  _  _    _(_)     (_)_    (_)         (_)  _(_)     (_)_ (_) (_)_(_) (_) _(_)     (_)_    
       (_)(_)(_)(_)_ (_) _  _  _ (_)   (_)         (_) (_) _  _  _ (_)(_)   (_)   (_)(_) _  _  _ (_)   
      _           (_)(_)(_)(_)(_)(_)   (_)         (_) (_)(_)(_)(_)(_)(_)         (_)(_)(_)(_)(_)(_)   
     (_)_  _  _  _(_)(_)         (_) _ (_) _       (_) (_)         (_)(_)         (_)(_)         (_)   
       (_)(_)(_)(_)  (_)         (_)(_)(_)(_)      (_) (_)         (_)(_)         (_)(_)         (_)   
                                                                                                       
                                                                                                       
"""

banner6 = """
       _____        _____        _____         _____        _____         _____        _____     
    __|___  |__  __|_    |__  __|_    |__  ___|__   |__  __|_    |__  ___|    _|__  __|_    |__  
   |   ___|    ||    \      ||    |      ||_    _|     ||    \      ||    \  /  | ||    \      | 
    `-.`-.     ||     \     ||    |      | |    |      ||     \     ||     \/   | ||     \     | 
   |______|  __||__|\__\  __||____|    __| |____|    __||__|\__\  __||__/\__/|__|_||__|\__\  __| 
      |_____|      |_____|      |_____|       |_____|      |_____|       |_____|      |_____|    
                                                                                                 

"""

banner7 = """
                                                                           
     _|_|_|    _|_|    _|_|_|  _|_|_|_|_|    _|_|    _|      _|    _|_|    
   _|        _|    _|    _|        _|      _|    _|  _|_|  _|_|  _|    _|  
     _|_|    _|_|_|_|    _|        _|      _|_|_|_|  _|  _|  _|  _|_|_|_|  
         _|  _|    _|    _|        _|      _|    _|  _|      _|  _|    _|  
   _|_|_|    _|    _|  _|_|_|      _|      _|    _|  _|      _|  _|    _|  
                                                                           

"""
def printBanners():
	#return	banner2
	#just for multiple banners
	banners = [banner1, banner2, banner3, banner4, banner5, banner6, banner7]
	return random.choice(banners)
