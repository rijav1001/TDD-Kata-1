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

    # create an array nums_list consisting only the extracted numbers string, and convert the string to int, make sure to ignore the numbers > 1000
    nums_list = [int(n) for n in nums if int(n) <= 1000]

    # check for negative values
    negatives = [int(n) for n in nums if int(n) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

    return sum(nums_list)