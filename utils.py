import json

def load_json(json_path):
    with open(json_path, 'r') as file:
        json_dct = json.load(file)

    return json_dct

# diperbolehkan untuk mengubah fungsi ini sesuai kebutuhan
def format_report(name, id, performances):
    performance_report =  f"""
{name} - {id}
---------- lev_trie ----------
best accuracy: {performances['lev_trie']['best_acc']}
candidate accuracy: {performances['lev_trie']['cand_acc']}
time: {performances['lev_trie']['time']} seconds
---------- dalev_trie ----------
best accuracy: {performances['dalev_trie']['best_acc']}
candidate accuracy: {performances['dalev_trie']['cand_acc']}
time: {performances['dalev_trie']['time']} seconds
---------- lev_dict ----------
best accuracy: {performances['lev_dict']['best_acc']}
candidate accuracy: {performances['lev_dict']['cand_acc']}
time: {performances['lev_dict']['time']} seconds
---------- dalev_dict ----------
best accuracy: {performances['dalev_dict']['best_acc']}
candidate accuracy: {performances['dalev_dict']['cand_acc']}
time: {performances['dalev_dict']['time']} seconds
"""

    return performance_report