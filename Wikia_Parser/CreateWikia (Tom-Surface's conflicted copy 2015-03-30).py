import sys, json, os, glob, time
import operator
import shutil
import csv
import time
import sys

dir = os.path.dirname(__file__)
template_path = os.path.join(dir, "templates")
json_path = os.path.join(os.path.dirname(__file__), 'JSON')
output_path = os.path.join(os.path.dirname(__file__), 'output')

data = {}
names = {}
extradata = {}


def main():
    if (os.path.exists(output_path)):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    global extradata
    extradata = json.load(open("ExtraData.json"))
    get_data()

    # output_duplicate_report()

    do_stuff()


def output_duplicate_report():
    outlist = []
    ass = 0
    for (main_key, main_data) in names.items():
        current_count = 0
        for (skill_key, skill_data) in main_data.items():
            current_count += len(skill_data)
        outlist.append((main_key, current_count))
    sortedd = sorted(outlist, key=lambda tup: tup[1], reverse=True)

    with open('output.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='', quoting=csv.QUOTE_NONE)
        spamwriter.writerow(['name', 'amount'])
        for single in outlist:
            spamwriter.writerow([single[0], single[1]])


# Main "doing" method
def do_stuff():
    for type_key in data.keys():
        #valid_keys = ["Armors", "Items", "Skills", "Weapons", "Enemies", "Actors"]
        valid_keys = {"Actors"}
        #valid_keys = ["Enemies"]
        if not type_key in valid_keys:
            continue

        f_template = open(os.path.join(template_path, type_key + ".txt"))
        atemplate = f_template.read()
        print("\n")
        print("Processing " + type_key)
        count = 0
        for (my_key, my_data) in data[type_key].items():
            count += 1
            update_progress(count, len(data[type_key].items()))
            result = getattr(sys.modules[__name__], "get_%s" % type_key)(my_data)
            test = atemplate % getattr(sys.modules[__name__], "get_%s" % type_key)(my_data)

            save_stuff(my_data["id"], my_data["name"], type_key, output_path, test)


def get_Actors(my_data):
    output = {'name': my_data["name"],#
              'image': "%s_%s.png" % (my_data["name"], my_data["nickname"]),#
              'fullname': "%s %s" % (my_data["name"], my_data["nickname"]),#
              'class_name': data["Classes"][my_data["class_id"]]["name"],#
              'caption': my_data["description"].replace("\r", "").replace("\n", " "),#
              'weapon_types': "",#
              'armor_types': "",#
              'skill_types': "",#
              'Target_Rate': "",#
              'Evasion': "",#
              'Hit_Rate': "",#
              'Crit_Chance': "",#
              'feature1': "",
              'feature2': "",
              'feature3': "",
              'feature4': "",
              'feature5': "",
              'feature6': "",
              'feature7': "",
              'feature8': "",
              'feature9': "",
              'feature10': "",
              'feature11': "",
              'feature12': "", }

    feature_no = 1
    #GET DATA FROM ACTOR---------------------------------------------------------------
    for single_feature in my_data["features"]:
        #ARMOR
        if single_feature["code"] == 52:
            value = extradata["ArmorType"][str(single_feature["data_id"])]
            if value not in output["armor_types"]:
                if output["armor_types"] != "":
                    output["armor_types"] += " / "
                output["armor_types"] += value
        #SKILLS
        elif single_feature["code"] == 41:
            value = extradata["Armors"]["Features"]["41"]["values"][str(single_feature["data_id"])]
            if value not in output["skill_types"]:
                if output["skill_types"] != "":
                    output["skill_types"] += " / "
                output["skill_types"] += extradata["Armors"]["Features"]["41"]["values"][str(single_feature["data_id"])]
        #Weapon
        elif single_feature["code"] == 51:
            value = extradata["Armors"]["Features"]["51"]["values"][str(single_feature["data_id"])]
            if value not in output["skill_types"]:
                if output["weapon_types"] != "":
                    output["weapon_types"] += " / "
                output["weapon_types"] += extradata["WeaponType"][str(single_feature["data_id"])]
        #EX PARAMATER
        elif single_feature["code"] == 22:
            #HIT
            if single_feature["data_id"] == 0:
                output['Hit_Rate'] = "%d%%" % (single_feature["value"] * 100)
            #EVA
            elif single_feature["data_id"] == 1:
                output['Evasion'] = "%d%%" % (single_feature["value"] * 100)
                pass
            #CRI
            elif single_feature["data_id"] == 2:
                output['Crit_Chance'] = "%d%%" % (single_feature["value"] * 100)
                pass
        #TARGET
        elif single_feature["code"] == 23:
            output['Target_Rate'] = "%d%%" % (single_feature["value"] * 100)

    #GET DATA FROM CLASS------------------------------------------------------
    for single_feature in data["Classes"][my_data["class_id"]]["features"]:
        #ARMOR
        if single_feature["code"] == 52:
            value = extradata["ArmorType"][str(single_feature["data_id"])]
            if value not in output["armor_types"]:
                if output["armor_types"] != "":
                    output["armor_types"] += " / "
                output["armor_types"] += value
        #SKILLS
        elif single_feature["code"] == 41:
            value = extradata["Armors"]["Features"]["41"]["values"][str(single_feature["data_id"])]
            if value not in output["skill_types"]:
                if output["skill_types"] != "":
                    output["skill_types"] += " / "
                output["skill_types"] += extradata["Armors"]["Features"]["41"]["values"][str(single_feature["data_id"])]
        #Weapon
        elif single_feature["code"] == 51:
            value = extradata["Armors"]["Features"]["51"]["values"][str(single_feature["data_id"])]
            if value not in output["weapon_types"]:
                if output["weapon_types"] != "":
                    output["weapon_types"] += " / "
                output["weapon_types"] += extradata["WeaponType"][str(single_feature["data_id"])]
        #EX PARAMATER
        elif single_feature["code"] == 22:
            #HIT
            if single_feature["data_id"] == 0:
                output['Hit_Rate'] = "%d%%" % (single_feature["value"] * 100)
            #EVA
            elif single_feature["data_id"] == 1:
                output['Evasion'] = "%d%%" % (single_feature["value"] * 100)
                pass
            #CRI\
            elif single_feature["data_id"] == 2:
                output['Crit_Chance'] = "%d%%" % (single_feature["value"] * 100)
                pass
        #TARGET
        elif single_feature["code"] == 23:
            output['Target_Rate'] = "%d%%" % (single_feature["value"] * 100)
        else:
            result = process_feature(my_data, single_feature)
            if result != None:
                output["feature" + str(feature_no)] = result
                feature_no += 1
    for x in range(feature_no, 13):
        output["feature" + str(x)] = ""
        pass
    return output


#METHODS run my do_stuff()
def get_Armors(my_data):
    output = {'image': extradata["icons"][str(my_data["icon_index"])],
              'armorType': extradata["ArmorType"][str(my_data['atype_id'])],
              'equipType': extradata["EquipType"][str(my_data['etype_id'])],
              'ATK': my_data["params"][2],
              'DEF': my_data["params"][3],
              'SATK': my_data["params"][4],
              'SDEF': my_data["params"][5],
              'AGI': my_data["params"][6],
              'LUCK': my_data["params"][7],
              'HP': my_data["params"][0],
              'SP': my_data["params"][1],
              'Description': my_data["description"],
              "name": my_data["name"],
              "id": my_data["id"], }
    #FEATURES
    feature_no = 1
    for single_feature in my_data["features"]:
        result = process_feature(my_data, single_feature)
        if result != None:
            output["feature" + str(feature_no)] = result
            feature_no += 1

    for x in range(feature_no, 17):
        output["feature" + str(x)] = ""
        pass

    return output


def get_Weapons(my_data):
    output = {'image': extradata["icons"][str(my_data["icon_index"])],
              'weaponType': extradata["WeaponType"][str(my_data['wtype_id'])],
              'ATK': my_data["params"][2],
              'DEF': my_data["params"][3],
              'SATK': my_data["params"][4],
              'SDEF': my_data["params"][5],
              'AGI': my_data["params"][6],
              'LUCK': my_data["params"][7],
              'HP': my_data["params"][0],
              'SP': my_data["params"][1],
              "Description": my_data["description"].replace("\r", "").replace("\n", " "),
              "name": my_data["name"],
              "id": my_data["id"], }

    #FEATURES
    feature_no = 1
    for single_feature in my_data["features"]:
        result = process_feature(my_data, single_feature)
        if result != None:
            output["feature" + str(feature_no)] = result
            feature_no += 1

    for x in range(feature_no, 17):
        output["feature" + str(x)] = ""
        pass

    return output


def get_Items(my_data):
    effects = ""

    tp_gain = ""
    damage_type = ""
    element_type = ""
    formula = ""
    variance = ""
    critical = ""

    if my_data["tp_gain"] != 0:
        tp_gain = my_data["tp_gain"]

    if my_data["damage"]["type"] != 0:
        damage_type = extradata["DamageType"][str(my_data["damage"]["type"])]
        element_type = extradata["ElementType"][str(my_data["damage"]["element_id"])]
        formula = my_data["damage"]["formula"]
        variance = my_data["damage"]["variance"]
        critical = my_data["damage"]["critical"]

    for effect in my_data["effects"]:
        #HP + MP Recovery
        if effect["code"] == 11 or effect["code"] == 12:
            value_id = 1 if effect["value2"] == 0 else 2
            amount = str(int(effect[("value" + str(value_id))] * 100)) if effect["value2"] == 0 else str(
                int(effect[("value" + str(value_id))]))
            text = extradata["Effect"][str(effect["code"])][str(value_id)]
            effects += (text % amount) + "\n"
        # TP Recovery
        elif effect["code"] == 13:
            text = extradata["Effect"][str(effect["code"])]
            amount = str(int(effect[("value" + str(value_id))]))
            effects += (text % amount) + "\n"
            pass
        # States + Buffs
        elif effect["code"] == 21:
            text = extradata["Effect"][str(effect["code"])]
            chance = str(int((effect["value1"] * 100)))
            state = data["States"][effect["data_id"]]["name"]
            effects += (text % (chance, state)) + "\n"
        elif effect["code"] == 22 or effect["code"] == 33 or effect["code"] == 34:
            text = extradata["Effect"][str(effect["code"])]
            state = data["States"][effect["data_id"]]["name"]
            effects += (text % (state)) + "\n"
        elif effect["code"] == 31 or effect["code"] == 32:
            text = extradata["Effect"][str(effect["code"])]
            state = data["States"][effect["data_id"]]["name"]
            turns = str(int((effect["value1"])))
            effects += (text % (state, turns)) + "\n"
        elif effect["code"] == 41:
            text = extradata["Effect"][str(effect["code"])]
            effects += (text % "Escape") + "\n"
        elif effect["code"] == 42:
            text = extradata["Effect"][str(effect["code"])]
            stat = extradata["BasicStatus"][str(effect["data_id"])]
            amount = str(int(effect["value1"]))
            effects += (text % (stat, amount))
        elif effect["code"] == 43:
            text = extradata["Effect"][str(effect["code"])]
            skill = data["Skills"][effect["data_id"]]["name"]
            effects += (text % skill) + "\n"
        elif effect["code"] == 44:
            text = extradata["Effect"][str(effect["code"])]
            event_text = data["CommonEvents"][effect["data_id"]]["name"]
            effects += (text % event_text) + "\n"

    effects = effects.rstrip('\n')

    return {"image": extradata["icons"][str(my_data["icon_index"])],
            "description": my_data["description"].replace("\r", "").replace("\n", " "),
            "name": my_data["name"],
            "consumable": my_data["consumable"],
            "occasion": extradata["Occasion"][str(my_data["occasion"])],
            "price": my_data["price"],
            "scope": extradata["Scope"][str(my_data["scope"])],
            "note": my_data["note"].rstrip('\n'),
            "speed": my_data["speed"],
            "id": my_data["id"],
            "effects": effects,
            "damage_type": damage_type,
            "success_rate": str(my_data["success_rate"]) + "%",
            "hit_type": extradata["HitType"][str(my_data["hit_type"])],
            "item_type": my_data["itype_id"],
            "repeats": my_data["repeats"],
            "tp_gain": tp_gain,
            "element_type": element_type,
            "formula": formula,
            "variance": variance,
            "critical": critical,
            "name": my_data["name"]}


def get_Skills(my_data):
    effects = ""

    tp_gain = ""
    damage_type = ""
    element_type = ""
    formula = ""
    variance = ""
    critical = ""

    required_weapon1 = ""
    required_weapon2 = ""
    message = ""

    mp_cost = ""
    tp_cost = ""

    if my_data["tp_gain"] != 0:
        tp_gain = my_data["tp_gain"]

    if my_data["damage"]["type"] != 0:
        damage_type = extradata["DamageType"][str(my_data["damage"]["type"])]
        element_type = extradata["ElementType"][str(my_data["damage"]["element_id"])]
        formula = my_data["damage"]["formula"]
        variance = my_data["damage"]["variance"]
        critical = my_data["damage"]["critical"]

    for effect in my_data["effects"]:
        #HP + MP Recovery
        if effect["code"] == 11 or effect["code"] == 12:
            value_id = 1 if effect["value2"] == 0 else 2
            amount = str(int(effect[("value" + str(value_id))] * 100)) if effect["value2"] == 0 else str(
                int(effect[("value" + str(value_id))]))
            text = extradata["Effect"][str(effect["code"])][str(value_id)]
            effects += (text % amount) + "\n"
        # TP Recovery
        elif effect["code"] == 13:
            text = extradata["Effect"][str(effect["code"])]
            amount = str(int(effect["value1"]))
            effects += (text % amount) + "\n"
            pass
        # States + Buffs
        elif effect["code"] == 21:
            text = extradata["Effect"][str(effect["code"])]
            chance = str(int((effect["value1"] * 100)))
            if effect["data_id"] == 0:
                state = "Normal Attack"
            else:
                state = data["States"][effect["data_id"]]["name"]
            effects += (text % (chance, state)) + "\n"
        elif effect["code"] == 22 or effect["code"] == 33 or effect["code"] == 34:
            text = extradata["Effect"][str(effect["code"])]
            state = data["States"][effect["data_id"]]["name"]
            effects += (text % (state)) + "\n"
        elif effect["code"] == 31 or effect["code"] == 32:
            text = extradata["Effect"][str(effect["code"])]
            state = data["States"][effect["data_id"]]["name"]
            turns = str(int((effect["value1"])))
            effects += (text % (state, turns)) + "\n"
        elif effect["code"] == 41:
            text = extradata["Effect"][str(effect["code"])]
            effects += (text % "Escape") + "\n"
        elif effect["code"] == 42:
            text = extradata["Effect"][str(effect["code"])]
            stat = extradata["BasicStatus"][str(effect["data_id"])]
            amount = str(int(effect["value1"]))
            effects += (text % (stat, amount))
        elif effect["code"] == 43:
            text = extradata["Effect"][str(effect["code"])]
            skill = data["Skills"][effect["data_id"]]["name"]
            effects += (text % skill) + "\n"
        elif effect["code"] == 44:
            text = extradata["Effect"][str(effect["code"])]
            event_text = data["CommonEvents"][effect["data_id"]]["name"]
            effects += (text % event_text) + "\n"

    effects = effects.rstrip('\n')

    if my_data["message2"] == "" or my_data["message2"].isspace():
        message = "(User) " + my_data["message1"]
    elif my_data["message1"] == "" or my_data["message1"].isspace():
        message = my_data["message2"]

    if my_data["required_wtype_id1"] > 1:
        required_weapon1 = extradata["WeaponType"][str(my_data["required_wtype_id1"])]

    if my_data["required_wtype_id2"] > 1:
        required_weapon2 = extradata["WeaponType"][str(my_data["required_wtype_id2"])]

    if my_data["mp_cost"] > 1:
        mp_cost = my_data["mp_cost"]
    elif my_data["tp_cost"] > 1:
        tp_cost = my_data["tp_cost"]
    else:
        mp_cost = 0

    return {"image": extradata["icons"][str(my_data["icon_index"])],
            "description": my_data["description"].replace("\r", "").replace("\n", " "),
            "name": my_data["name"],
            "tp_cost": my_data["tp_cost"],
            "occasion": extradata["Occasion"][str(my_data["occasion"])],
            "mp_cost": my_data["mp_cost"],
            "scope": extradata["Scope"][str(my_data["scope"])],
            "note": my_data["note"].rstrip('\n'),
            "speed": my_data["speed"],
            "id": my_data["id"],
            "effects": effects,
            "damage_type": damage_type,
            "success_rate": my_data["success_rate"],
            "hit_type": extradata["HitType"][str(my_data["hit_type"])],
            "skill_type": extradata["Skill_Type"][str(my_data["stype_id"])],
            "repeats": my_data["repeats"],
            "tp_gain": tp_gain,
            "element_type": element_type,
            "formula": formula,
            "variance": variance,
            "critical": critical,
            "message": message,
            "required_weapon1": required_weapon1,
            "required_weapon2": required_weapon2,
            "name": my_data["name"]
    }


def get_Enemies(my_data):
    #ACTIONS
    item_drops = ""
    actionstext = ""

    output = dict(name=get_att(my_data, "name"),
                  gold=get_att(my_data, "gold"),
                  battler_hue=get_att(my_data, "battler_hue"),
                  exp=get_att(my_data, "exp"),
                  hit=get_att(my_data, "hit"),
                  battler_name=get_att(my_data, "battler_name"),
                  image=get_battler_image(get_att(my_data, "battler_name")),
                  id=get_att(my_data, "id"),
                  eva=get_att(my_data, "eva"),
                  drop_items=item_drops,
                  ATK=get_att(my_data, "params", 2),
                  DEF=get_att(my_data, "params", 3),
                  SATK=get_att(my_data, "params", 4),
                  SDEF=get_att(my_data, "params", 5),
                  AGI=get_att(my_data, "params", 6),
                  LUCK=get_att(my_data, "params", 7),
                  HP=get_att(my_data, "params", 0),
                  SP=get_att(my_data, "params", 1))

    #DROP ITEMS
    kinds = ["", "Items", "Weapons", "Armors"]
    drop_no = 1
    for single_drop_item in my_data["drop_items"]:
        if single_drop_item["kind"] == 0:
            continue

        value = get_filename_of_item(data[kinds[single_drop_item["kind"]]][single_drop_item["data_id"]]["name"],
                                     data[kinds[single_drop_item["kind"]]][single_drop_item["data_id"]]["id"],
                                     kinds[single_drop_item["kind"]])
        chance = single_drop_item["denominator"]
        output["itemdrop" + str(drop_no)] = "1/%d chance of [[%s|%s]]" % \
                                            (chance,
                                             data[kinds[single_drop_item["kind"]]][single_drop_item["data_id"]]["name"],
                                             value)
        drop_no += 1

    for x in range(drop_no, 4):
        output["itemdrop" + str(x)] = ""
        pass

    #FEATURES
    feature_no = 1
    for single_feature in my_data["features"]:
        result = process_feature(my_data, single_feature)
        if result != None:
            output["feature" + str(feature_no)] = result
            feature_no += 1

    for x in range(feature_no, 17):
        output["feature" + str(x)] = ""
        pass

    if output["name"] == "Wally":
        pass

    #ACTIONS
    action_no = 1
    for action in my_data["actions"]:
        output["action%d_skill" % action_no] = "[[%s|%s]]" % \
                                               (get_filename_of_skill(data["Skills"][action["skill_id"]]["name"],
                                                                      data["Skills"][action["skill_id"]]["id"]),
                                                data["Skills"][action["skill_id"]]["name"])
        output["action%d_r" % action_no] = action["rating"]

        if action["condition_type"] == 0:
            output["action%d_condition" % action_no] = "Always"
        elif action["condition_type"] == 1:
            output["action%d_condition" % action_no] = "Begin turn %d, repeat every %d" % \
                                                       (action["condition_param1"], action["condition_param2"])
        elif action["condition_type"] == 2:
            output["action%d_condition" % action_no] = "When HP is between %d%% - %s%%" % \
                                                       (int(action["condition_param1"] * 100),
                                                        int(action["condition_param2"] * 100))
        elif action["condition_type"] == 3:
            output["action%d_condition" % action_no] = "When MP is between %d%% - %s%%" % \
                                                       (int(action["condition_param1"] * 100),
                                                        int(action["condition_param2"] * 100))
        elif action["condition_type"] == 4:
            output["action%d_condition" % action_no] = "When [[%d]]" % data["States"][action["condition_param1"]][
                "name"]
        elif action["condition_type"] == 5:
            output["action%d_condition" % action_no] = "When party level avg is %s or above" % action[
                "condition_param1"]
        elif action["condition_type"] == 6:
            output["action%d_condition" % action_no] = "Program Switch %d" % action["condition_param1"]

        #actionstext += "%s | %s | %s\n" % (single["skill_name"], single["rating"], single["conditions"])
        #actions.append(single)
        action_no += 1

    for x in range(action_no, 13):
        output["action%d_skill" % x] = ""
        output["action%d_r" % x] = ""
        output["action%d_condition" % x] = ""
        pass

    return output


#Grabs all data from JSON folder and modifies to allow for O(1) search, output -> data
def get_data():
    path = json_path + "/*.json"
    for fname in glob.glob(path):
        # print(fname)
        base = os.path.splitext(os.path.basename(fname))[0]
        print("Loading " + base)
        f = open(fname)
        # print(f)
        # ass = f.read()

        MY_JSON = json.load(f)
        new_json = {}
        for thing in MY_JSON:
            if thing is None:
                continue
            elif thing["name"] == "":
                continue
            elif sane_file_name(thing["name"]) in extradata["blacklist"]:
                continue
            new_json[thing["id"]] = thing
            add_name(thing["name"], base, thing["id"])
        data[base] = new_json


def get_battler_image(battler):
    if battler == " ":
        return ""
    else:
        battler = battler.replace(" ", "_")
        return "Battler_" + battler + ".png"


def get_att(the_data, key, index=None):
    if index is not None:
        return " " if not key in the_data.keys() else the_data[key][index]
    else:
        return " " if not key in the_data.keys() else the_data[key]


def process_feature(my_data, single_feature):
    if single_feature["code"] == 11 or single_feature["code"] == 12:
        if single_feature["value"] != 0:
            element = extradata["Features"][str(single_feature["code"])]["values"][str(single_feature["data_id"])]
            value = str(int(single_feature["value"] * 100))
            return "[[%s]] * %s%%" % (element, value)
    elif single_feature["code"] == 13:
        element = data["States"][single_feature["data_id"]]["name"]
        value = str(int(single_feature["value"] * 100))
        return "[[%s]] * %s%%" % (element, value)
    elif single_feature["code"] == 14:
        element = data["States"][single_feature["data_id"]]["name"]
        return "State Resist: [[%s]]" % (element)
    elif single_feature["code"] == 21 or single_feature["code"] == 22 or single_feature["code"] == 23:
        if single_feature["value"] != 0:
            element = extradata["Features"][str(single_feature["code"])]["values"][str(single_feature["data_id"])]
            value = str(int(single_feature["value"] * 100))
            return "[[%s]] * %s%%" % (element, value)
    elif single_feature["code"] == 31:
        return "Attack Element: %s" % extradata["Features"][str(single_feature["code"])]["values"][
            str(single_feature["data_id"])]
    elif single_feature["code"] == 32:
        element = data["States"][single_feature["data_id"]]["name"]
        value = str(int(single_feature["value"] * 100))
        return "Attack State: [[%s]] + %s%%" % (element, value)
    elif single_feature["code"] in (33, 34, 61):
        value = str(int(single_feature["value"]))
        temptype = "Template+" if single_feature["value"] > 0 else "Template-"
        template = extradata["Features"][str(single_feature["code"])][temptype]
        return template % value
    elif single_feature["code"] in (41, 42, 43, 41, 51, 52, 53, 54, 55, 62, 63, 64):
        template = extradata["Features"][str(single_feature["code"])]["Template"]
        return template % extradata["Features"][str(single_feature["code"])]["values"][str(single_feature["data_id"])]
    return None


#Add name to global list to see if Disambig pages are needed
def add_name(name, base, id):
    # Does the name exist? If not, make the new Dict, if so, check if the base also exists
    name = sane_file_name(name)
    if name not in names:
        names[name] = {}

    if base in names[name].keys():
        names[name][base].append(id)
    else:
        names[name][base] = []
        names[name][base].append(id)


def get_filename_of_item(name, id, type_key):
    name = sane_file_name(name).strip()
    extra_text = ""

    if len(names[name].keys()) > 1:
        if type_key == "Enemies":
            extra_text = "(Enemy)"
        else:
            extra_text = "(%s)" % type_key.rstrip("s")

    if len(names[name][type_key]) > 1:
        extra_text += "_" + str(id)

    return name + extra_text


def get_filename_of_skill(name, id):
    name = sane_file_name(name).strip()
    extra_text = ""

    if len(names[name].keys()) > 1:
        extra_text = "(Skill)"

    if len(names[name]["Skills"]) > 1:
        extra_text += "_" + str(id)

    return name + extra_text


#Saves the the resulting wikia page, taking duplicate names into consideration
def save_stuff(id, name, type_key, output_path, output_data):
    name = sane_file_name(name).strip()
    extra_text = ""

    if len(names[name].keys()) > 1:
        if type_key == "Enemies":
            extra_text = "(Enemy)"
        else:
            extra_text = "(%s)" % type_key.rstrip("s")

    if len(names[name][type_key]) > 1:
        extra_text += "_" + str(id)

    test = name + extra_text + ".txt"
    write_folder = os.path.join(output_path, name)

    #Write parent plain name folder
    if not os.path.exists(write_folder):
        os.makedirs(write_folder)

    if os.path.exists(os.path.join(write_folder, (name + extra_text + ".txt"))):
        #Shit one already exists
        pass

    with open(os.path.join(write_folder, (name + extra_text + ".txt")), "w") as the_file:
        the_file.write(output_data)


def sane_file_name(name):
    return "".join([c for c in name if c.isalpha() or c.isdigit() or c == ' ']).rstrip().strip()


def update_progress(current, total):
    #print('\r[{0}] {1}%'.format('#'*(progress/10), progress))
    percentage = current / total
    total_icons = 20

    icons = int(total_icons * percentage)
    filler = total_icons - icons

    #print('\r[{0}{1}] {2}%'.format('#'*int((progress/10)), ''*int((progress/10))progress))
    text = '\r[{0}{1}] {2}/{3} {4}%'.format('#' * icons, ' ' * filler, current, total, int(percentage * 100))
    sys.stdout.write(text)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
    print("\n\n\n")