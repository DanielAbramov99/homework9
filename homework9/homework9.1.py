temp_list: list[float] = []
temp_list1: list[float] = [-20.0, 39.1, 18.5]
stop: int = -999
while True:
    temperature: float = float(input("enter temperature:"))
    if temperature == stop:
        break
    if not -50 < temperature < 50:
        continue
    temp_list.append(temperature)
temp_list.extend(temp_list1)
copy_temp = temp_list.copy()
copy_temp.sort()
print(f"after sort:{copy_temp}")
copy_temp_reverse = temp_list.copy()
copy_temp_reverse.sort(reverse=True)
print(f"after sort:{copy_temp_reverse}")
print(temp_list)
print(f"the maximum temperature input is:{max(temp_list)}")
print(f"the minimum temperature input is:{min(temp_list)}")
print(f"the average temperature is:{sum(temp_list) / len(temp_list)}")
if 18.5 in temp_list:
    print("True")
else:
    print("False")
count_20 = temp_list.count(-20)
print(f" the amount of temperature inputs that is -20 are:{count_20}")
for temperature in temp_list:
    print(temperature)
index_number = temp_list.index(39.1)
print(f"the number of index of temperature 39.1 is:{index_number}")
del temp_list[0]
del temp_list[1::2]
print(f" temperature list after removing the firs index and all even indexes as well:{temp_list}")
# you should check if index that you want to remove is in the list in the first place and wasn't removed before because otherwise the code may crash.
if 18.5 in temp_list:
    temp_list.remove(18.5)
print(f" 18.5 is removed from the temperature list,{temp_list}")
temp_last: float = temp_list.pop()
print(f"the temperature removed is:{temp_last}")
print(f"the temperature list after removal is:{temp_list}")
