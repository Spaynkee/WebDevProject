from ast import literal_eval

def clean_abilities(abils):
    abil_list = literal_eval(abils)
    abilities = ''
    if abil_list:
        for item in abil_list:
            ability = item
            ability = ability.replace("['", "")
            ability = ability.replace('["', "")
            ability = ability.replace("', '", "<br />")
            ability = ability.replace("', \"", "<br />")
            ability = ability.replace('", \'', "<br />")
            ability = ability.replace('", "', "<br />")
            ability = ability.replace("\\'", "'")
            ability = ability.replace("']", "")
            ability = ability.replace('"]', "")
            ability = ability.replace("'{", "{")
            ability = ability.replace("{T}", "<img class='symbol' src='/static/img/tap.png'></img>")
            ability = ability.replace("{W}", "<img class='symbol' src='/static/img/White.png'></img>")
            ability = ability.replace("{R}", "<img class='symbol' src='/static/img/Red.png'></img>")
            ability = ability.replace("{G}", "<img class='symbol' src='/static/img/Green.png'></img>")
            ability = ability.replace("{B}", "<img class='symbol' src='/static/img/Black.png'></img>")
            ability = ability.replace("{U}", "<img class='symbol' src='/static/img/Blue.png'></img>")
            for i in range(0, 9):
                ability = ability.replace("{%s}" % str(i), "<span class='badge' style='padding: 4px; padding-top: 1px; padding-bottom: 1px;'>%s</span>" % str(i))

            abilities += ability + "<br />"
    return abilities.strip()

def clean_cost(cost):
    if cost:
        cost_string = cost
        cost_string = cost_string.replace("W", "<img class='symbol' src='/static/img/White.png'></img>")
        cost_string = cost_string.replace("R", "<img class='symbol' src='/static/img/Red.png'></img>")
        cost_string = cost_string.replace("G", "<img class='symbol' src='/static/img/Green.png'></img>")
        cost_string = cost_string.replace("B", "<img class='symbol' src='/static/img/Black.png'></img>")
        cost_string = cost_string.replace("U", "<img class='symbol' src='/static/img/Blue.png'></img>")
        cost_string = cost_string.replace("X", '<span class="badge">X</span>')
        
        for i in range(0, 9):
            if not cost_string.find(str(i)):               
                cost_string = cost_string.replace("%s" % str(i), "{%s}" % str(i))
                
        for i in range(0, 9):
            cost_string = cost_string.replace("{%s}" % str(i), '<span class="badge">%s</span>' % str(i))

        return cost_string
