data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f: 
        data.append(line)
        count += 1 #等於 count = count + 1 的簡寫
        if count % 1000 == 0: #count與1000的餘數等於0
            print(len(data)) #總共有幾筆留言
print("檔案讀取完了, 總共有: ", len(data), "筆資料")

sum_len = 0
for d in data:
    sum_len += len(d) #每一筆留言加起來的總長度

print('留言的平均長度是: ', sum_len/len(data), '資料')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言裡有good的單字')
print(good[1])
    

