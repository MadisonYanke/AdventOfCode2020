import re

def getPossibilities(bag, bagRules):
    possibilities = []
    for bagRule in bagRules:
        if bag in bagRule[1]:
            possibilities.append(bagRule[0].strip())
            possibilities += getPossibilities(bagRule[0].strip(), bagRules)
    return possibilities

def getNumberOfBagsInside(bag, bagRules):
    numberOfInnerBags = 0
    for bagRule in bagRules:
        if bag in bagRule[0]:
            if 'no other' in bagRule[1]: return 0
            for innerBag in bagRule[1].split(','):
                numberOfInnerBag = int(re.search(r'\d+', innerBag).group(0))
                innerBagColor = re.sub(r'\d+|[.]', '', innerBag).strip()
                numberOfInnerBags += numberOfInnerBag * getNumberOfBagsInside(innerBagColor, bagRules) + numberOfInnerBag
    return numberOfInnerBags

bagRules = [line.strip().replace('bags','').replace('bag','') for line in open('day7input.txt')]
bagRules = [rule.split('contain') for rule in bagRules]

print(len(set(getPossibilities('shiny gold', bagRules))))
print(getNumberOfBagsInside('shiny gold', bagRules))

bagRulesSmall = [line.strip().replace('bags','').replace('bag','') for line in open('day7small.txt')]
bagRulesSmall = [rule.split('contain') for rule in bagRulesSmall]

print(len(set(getPossibilities('shiny gold', bagRulesSmall))))
print(getNumberOfBagsInside('shiny gold', bagRulesSmall))