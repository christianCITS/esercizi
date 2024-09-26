quest = [0]
risp = []
med = []

with open("quiz.json", "r") as file:
    content = json.load(file)

def question_counter(data, root, quest, risp, med):

    if type(data) is dict:

        for keys, value in data.items():

            if keys == "question":

                quest[0] += 1

            if keys == "options":
                for risp in value:
                    risp.append(risp)

            if keys == "maths":
                for d in data["maths"].values():
                    for q in d.items():
                        for c in q:
                            if type(c) is list:
                                for i in c:
                                    med.append(i)

            if type(data[keys]) is dict:

                if root != "":
                    question_counter(f"{data[keys]} {root}.{keys} {quest} {risp} {med}")

                else:
                    question_counter(f"{data[keys]} {keys} {quest} {risp} {med}")

            if type(data[keys]) is list:

                if root != "":
                    question_counter(f"{data[keys]} {root}.{keys} {quest} {risp} {med}")

                else:
                    question_counter(f"{data[keys]} {keys} {quest} {risp} {med}")


question_counter(content, "", quest, risp, med)

print(f"Numero di domande: {quest[0]}\nLa media delle risposte è: {len(risp) / quest[0]}\n Domande di matematica: {len(med)}")