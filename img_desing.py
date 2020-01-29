# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:41:19 2020

@author: Batuh
"""

from PIL import Image, ImageDraw, ImageFont
import sqlite3
import PIL
# Body Process Area's
killer_area = (10,175,310,488)
victim_area = (310,175,610,488)

# Body İnside Area's
bag_area      = (47,55)
head_area     = (323,75)
cape_area     = (600,55)
main_hand_area= (97,267)
armor_area    = (325,270)
off_hand_area = (556,267)
food_area     = (47,487)
shoes_area    = (325,465)
pot_area      = (600,487)
mount_area    = (324,655)
Body_area     = [main_hand_area, off_hand_area, head_area, armor_area, shoes_area,
            bag_area, cape_area, mount_area, food_area, pot_area]
# Top of image Area's
logo_size     = (100,30)
logo_area     = (650,70,750,100)
sec_logo_area = (650,100,750,130)
logo = "Made by" 
sec_logo = "Heyopa"
dmg = 'Top Five:'

# Killer Name-Guild-Ip Area'
killer_name_area  = (0,50,325,75)
killer_name_size  = (325,25)
killer_guild_area = (0,75,325,100)
killer_ip_area    = (0,150,325,175) 

# Victim Name-Guild-Ip Area's
victim_name_area  = (325, 50, 600,75)
victim_name_size  = (275,25)
victim_guild_area = (325, 75, 600,100)
victim_ip_area    = (325, 150, 600, 175)

# Right Block Area
rblock_size = (190,25)
dmg_size    = (150,25)
dmg_area    = (625,225,775,250)

# Participant's Area's
participant1_area = (610,250,800,275)
participant2_area = (610,275,800,300)
participant3_area = (610,300,800,325)
participant4_area = (610,325,800,350)
participant5_area = (610,350,800,375)
ptcp = [participant1_area, participant2_area, participant3_area, 
        participant4_area, participant5_area]

# Total Fame area
fame_area = (610,400,800,425)
fimg_area = (630,400,655,425)
fdiv_area = (610,425,800,450)

# Stable Image Open
background = Image.open('backscreen.png')
killer = Image.open('gear.png')
victim = Image.open('gear.png')
fame_image = Image.open('fame.png') 

#Process
def text_process(text,size,img,area):
    blank = Image.new('RGBA',(size),(221,188,154))
    font = ImageFont.truetype('arial.ttf',20)
    draw = ImageDraw.Draw(blank)
    w,h = font.getsize(text)
    draw.text(((size[0]-w)/2,(size[1]-h)/2),text,font=font,fill='black')
    img.paste(blank,area)
    return img

def participants_text(text,size,img,area,color):
    blank = Image.new('RGBA',(size),(221,188,154))
    font = ImageFont.truetype('arial.ttf',20)
    draw = ImageDraw.Draw(blank)
    w,h = font.getsize(text)
    draw.text(((size[0]-w)/2,(size[1]-h)/2),text,font=font,fill=color)
    img.paste(blank,area)
    return img

def img_resize(img):
    (width, height) = (300,350)
    img.resize((width, height))
    return img

def img_paste(background,img,area):
    background.paste(img,area)
    return background

def img_open(item,quality):   
    try:
        img = Image.open("./Main/Images/{}{}.png".format(item,quality))
    except:        
            item_url = str("https://gameinfo.albiononline.com/api/gameinfo/items/"+item+".png?count="+str(1)+"&quality="+str(quality))
            file_name = "{}{}".format(item,quality)
            full_path = 'Main/Images/' + file_name +'.png'
            try:
                urllib.request.urlretrieve(item_url, full_path)
                print('Image Saved!')
                img = Image.open("./Main/Images/{}{}.png".format(item,quality))
            except:
                img = Image.open("404.png")
                print('Http Error')
    return img

def get_gear_img(gear):
    item, qualitys, count = gear[0]
    gear_img = Image.open("gear.png")
    size = (300,350)
    if item[0] != "None":  
        main_hand = img_open(item[0],qualitys[0])
        gear_img.paste(main_hand,Body_area[0],main_hand)
    if item[1] != "None":
        off_hand = img_open(item[1],qualitys[1])
        gear_img.paste(off_hand,Body_area[1],off_hand)
    if item[2] != "None":
        head = img_open(item[2],qualitys[2])
        gear_img.paste(head,Body_area[2],head)
    if item[3] != "None":
        armor = img_open(item[3],qualitys[3]) 
        gear_img.paste(armor,Body_area[3],armor)
    if item[4] != "None":
        shoes = img_open(item[4],qualitys[4])   
        gear_img.paste(shoes,Body_area[4],shoes)
    if item[5] != "None":
        bag = img_open(item[5],qualitys[5])   
        gear_img.paste(bag,Body_area[5],bag)
    if item[6] != "None":
        cape = img_open(item[6],qualitys[6])    
        gear_img.paste(cape,Body_area[6],cape)
    if item[7] != "None":
        mount = img_open(item[7],qualitys[7])
        gear_img.paste(mount,Body_area[7],mount)
    if item[8] != "None":
        food = img_open(item[8],qualitys[8])
        gear_img.paste(food,Body_area[8],food)
    if item[9] != "None":    
        potions = img_open(item[9],qualitys[9])
        gear_img.paste(potions,Body_area[9],potions)
    gear_img.thumbnail(size)
    return gear_img

def get_text_values(killer,victim,fame,participants):
    # Take Background
    img = background
    # All text process
    killer = killer[0]
    victim = victim[0]
    print(killer[0])
    if killer[0] == "None" or killer[1] == "None":
        killer[0] = "-" 
        killer[1] = "-"
    if victim[0] == "None" or victim[1] == "None":
        victim[0] = "-" 
        victim[1] = "-"    
    participants = participants[0]
    if len(participants) == 0:
        x = 1    
    else:
        x = len(participants)
    img = text_process(logo,logo_size,img,logo_area)
    img = text_process(sec_logo,logo_size,img,sec_logo_area)
    img = text_process(dmg,dmg_size,img,dmg_area)
    img = text_process(str(killer[2]),killer_name_size,img,killer_name_area)
    img = text_process(str(killer[0]+killer[1]),killer_name_size,img,killer_guild_area)
    img = text_process("IP: "+str(killer[3]),killer_name_size,img,killer_ip_area)
    img = text_process(str(victim[2]),victim_name_size,img,victim_name_area)
    img = text_process(str(victim[0]+victim[1]),victim_name_size,img,victim_guild_area)
    img = text_process("IP: "+str(victim[3]),victim_name_size,img,victim_ip_area)
    img = text_process(str(fame),rblock_size,img,fame_area)
    img = text_process(str(x)+"x"+ str(int(fame/x)),rblock_size,img,fdiv_area)
    # Participant's Damage text process
    for i in range(0,len(participants)):
        p_area = ptcp[i]
        img = participants_text(participants[i][0]+":"+str(participants[i][1]),rblock_size,img,p_area,participants[i][2])
    img = img_paste(img,fame_image,fimg_area)
    return img

def check_participants(participants):
    total = []       
    for i in range(0,len(participants)):
        if i == 0:
            d1 = [participants[i][0],participants[i][1],'red']
            total.append(d1)
            d2 = [participants[i][0],participants[i][2],'green'] 
            total.append(d2)
        elif i == 1:
            d3 = [participants[i][0],participants[i][1],'red']
            total.append(d3)
            d4 = [participants[i][0],participants[i][2],'green']
            total.append(d4)
        elif i == 2:
            d5 = [participants[i][0],participants[i][1],'red']
            total.append(d5)
            d6 = [participants[i][0],participants[i][2],'green']     
            total.append(d6)
        elif i == 3:
            d7 = [participants[i][0],participants[i][1],'red']
            total.append(d7)
            d8 = [participants[i][0],participants[i][2],'green'] 
            total.append(d8)
        elif i == 4:
            d9 = [participants[i][0],participants[i][1],'red']
            total.append(d9)
            d10 = [participants[i][0],participants[i][2],'green'] 
            total.append(d10)
    #ilk_beş_eleman = sorted(liste, key = lambda eleman: int(eleman[1]), reverse = True)[:5]
    if (len(participants)*2) > 5: 
        a = 5
    else:
        a = len(participants)
    firstfive = sorted(total, key = lambda dmg: dmg[1], reverse= True)[:a]
    firstfive = [firstfive]
    return firstfive
 
def PickinSQL():
    db = sqlite3.connect('KillbotDatabase.sqlite')
    imlec = db.cursor()
    imlec.execute("SELECT EventID, KillerProfile, KillerEquipment, VictimProfile, VictimEquipment,VictimInventory, TotalKillFame, Participants FROM 'Iron_Hand_KillBot'")
    data = []
    if imlec != [] or imlec != None:
        for i in imlec:
            data.append(i)
        db.close()
        return data
    else:
        db.close()
        return None


def make_url(eventID):
    url = "https://albiononline.com/en/killboard/kill/{}".format(eventID)
    return url

def img_main(data):
    img_list = []
    for i in range(0,len(data)):
        EventID, Killer_Profile, Killer_Equipment, Victim_Profile, Victim_Equipment,Victim_Inventory, TotalKillFame, Participants = data[i]
        event_url = make_url(EventID)
        print(event_url)
        participant_s = check_participants(Participants)
        event_img = get_text_values(Killer_Profile,Victim_Profile,TotalKillFame,participant_s)
        killer_gear = get_gear_img(Killer_Equipment)
        #killer_gear.resize((350,300))
        victim_gear = get_gear_img(Victim_Equipment)
        #victim_gear.resize((350,300))
        event_img = img_paste(event_img,killer_gear,killer_area)
        event_img = img_paste(event_img,victim_gear,victim_area)
        img_list.append(event_img)
        event_img.show()  
    return img_list
