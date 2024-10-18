"""
Quest status

Fantasy Quest needs a way to check the status of individual character's quest status. The game stores each character's progress in a nested data structure, and your job is to fetch the status of a particular quest.

Here's the structure of a progress dictionary:

{
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
}

Assignment

Complete the get_quest_status function. It accepts a progress dictionary and returns the character's status in the "Dragon_Slayer" quest. Chain the keys to access the nested data.
Hint

If the value retrieved from a dictionary is itself a dictionary, how would you access its values?
"""

def get_quest_status(progress):

    try:
        quest = progress["entity"]["character"]["quests"]["Dragon_Slayer"]["status"]
    except KeyError:
        quest = None
    return quest


"""
---------------------------------
Inputs:
 * Progress Dictionary: {'entity': {'character': {'name': 'Sir Galahad', 'quests': {'Dragon_Slayer': {'status': 'In Progress'}, 'Goblin_Hunter': {'status': 'Completed'}}}}}
Expecting: In Progress
Actual: In Progress
Pass
---------------------------------
Inputs:
 * Progress Dictionary: {'entity': {'character': {'name': 'Lady Gwen', 'quests': {'Dragon_Slayer': {'status': 'Completed'}, 'Goblin_Hunter': {'status': 'In Progress'}}}}}
Expecting: Completed
Actual: Completed
Pass
---------------------------------
Inputs:
 * Progress Dictionary: {'entity': {'character': {'name': 'Archer Finn', 'quests': {'Dragon_Slayer': {'status': 'Not Started'}, 'Goblin_Hunter': {'status': 'Completed'}}}}}
Expecting: Not Started
Actual: Not Started
Pass
---------------------------------
Inputs:
 * Progress Dictionary: {'entity': {'character': {'name': 'Mage Elara', 'quests': {'Dragon_Slayer': {'status': 'Failed'}, 'Goblin_Hunter': {'status': 'Completed'}}}}}
{'status': 'Completed'}}}}}
Expecting: Failed
Actual: Failed
Pass
---------------------------------
Inputs:                                                                                                                                    r': {'status': 'Not Started'}}}}}
 * Progress Dictionary: {'entity': {'character': {'name': 'Rogue Talon', 'quests': {'Dragon_Slayer': {'status': 'Completed'}, 'Goblin_Hunter': {'status': 'Not Started'}}}}}
Expecting: Completed
Actual: Completed
Pass
============= PASS ==============
5 passed, 0 failed
"""