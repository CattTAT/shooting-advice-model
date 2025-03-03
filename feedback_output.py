form_feedback = [
    "Forearm insufficient pushing power/ or release arm pulling too much",
    "Forearm pushing too much/ or release arm insufficient pulling power",
    "Anchor point or string shadow too left",
    "Anchor point or string shadow too right",
    "Arrow release motion should continue moving backwards",
    "Mind the head alignment and maintain the same posture",
    "Maintain the elbow at the line of force",
    "Mind the consistency between each arrows"
]

equip_feedback = [
    "Sight adjust to the left slightly",
    "Sight adjust to the left moderately",
    "Sight adjust to the left significantly",
    "Sight adjust to the right slightly",
    "Sight adjust to the right moderately",
    "Sight adjust to the right significantly",
    "Sight adjust downward slightly",
    "Sight adjust downward moderately",
    "Sight adjust downward significantly",
    "Sight adjust upward slightly",
    "Sight adjust upward moderately",
    "Sight adjust upward significantly",
    "Sight adjustment is not necessary"
]

def get_form_feedback(ids):
    return [form_feedback[id] for id in ids]

def get_equip_feedback(ids):
    return [equip_feedback[id] for id in ids]
