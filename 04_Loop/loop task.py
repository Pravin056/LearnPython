for i in range(5):
    i += 1
    if i == i:
        print(i, "KM Reached")
        a = input("Are you tired : ")
        if a == "yes":
            print("Take a break")
            break
        if a == "no":
            continue
else:
    print("You Win")
