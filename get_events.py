# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:49:32 2020

@author: Batuhan
"""
import pandas as pd
import time as tm
import sqlite3
import urllib
import os

def get_equipment(equ):
    equipment = []
    if not equ['MainHand'] == None:
        main_hand = equ['MainHand']['Type']
        main_hand_q = equ['MainHand']['Quality']
        main_hand_c = equ['MainHand']['Count']
    else:
        main_hand = 'None'
        main_hand_q = 'None'
        main_hand_c = 'None'
    if not equ['Head'] == None:    
        head = equ['Head']['Type']
        head_q = equ['Head']['Quality']
        head_c = equ['Head']['Count']
    else:
        head   = 'None'
        head_q = 'None'
        head_c = 'None'
    if not equ['Armor'] == None:    
        armor = equ['Armor']['Type']
        armor_q = equ['Armor']['Quality']
        armor_c = equ['Armor']['Count']
    else:
        armor = 'None'
        armor_q = 'None'
        armor_c = 'None'
    if not equ['Shoes'] == None:    
        shoes = equ['Shoes']['Type']
        shoes_q = equ['Shoes']['Quality']
        shoes_c = equ['Shoes']['Count']
    else:
        shoes = 'None'
        shoes_q = 'None'
        shoes_c = 'None'
    if not equ['Bag'] == None:    
        bag = equ['Bag']['Type']
        bag_q = equ['Bag']['Quality']
        bag_c = equ['Bag']['Count']
    else:
        bag = 'None'
        bag_q = 'None'
        bag_c = 'None'
    if not equ['Cape'] == None:    
        cape = equ['Cape']['Type']
        cape_q = equ['Cape']['Quality']
        cape_c = equ['Cape']['Count']
    else:
        cape = 'None'
        cape_q = 'None'
        cape_c = 'None'
    if not equ['Mount'] == None:
        mount = equ['Mount']['Type']
        mount_q = equ['Mount']['Quality']
        mount_c = equ['Mount']['Count']
    else:
        mount = 'None'
        mount_q = 'None'
        mount_c = 'None'
    if not equ['Potion'] == None:
        potions = equ['Potion']['Type']
        potions_q = equ['Potion']['Quality']
        potions_c = equ['Potion']['Count']
    else:
        potions = 'None'
        potions_q = 'None'
        potions_c = 'None'
    if not equ['Food'] == None:    
        food = equ['Food']['Type']
        food_q = equ['Food']['Quality']
        food_c = equ['Food']['Count']
    else:
        food = 'None'
        food_q = 'None'
        food_c = 'None'
    if not equ['OffHand'] == None:
        off_hand = equ['OffHand']['Type']
        off_hand_q = equ['OffHand']['Quality']
        off_hand_c = equ['OffHand']['Count']
    else:
        off_hand = 'None'
        off_hand_q = 'None' 
        off_hand_c = 'None'
    items = {0: main_hand,
            1: off_hand,
            2: head,
            3: armor,
            4: shoes,
            5: bag,
            6: cape,
            7: mount,
            8: food,
            9: potions
            }
    qualitys = {0: main_hand_q,
            1: off_hand_q,
            2: head_q,
            3: armor_q,
            4: shoes_q,
            5: bag_q,
            6: cape_q,
            7: mount_q,
            8: food_q,
            9: potions_q
            }
    count = {0: main_hand_c,
            1: off_hand_c,
            2: head_c,
            3: armor_c,
            4: shoes_c,
            5: bag_c,
            6: cape_c,
            7: mount_c,
            8: food_c,
            9: potions_c
            }
    equipment.append([items,qualitys,count])    
    return equipment

def get_profiles(p):
    profile = []
    if not p['AllianceName'] == 'None':
        AllianceName = '['+p['AllianceName']+']'
    else:
        AllianceName = ''
    if not p['GuildName'] == 'None':
        GuildName = p['GuildName']
    else:
        GuildName = '--'
    if not p['AverageItemPower'] == 'None':
        AverageItemPower = int(p['AverageItemPower'])
    else:
        AverageItemPower = 'None' 
    if not p['Name'] == 'None':
        Name = p['Name']
    else:
        Name = 'None'    
        
    profile.append([AllianceName,GuildName,Name,AverageItemPower])
    return profile

def get_inventory(victim):
    ınventory = []
    for i in range(0,48):
        if not victim['Inventory'][i] == None:
            item = victim['Inventory'][i]['Type']
            item_q = victim['Inventory'][i]['Quality']
            item_c = victim['Inventory'][i]['Count']                      
            ınventory.append([item,item_q,item_c])
        else:
            continue
    return ınventory
def get_participants(p,nop):
    participants = []
    NoP = int(nop)
    for i in range(0,NoP):    
        if not p[i]['Name'] == 'None':
            Nick = p[i]['Name']
        else:
            Nick = 'None' 
        
        if not p[i]['DamageDone'] == 'None': 
            DamageDone = int(p[i]['DamageDone'])
        else:
            DamageDone = 0 
        
        if not p[i]['SupportHealingDone'] == 'None': 
            SupportHealingDone = int(p[i]['SupportHealingDone'])
        else:
            SupportHealingDone = 0
        participants.append([Nick, DamageDone, SupportHealingDone])            
    return participants

def Main_Events():
    url = "https://gameinfo.albiononline.com/api/gameinfo/events" 
    db = sqlite3.connect('KillbotDatabase.sqlite')
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS 'KillBotCheck' (EventID)")
    try:        
        rowdataset = pd.read_json(url)
    except: 
        print('Veriye ulaşamadım')
        return None
    eventsıd = rowdataset.iloc[:,2:3].values
    killers = rowdataset.iloc[:,5:6].values
    victims = rowdataset.iloc[:,6:7].values
    totalkillfame = rowdataset.iloc[:,7:8].values
    numberofparticipants = rowdataset.iloc[:,0:1].values
    participants = rowdataset.iloc[:,9:10].values
    r_data = []
    for i in range(0,20):
        eventID = int(eventsıd[i][0])
        killer = killers[i][0]
        killer_profile = get_profiles(killer)
        victim = victims[i][0]
        victim_profile = get_profiles(victim)
        if killer_profile[0][1] == 'Iron Hand' or victim_profile[0][1] == 'Iron Hand': 
            killer_equipment = get_equipment(killer['Equipment'])
            victim_equipment = get_equipment(victim['Equipment'])
            victim_inventory = get_inventory(victim)
            tkf = int(totalkillfame[i][0])        
            NoP = numberofparticipants[i]
            Party = participants[i][0]
            nop = get_participants(Party,NoP)
            data = (eventID,killer_profile,killer_equipment,victim_profile,victim_equipment,victim_inventory,tkf,nop)
            picker = db.execute("SELECT EventID FROM 'KillBotCheck'")
            kontrol = []
            for row in picker:
                kontrol.append(row[0])
            if eventID in kontrol:
                continue
            else:
                str(eventID)
                imlec.execute("INSERT INTO 'KillBotCheck' VALUES ({})".format(eventID))
                print('Data Saved!')
                r_data.append(data)
    db.commit()
    db.close()
    return  r_data
