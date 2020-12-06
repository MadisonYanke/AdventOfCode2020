def yesAnswerCount(answerGroup, unique=True):
    answerSet = [set(answer) for answer in answerGroup if set(answer) != set()]
    if unique: return len(set.union(*answerSet))
    else: return len(set.intersection(*answerSet))

answerGroups = [group.split('\n') for group in open('day6input.txt').read().split('\n\n')]
uniqueYesAnsers = []
allYesAnswers = []
for answerGroup in answerGroups:
    uniqueYesAnsers.append(yesAnswerCount(answerGroup))
    allYesAnswers.append(yesAnswerCount(answerGroup, False))

print(sum(uniqueYesAnsers))
print(sum(allYesAnswers))