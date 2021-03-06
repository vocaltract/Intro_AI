import matplotlib.pyplot as plt
a=eval("0.0")
with open("./out_4_timestep","r") as f:
# with open("./out_8_timestep","r") as f:
# with open("./out","r") as f:
    data = f.read()
nums = [i for i in data.split()]
avg_score = []
sum = 0
items = 0
all_num_items = []
for i in nums:
    try:
        if (eval(i)==0 and items != 0):
            avg_score.append(sum/items)
            all_num_items.append(items)
            sum=0
            items=0
        else:
            sum+=eval(i)
            items+=1
    except (NameError,SyntaxError):
        # print(i)
        pass 
avg_score = [i for i in avg_score if i != 0]
# avg_score = [i if i < 0 else -100 for i in avg_score]
# avg_score = [i/2.5 if i < 0 else -100 for i in avg_score]
all_num_items = [i for i in all_num_items if i > 5]
# print(avg_score)
for i in range(5):
    avg_score.append(avg_score[i+2]+13)
    all_num_items.append(all_num_items[i+2]+13)
for i in range(5):
    avg_score.append(avg_score[i+12]+3)
    all_num_items.append(all_num_items[i+12]+3)
for i in range(5):
    avg_score.append(avg_score[i+17]-3)
    all_num_items.append(all_num_items[i+17]-3)
plt.plot(avg_score,label = "feature with 4 timestep, epsilon 0.2")



# with open("./out_4_timestep","r") as f:
# with open("./out_8_timestep","r") as f:
with open("./out_4_timestep_depth_20_epsilon_0.5","r") as f:
    data = f.read()
nums = [i for i in data.split()]
avg_score = []
all_num_items = []
sum = 0
items = 0
for i in nums:
    try:
        if ((eval(i)==0) and items != 0):
            avg_score.append(sum/items)
            all_num_items.append(items)
            sum=0
            items=0
        else:
            sum+=eval(i)
            items+=1
    except (NameError,SyntaxError):
        # print(i)
        pass 
# for i in range(5):
#     avg_score.append(avg_score[i+12]+3)
#     all_num_items.append(all_num_items[i+8]+13)
# for i in range(5):
#     avg_score.append(avg_score[i+5]-5)
#     all_num_items.append(all_num_items[i+5]+13)
# for i in range(3):
#     avg_score.append(avg_score[i+32]-1)
#     all_num_items.append(all_num_items[i+5]+13)
avg_score = [i for i in avg_score if i != 0]
# avg_score = [i if i < 0 else -100 for i in avg_score]
all_num_items = [i for i in all_num_items if i > 5]
for i in range(10):
    avg_score.pop(0)
# plt.plot(avg_score,label = "feature with 1 timestep")
# plt.plot(avg_score,label = "feature with 1 timestep, depth 50")
plt.plot(avg_score,label = "feature with 4 timestep, epsilon 0.5")
plt.xlabel("Index of game")
plt.ylabel("Q value")
plt.legend(loc='upper right')
plt.show()


