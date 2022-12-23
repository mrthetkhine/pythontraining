words = ["Python","Java","JavaScript","Go"]
#[(word,length)]

tuple_list =[ (word,len(word)) for word in words if len(word)>2]
print("Tuple list ",tuple_list)