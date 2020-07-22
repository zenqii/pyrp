
#      Copyright (c) 2020, Zenqi & qwertyquerty
# Please note that I do not own the pyprense module
# For more information about the module, kindly visit the docs:
# https://qwertyquerty.github.io/pypresence/html/index.html



from src import Presence
import time, sys, os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0 just in case

def connectRP4():

    RPC = Presence(client_id=clientid)
    try:
        RPC.connect()
    except Exception as e:
        print(e)
        print("Cannot connect through the discord, is the id is correct or is discord running?")

    try:
        RPC.update(
                state=state, details=detail,
                start=start, end=end,
                large_image=largeimg,large_text=largetxt,
                small_image=smallimg,small_text=smalltxt,

        )    
        print(title)
        print("-"*50)
        print("Detail\n"+"-"*50+"\nState: %s\nDetails: %s\nStartTimeStamp: %s\nEndTimeStamp: %s\n"%(state, detail, start, end))
        print("-"*50)
        print("Images")
        print("-"*50)
        print("LargeImage: %s\nSmallImage: %s\nLargeText: %s\nSmallText: %s"%(largeimg, smallimg, largetxt, smalltxt))
        print("-"*50)
        print("Party")
        print("-"*50)
        print("Party ID: %s\nJoin Key: %s\nSpectate Key: %s"%(partyid,joins,spectates))
        print("\nClientID: "+clientid)
        print("-"*50)
        print("\nCopyright (c) 2020, Zenqi & qwertyquerty. All rights reserved")
            
        
    except Exception as e:
        print(e)
        print("An error occur please contact Zenqi#7610 to solve the problem or try to solve by your own")
        input("")
        sys.exit()
def connectRP3():
    
    RPC = Presence(client_id=clientid)
    try:
        RPC.connect()
    except Exception as e:
        print(e)
        print("Cannot connect through the discord, is the id is correct or is discord running?")

    try:
        RPC.update(
                state=state, details=detail
        )

        print(title)
        print("-"*50)
        print("Detail\n"+"-"*50+"\nState: %s\nDetails: %s\nStartTimeStamp: %s\nEndTimeStamp: %s\n"%(state, detail, start, end))
        print("-"*50)
        print("Images")
        print("-"*50)
        print("LargeImage: %s\nSmallImage: %s\nLargeText: %s\nSmallText: %s"%(largeimg, smallimg, largetxt, smalltxt))
        print("\nClientID: "+clientid)
        print("-"*50)
        print("\nCopyright (c) 2020, Zenqi & qwertyquerty. All rights reserved")

            
    except Exception as e:
        print(e)
        print("An error occur please contact Zenqi#7610 to solve the problem or try to solve by your own")
        input("")
        sys.exit()
def connectRP2():
    
    RPC = Presence(client_id=clientid)
    try:
        RPC.connect()
    except Exception as e:
        print(e)
        print("Cannot connect through the discord, is the id is correct or is discord running?")

    try:
        RPC.update(
                state=state, details=detail,
                start=start,
                end=end
        )


        print(title)
        print("-"*50)
        print("Detail\n"+"-"*50+"\nState: %s\nDetails: %s\nStartTimeStamp: %s\nEndTimeStamp: %s\n"%(state, detail, start, end))
        print("-"*50)
        print("Images")
        print("-"*50)
        print("LargeImage: %s\nSmallImage: %s\nLargeText: %s\nSmallText: %s"%(largeimg, smallimg, largetxt, smalltxt))
        print("\nClientID: "+clientid)
        print("-"*50)
        print("\nCopyright (c) 2020, Zenqi & qwertyquerty. All rights reserved")
            
            
    except Exception as e:
        print(e)
        print("An error occur please contact Zenqi#7610 to solve the problem or try to solve by your own")
        input("")
        sys.exit()

def connectRP():

    RPC = Presence(client_id=clientid)
    try:
        RPC.connect()
    except Exception as e:
        print(e)
        print("Cannot connect through the discord, is the id is correct or is discord running?")

    try:
        RPC.update(
                state=state, details=detail,
                start=start, end=end,
                large_image=largeimg,large_text=largetxt,
                small_image=smallimg,small_text=smalltxt,
                party_id=partyid, 
                join=joins, spectate=spectates
        )    
        print(title)
        print("-"*50)
        print("Detail\n"+"-"*50+"\nState: %s\nDetails: %s\nStartTimeStamp: %s\nEndTimeStamp: %s\n"%(state, detail, start, end))
        print("-"*50)
        print("Images")
        print("-"*50)
        print("LargeImage: %s\nSmallImage: %s\nLargeText: %s\nSmallText: %s"%(largeimg, smallimg, largetxt, smalltxt))
        print("-"*50)
        print("Party")
        print("-"*50)
        print("Party ID: %s\nJoin Key: %s\nSpectate Key: %s"%(partyid,joins,spectates))
        print("\nClientID: "+clientid)
        print("-"*50)
        print("\nCopyright (c) 2020, Zenqi & qwertyquerty. All rights reserved")
            
        
    except Exception as e:
        print(e)
        print("An error occur please contact Zenqi#7610 to solve the problem or try to solve by your own")
        input("")
        sys.exit()

config = ConfigParser(allow_no_value=True)
config.read('settings.ini') # reads the data from our settings

# After reading, we gonna get the user input

global clientid, state, detail, start, end
global largeimg, smallimg, largetxt, smalltxt

clientid = config['INFO']['client_id']

state = config['STATE']['state']
detail = config['STATE']['details']
start = config['STATE']['starttimestamp']
end = config['STATE']['endtimestamp']

largeimg = config['IMAGES']['large_image']
smallimg = config['IMAGES']['small_image']
largetxt = config['IMAGES']['large_text']
smalltxt = config['IMAGES']['small_text']

partyid = config['PARTY']['party_id']
joins = config['PARTY']['join']
spectates = config['PARTY']['spectate']

pt = config.get("PARTY", "party_id")
j = config.get('PARTY', 'join')
ss = config.get('PARTY', 'spectate')


l = config.get('IMAGES', 'large_image')
s = config.get('IMAGES', 'small_image')
st = config.get('STATE', 'starttimestamp')
en = config.get('STATE', 'endtimestamp')

global title
title = """
                                    
@@@@@@@  @@@ @@@ @@@@@@@  @@@@@@@  
@@!  @@@ @@! !@@ @@!  @@@ @@!  @@@ 
@!@@!@!   !@!@!  @!@!!@!  @!@@!@!  
!!:        !!:   !!: :!!  !!:      
:         .:     :   : :  :  
    """

os.system('title PY-RP')

if st == "" or en == "":
    connectRP3()
elif s == "" or l == "":
    connectRP2()
elif pt == ""  or j == "" or ss == "":
    try:
        connectRP4()
    except Exception:
        connectRP2()
else:
    connectRP()
    




