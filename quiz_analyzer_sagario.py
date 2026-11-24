scores = []

for i in range(1, 6):
    score = int(input(f'enter quiz score: '))
    scores.append(score)

print(f'your score is', scores)
print(len(scores))
print(max(scores))
print(min(scores))

total_score = sum(scores)
print(f'your total score is,', total_score)
average_score = total_score / len(scores)
print(f'your average score is, {average_score:.2f}')

ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print('Ascending order:, ', ascending)
print('Descending order:, ', descending)

