marks= {
    "ahmad":100,
    "Armaghan":92,
    "Haris":88
    }

#print(marks.keys())
#print(marks.items())
#print(marks.values())
marks.update({"ahmad":99})
print(marks)

print(marks.get("ahmad2")) #Prints None
print(marks("ahmad")) #prints error

