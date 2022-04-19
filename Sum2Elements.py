def Sum2Elements():
    count,x,y = False, 0, 0
    nums = [ int(x) for x in input("nums = ").split(",")]
    sum = input("sum = ")
    
    print("Input: nums = ",nums,", sum = ",sum)
    for x in range(len(nums)):
        for y in range(x,len(nums)):
            if x!=y:
                if (nums[x]+nums[y])== int(sum):
                    count = True
                    return count,x,y,sum
    return count,x,y,sum

count,x,y,sum = Sum2Elements()
if count==True:
    print("Output: ",x,",",y)
    print("Explanation: Because nums[",x,"] + nums[",y,"] = ",sum)
else:
    print("Output: no output")
    print("Explanation: The are no two numbers that add up to ",sum)

