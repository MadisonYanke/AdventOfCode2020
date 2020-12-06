def yesAnswerCount(answerGroup, unique=True):
    answerSet = [set(answer) for answer in answerGroup if set(answer) != set()]
    if unique: return len(set.union(*answerSet))
    else: return len(set.intersection(*answerSet))

answerGroups = [group.split('\n') for group in open('day6input.txt').read().split('\n\n')]

print(sum([yesAnswerCount(group) for group in answerGroups]))
print(sum([yesAnswerCount(group, False) for group in answerGroups]))