# روش اول: استفاده از دیکشنری (زمان خطی)
def find_two_sum(nums, target):
    num_dict = {}
    for num in nums:
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = True
    return None

# مثال استفاده
numbers = [2, 7, 11, 15]
target = 9
result = find_two_sum(numbers, target)
print(result)  # خروجی: (2, 7)

# روش دیکشنری: در این روش با یک بار پیمایش لیست و استفاده از دیکشنری، می‌توان به سرعت جفت اعداد را پیدا کرد.

# روش دوم: مرتب‌سازی و دو اشاره‌گر (زمان خطی لگاریتمی)
def find_two_sum_sorted(nums, target):
    nums.sort()  # مرتب‌سازی لیست
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left], nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


# مثال استفاده
numbers = [3, 2, 4]
target = 6
result = find_two_sum_sorted(numbers, target)
print(result)  # خروجی: (2, 4)

# روش مرتب‌سازی: در این روش ابتدا لیست را مرتب می‌کنیم و سپس با استفاده از دو اشاره‌گر به جستجوی جفت اعداد می‌پردازیم.
