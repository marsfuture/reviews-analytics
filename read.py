data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f: 
        data.append(line)
        count += 1 #等於 count = count + 1 的簡寫
        if count % 1000 == 0: #count與1000的餘數等於0
            print(len(data))
print(len(data))
print(data[0])
