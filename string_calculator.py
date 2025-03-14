import re

def add(nums: str) -> int:
    if not nums:
        return 0
    
    # check the string for delimeters, extract regex pattern for those delimeters and then split the nums such that our resultant output is just the numbers to be added
    if nums.startswith("//"):
        delimiters, nums = nums[2:].split("\n", 1)
        delimiters = re.findall(r"\[([^\]]+)\]", delimiters) or [delimiters]
        pattern = "|".join(map(re.escape, delimiters))
        nums = re.split(pattern, nums)
    else:
        nums = re.split("[,\n]", nums)

    nums_list = [int(n) for n in nums if int(n) <= 1000]

    return sum(nums_list)