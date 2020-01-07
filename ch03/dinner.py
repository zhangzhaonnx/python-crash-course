guests = ['薛云峰','谢召飞','王灿','马楠']
print("邀请 " + str(guests) + " 共进晚餐")

busy_guest = guests.pop(2)
print("嘉宾 " + busy_guest + " 无法赴约")
guests.append('刘小龙')
print("邀请 " + str(guests) + " 共进晚餐")

print("找到了一个更大的餐桌")
guests.insert(0, '牛群')
guests.insert(2, '郭星')
guests.append('王平')
print("邀请 " + str(guests) + " 共进晚餐")

print("只能邀请两位嘉宾共进晚餐")
guest = guests.pop()
print(guest + "，很抱歉，无法邀请你来共进晚餐")
guest = guests.pop()
print(guest + "，很抱歉，无法邀请你来共进晚餐")
guest = guests.pop()
print(guest + "，很抱歉，无法邀请你来共进晚餐")
guest = guests.pop()
print(guest + "，很抱歉，无法邀请你来共进晚餐")
guest = guests.pop()
print(guest + "，很抱歉，无法邀请你来共进晚餐")
print(guests[0] + "，你依然在受邀之列")
print(guests[1] + "，你依然在受邀之列")
del guests[0]
del guests[0]
print("邀请 " + str(guests) + " 共进晚餐")
