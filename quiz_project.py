import json

with open("questions.json", 'r')as file:
    content = file.read()

data = json.loads(content)
score = 0
print("Quiz")
print("Total five Mcqs")
for index,question in enumerate(data):
    print("Q", index + 1, ":",question["question_text"])
    for index,alternatives in enumerate(question["alternatives"]):
        print(index + 1,  "-", alternatives)
    user_choice = int(input("Enter the answere: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answere"]:
        score = score + 1
        result = "correct answere"
        print(result)
    else:
        result = "wrong answere"
        print(result)

for index,question in enumerate(data):
    message = "Your answere: " ,question['user_choice']," correct answere: ",question['correct_answere']
    print(index + 1 ,"-", message)

# print(data)
print("score: ", score, "/", len(data))