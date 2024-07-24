set1={10,20,30,40,50}
set2={20,30,40,90,80}

#union()
union_set=set1.union(set2)
print(union_set)

#intersection()
intersection_set=set1.intersection(set2)
print(intersection_set)

#difference()
difference_set=set1.difference(set2)
print(difference_set)
difference_set2=set2.difference(set1)
print(difference_set2)