
 
# Output: 2

# longest substring without repeating characters

# height = [1,8,6,2,5,4,8,3,7]

intervals =  [[9,16],[6,16],[1,9],[3,15]]
intervals.sort(key=lambda x:(x[1],-x[0]))
print(intervals)
output = 1 if (len(intervals) > 0) else 0
for k in range(len(intervals) - 1):
    
    nextItem = intervals[k+1][0]
    currentEnd = intervals[k][1]
    if (currentEnd > nextItem):
        output += 1
print(output)