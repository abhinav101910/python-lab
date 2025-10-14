n=int(input("Enter total number of choice:"))
print("Enter colors")
for i in range(n):
    ch=input()
    color.append(ch)
    print(f"first color is:{color[0]}\nLast color is:{color[-1]}")
