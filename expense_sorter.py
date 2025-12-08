def get_expensive_prices(items): 
    expensive=[]
    for item in items:
        if item>100:
            expensive.append(item)
    return expensive    



prices=[120,45, 300, 85, 150]
print(get_expensive_prices(prices))