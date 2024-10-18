"""
Vendor

Fantasy Quest players want a way to track what items they purchased from the vendor, how much it cost, and what they still need to purchase from their tracked items list.
Assignment

Complete the calculate_total function.
Inputs

    items_purchased: A list of the names of items purchased. This is a list of strings.
    pinned_list: A list of the names of items the player has 'pinned' and wanted to purchase. This is also a list of strings.

Outputs

The function should return 3 values in this order:

    unpurchased_items: A list of all the item names in pinned_list that weren't found in items_purchased in order.
    receipt: A dictionary containing all the items the player purchased, even stuff not on their pinned_list. The keys are the item names and the values are their respective prices from the item_prices dictionary.
    total: The total cost of all the items that were purchased.

Return each value separately, not in a list. For example:

return item1, item2, item3

Tip

You can combine the not negation keyword with in membership operator: if item not in some_list:
"""

def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line
    unpurchased_items = []
    receipt = {}
    total = 0
        
    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)        
    
    for item in items_purchased:
        receipt[item] = item_prices[item]

    for cost in receipt:
        total += receipt[cost]

    return unpurchased_items, receipt, total


"""
---------------------------------
Inputs: (['health_potion', 'mana_potion', 'gold_dust', 'herbs', 'crystal_shard', 'dwarven_ale'], ['health_potion', 'mana_potion', 'ice_cold_milk', 'gold_dust', 'herbs', 'crystal_shard', 'magic_ring', 'dwarven_ale', 'mystic_amulet'])
Expecting: (['ice_cold_milk', 'magic_ring', 'mystic_amulet'], {'health_potion': 10.0, 'mana_potion': 12.0, 'gold_dust': 5.0, 'herbs': 7.0, 
'crystal_shard': 20.0, 'dwarven_ale': 8.0}, 62.0)
Actual: (['ice_cold_milk', 'magic_ring', 'mystic_amulet'], {'health_potion': 10.0, 'mana_potion': 12.0, 'gold_dust': 5.0, 'herbs': 7.0, 'crystal_shard': 20.0, 'dwarven_ale': 8.0}, 62.0)
Pass
---------------------------------
Inputs: (['health_potion', 'gold_dust', 'herbs', 'crystal_shard'], ['health_potion', 'mana_potion', 'gold_dust', 'ice_cold_milk', 'herbs', 
'magic_ring', 'crystal_shard', 'mystic_amulet'])
Expecting: (['mana_potion', 'ice_cold_milk', 'magic_ring', 'mystic_amulet'], {'health_potion': 10.0, 'gold_dust': 5.0, 'herbs': 7.0, 'crystal_shard': 20.0}, 42.0)
Actual: (['mana_potion', 'ice_cold_milk', 'magic_ring', 'mystic_amulet'], {'health_potion': 10.0, 'gold_dust': 5.0, 'herbs': 7.0, 'crystal_shard': 20.0}, 42.0)
Pass
---------------------------------
Inputs: (['health_potion', 'mana_potion', 'gold_dust', 'ice_cold_milk', 'herbs', 'magic_ring', 'crystal_shard', 'mystic_amulet'], ['health_potion', 'gold_dust', 'herbs', 'crystal_shard'])
Expecting: ([], {'health_potion': 10.0, 'mana_potion': 12.0, 'gold_dust': 5.0, 'ice_cold_milk': 50.0, 'herbs': 7.0, 'magic_ring': 100.0, 'crystal_shard': 20.0, 'mystic_amulet': 150.0}, 354.0)
Actual: ([], {'health_potion': 10.0, 'mana_potion': 12.0, 'gold_dust': 5.0, 'ice_cold_milk': 50.0, 'herbs': 7.0, 'magic_ring': 100.0, 'crystal_shard': 20.0, 'mystic_amulet': 150.0}, 354.0)
Pass
============= PASS ==============
3 passed, 0 failed
"""