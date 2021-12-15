
weapons = {
    0:"Lava Gun",
    1:"Morph O' Ray",
    2:"Mines",
    3:"Gravity Bomb",
    4:"Rockets",
    5:"Blitz",
    6:"N60",
    7:"Flux"
}

def weaponParser(num):
    '''Accepts PLAYER_SKILL_LEVEL named field INTEGER number (which is 2 a byte long hex string)'''
    # print("player skill number {} ".format(num))
    num = int(num) if type(num) != 'int' else num
    num = format(num, "#010b")[2:]
    res = []
    for i in range(len(num)-1, -1, -1):
        if num[i] == "0":
            res.append(weapons[i])
    return res



import struct
OTHER_RULES = {
    'base_defenses' : 19,
    "spawn_charge_boots":18,   
    'spawn_weapons':17,
    'unlimited_ammo':16,
    "player_names":9,
    "vehicles":1,

}

def advancedRulesParser(num):
    '''Accepts generic_field_3 INTEGER number (which is 4 a byte long hex string)
    returns game MODE andd game SUBMODE/ type'''
    advanced_rules = {}
    num = int(num) if type(num) != 'int' else num
    num = struct.pack('<I', num).hex()
    num=num[2:] #cut off the front 2 bytes
    num = int(num,16)
    num = format(num, "#026b")[2:]
    advanced_rules['baseDefenses'] = True if num[OTHER_RULES['base_defenses']] == '1' else False
    advanced_rules['spawn_charge_boots'] = True if num[OTHER_RULES['spawn_charge_boots']] == '1' else False
    advanced_rules['spawn_weapons'] = True if num[OTHER_RULES['spawn_weapons']] == '1' else False
    advanced_rules["player_names"] = True if num[OTHER_RULES["player_names"]] == '1' else False
    advanced_rules['vehicles'] = True if num[OTHER_RULES['vehicles']] == '0' else False
    return advanced_rules


import struct
MAPS = {
    "00001":"Bakisi_Isle",
    "00010":"Hoven_Gorge",
    "00011":"Outpost_x12",
    "00100":"Korgon_Outpost",
    "00101":"Metropolis",
    "00110":"Blackwater_City",
    "00111":"Command_Center",
    "01001":'Aquatos_Sewers',
    "01000": "Blackwater_Dox",
    "01010":"Marcadia_Palace",
}


def mapParser(num):
    '''Accepts generic_field_3 INTEGER number (which is 4 a byte long hex string)'''
    num = int(num) if type(num) != 'int' else num
    num = struct.pack('<I', num).hex()
    num=num[0:2]
    num = int(num,16)
    num = format(num, "#010b")[2:]
    game_map = num[:5]
    game_map = MAPS[game_map]
    return game_map


import struct


TIME = {
    '000':'no_time_limit',
    '001':"5_minutes",
    '010':"10_minutes",
    '011':"15_minutes",
    "100":"20_minutes",
    "101":"25_minutes",
    "110":"30_minutes",
    "111":"35_minutes",
}

def timeParser(num):
    '''Accepts generic_field_3 INTEGER number (which is 4 a byte long hex string)'''
    num = int(num) if type(num) != 'int' else num
    num = struct.pack('<I', num).hex()
    num=num[0:2]
    num = int(num,16)
    num = format(num, "#010b")[2:]
    game_time = num[5:]  
    game_time = TIME[game_time]
    return game_time



import struct
MODE={ #3,4
    '00':"Siege",
    '01':"CTF",
    '10':"Deathmatch"
}
SUBMODES = { 
    # '1':"no_teams", #13
    # "1":"base_attrition" #20
    'isTeams':13, #1 = yes, means u can swap teams only 0 in DM
    "isAttrition":20, #1 = yes #consitutes also as chaos ctf

}


def gamerulesParser(num):
    '''Accepts generic_field_3 INTEGER number (which is 4 a byte long hex string)
    returns game MODE andd game SUBMODE/ type'''
    num = int(num) if type(num) != 'int' else num
    num = struct.pack('<I', num).hex()
    num=num[2:] #cut off the front 2 bytes
    num = int(num,16)
    num = format(num, "#026b")[2:]
    game_mode = MODE[num[3:5]] if num[3:5] in MODE else "Unknown Game Mode"
    isTeams = True if num[SUBMODES['isTeams']] == '1' else False
    isAttrition = True if num[SUBMODES['isAttrition']]== '1' else False
    
    if game_mode == MODE['00']:
        game_type = "Attrition" if isAttrition else "Normal"
    elif game_mode == MODE['01']:
        game_type = "Chaos" if isAttrition else "Normal"
    elif game_mode == MODE['10']:
        game_type = "Teams" if isTeams else "FFA"
    else:
        game_type = "Game Type Not Found"
    return game_mode, game_type