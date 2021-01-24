import json

roll_odds = [[1, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0], 
            [.75, .25, 0, 0, 0],
            [.55, .3, .15, 0, 0],
            [.45, .33, .2, .02, 0],
            [.35, .35, .25, .05, 0],
            [.22, .35, .3, .12, .01],
            [.15, .25, .35, .2, .05],
            [.1, .15, .3, .3, .15]]
#champions_count = [29, 22, 18, 12, 10]
champions_path = 'champions.json'
champions_dict = {}
traits_dict = {}

def parse():
    champions_list = []
    with open(champions_path, 'r') as c:
        champions_list = json.load(c)
    for entry in champions_list:
        champion = entry['name'].lower()
        champions_dict[champion] = {}
        champions_dict[champion]['cost'] = entry['cost']
        champions_dict[champion]['traits'] = entry['traits']
        for trait in entry['traits']:
            if trait not in traits_dict.keys():
                traits_dict[trait] = []
            traits_dict[trait].append(champion)

parse()

def get_cost(champion):
    return champions_dict[champion]['cost']

def get_traits(champion):
    return champions_dict[champion]['traits']

def get_total_count_by_cost(candidates):
    counts = [0, 0, 0, 0, 0]
    for candidate in candidates:
        cost = get_cost(candidate)
        counts[cost - 1] = counts[cost - 1] + 1
    return counts

def get_candidates(champion):
    traits = get_traits(champion)
    candidates = []
    for trait in traits:
        candidates.extend(traits_dict[trait])
    candidates = set(candidates)
    return candidates

def use_simple(level, champion):
    parse()
    odds = roll_odds[level - 1]
    candidates = get_candidates(champion)
    counts = get_total_count_by_cost(candidates)
    results = []
    for candidate in candidates:
        candidate_cost = get_cost(candidate)
        probability = odds[candidate_cost - 1] / counts[candidate_cost - 1]
        results.append((candidate, probability))
    results.sort(key = lambda x: x[1], reverse=True)
    return results


def roll_simple(level, champion):
    parse()
    candidates = get_candidates(champion)
    results = []
    for candidate in candidates:
        probabilities = use_simple(level, candidate)
        print(candidate)
        print(probabilities)
        for probability in probabilities:
            if probability[0] == champion:
                results.append((candidate, probability[1]))
    results.sort(key = lambda x: x[1], reverse=True)
    return results