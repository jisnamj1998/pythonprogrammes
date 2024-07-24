players={"sachin","dravid","laxman","jadeja","dhoni","raina"}
dhoni_frnds={"sachin","raina"}
suggestion_set=players.difference(dhoni_frnds)
suggestion_set.discard("dhoni")
print(suggestion_set)


all_students={"jithin","jilu","jisna","jibin","jerin","jeffin","jeeva"}
passed_students={"jithin","jilu"}
failed_students=all_students.difference(passed_students)
print(failed_students)
