# سوال: قطعه کدی که از نظر زمانی و مکانی ناکارآمد است، بهینه‌سازی کنید.

# فرض کنیم یک حلقه تودرتو داریم که بهینه نیست:
def inefficient_function(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j]:
                print(data[i])


# بهینه ‌سازی شده:
def optimized_function(data):
    unique_data = set(data)
    for item in unique_data:
        print(item)
