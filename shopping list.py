budget=3000
print(budget,"your total budget")
item_list={"shampo":300,"oil":600, "register":400,"shoes":800,"dress":1800}
total_budget=sum(item_list.values())
print(total_budget)
if total_budget<=budget:
    print("your shopping is in range of your budget")
else:
    print("your shopping is out of your budget range")    