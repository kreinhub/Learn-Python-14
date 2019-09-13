scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [3,2,2,5,2]},{'school_class': '4c', 'scores': [4,5,4,5,2]}]

sum_scores = 0
for i in scores:
    sum_scores += sum(i["scores"])

    avg = sum(i["scores"])/len(i["scores"])
    class_number = i["school_class"]
    print(f"Average score of {class_number} class is {avg}")

avg_common = sum_scores/len(scores)
print(f"Common average score is {avg_common}")