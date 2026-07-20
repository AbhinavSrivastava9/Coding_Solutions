def say_hello(name):
    print("Hello , Welcome back to function",name)

say_hello("Abhinav")


t = tuple()

print(t)

t1 = ("Abhinav","Pusphendra","AKshat")
print(t1)

t2 = ["Abhinav","Viraj","Pushpendra","Sachin"]
print(tuple(t2))
print(t2[0])
print(t2[-1])
print("Sachin" in t2)

new_tuple = list(t2)
print(type(new_tuple))
print(new_tuple)

new_tuple.append("Akshat")
print(new_tuple)

new_tuple2 = tuple(new_tuple)
print(new_tuple2)





