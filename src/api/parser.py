from utils import utils
from enums.enums import CLANTAG_ALLOWED_CHARACTERS

LADDER_STATS_WIDE_BREAKDOWN = {
0: '',
1: 'overall rank',
2: 'wins',
3: 'losses',
4: 'w/l ratio',
5: 'kills',
6: 'deaths',
7: 'suicides',
8: 'kill/death ratio',
9: 'base dmg',
10: 'nodes',
11: 'games played',
12: '',
13: '',
14: '',
15: '',
16: 'dm rank',
17: 'siege rank',
18: 'ctf rank',
19: '',
20: 'n60 deaths',
21: 'n60 kills',
22: 'lava gun deaths',
23: 'lava gun kills',
24: 'gravity bomb deaths',
25: 'gravity bomb kills',
26: 'flux rifle deaths',
27: 'flux rifle kills',
28: 'mins glove deaths',
29: 'mine glove kills',
30: 'morph-o-ray deaths',
31: 'morph-o-ray kills',
32: 'blitz cannon deaths',
33: 'blitz cannon kills',
34: 'rocket deaths',
35: 'rocket kills',
36: 'wrench deaths',
37: 'wrench kills',
38: 'siege wins',
39: 'siege losses',
40: 'siege w/l ratio',
41: 'siege kills',
42: 'siege deaths',
43: 'siege k/d ratio',
44: 'siege base dmg',
45: 'siege nodes',
46: 'siege games played',
47: 'dm wins',
48: 'dm losses',
49: 'dm w/l ratio',
50: 'dm kills',
51: 'dm deaths',
52: 'dm k/d ratio',
53: 'dm games played',
54: 'ctf wins',
55: 'ctf losses',
56: 'ctf w/l ratio',
57: 'ctf kills',
58: 'ctf deaths',
59: 'ctf k/d ratio',
60: 'ctf base dmg',
61: 'ctf nodes',
62: 'ctf flags captured',
63: 'ctf flags saved',
64: 'ctf games played',
65: '',
66: 'siege suicides',
67: 'ctf suicides',
68: 'dm suicides',
69: 'avg kills',
70: 'avg deaths',
71: 'avg suicides',
72: 'avg nodes',
73: 'avg base dmg',
74: 'siege avg kills',
75: 'siege avg deaths',
76: 'siege avg nodes',
77: 'siege avg base dmg',
78: 'siege avg suicides',
79: 'ctf avg kills',
80: 'ctf avg deaths',
81: 'ctf avg nodes',
82: 'ctf avg base dmg',
83: 'ctf avg flags',
84: 'ctf avg flag saves',
85: 'ctf avg suicides',
86: 'dm avg kills',
87: 'dm avg deaths',
88: 'dm avg suicides',
89: 'total squats',
90: 'avg squats',
91: 'squat/kill ratio',
92: 'total times squatted',
93: 'avg times squatted on',
94: 'squatted/death ratio',
95: 'total team squats',
96: 'avg team squats',
97: '',
98: '',
99: '',
}

CLAN_STATS_BREAKDOWN = {
0: 'kills',
1: 'deaths',
2: 'wins',
3: 'losses',
4: '',
5: '',
6: '',
7: 'avg overall rank',
8: 'avg siege rank',
9: 'avg dm rank',
10: 'avg ctf rank',
11: 'avg power rank',
12: 'siege power rank',
13: 'dm power rank',
14: 'ctf power rank',
15: 'w/l ratio',
16: 'k/d ratio',
17: '',
18: '',
19: '',
20: '',
}

def generate_skill_bolt_stats(siege_bolt, dm_bolt, ctf_bolt, overall_bolt):
    skill_bolt_codes = {
        1: ['00C0A844', '0000AF43'],
        2: ['00C0A844', '00808443'],
        3: ['00C0A844', '00000000'],
        4: ['C8C8D444', '00808943']
    }
    res = ''
    for idx in range(2):
        for rank in [siege_bolt, dm_bolt, ctf_bolt, overall_bolt]:
            a = skill_bolt_codes[rank][idx]
            res += a
    return res

def get_skill_from_ladderstatswide(ladderstatswide):
    def get_skill_from_game(games):
        if 0 <= games < 200:
            return 1
        if 200 <= games < 400:
            return 2
        if 400 <= games < 800:
            return 3
        else:
            return 4
    result = {}
    ladder_array = [ladderstatswide[i:i+8] for i in range(0, len(ladderstatswide), 8)]

    result['Siege'] = get_skill_from_game(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_array[46])))
    result['CTF'] = get_skill_from_game(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_array[64])))
    result['Deathmatch'] = get_skill_from_game(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_array[53])))
    result['Overall'] = get_skill_from_game(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_array[11])))
    return result

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



def get_clean_clan_tag_from_stats(tag: str):
    tag = utils.hex_to_bytes(tag)[16:24].hex().upper()

    clan_tag = [tag[i:i+4] for i in range(0,len(tag),4)]
    result = []
    for i in range(len(clan_tag)):
        character = CLANTAG_ALLOWED_CHARACTERS[clan_tag[i]]
        if len(character) == 1:
            result.append(character)
    result = ''.join(list(reversed(result)))
    return result

def parse_clanstats_wide(data: dict):
    statswide = data['clan_statswide']
    statswide = utils.hex_to_bytes(statswide)
    data['kills'] = utils.bytes_to_int_little(statswide[0:4])
    data['deaths'] = utils.bytes_to_int_little(statswide[4:8])
    data['wins'] = utils.bytes_to_int_little(statswide[8:12])
    data['losses'] = utils.bytes_to_int_little(statswide[12:16])
    return data
