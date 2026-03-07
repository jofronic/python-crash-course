from restaurant import Restaurant as R

food = R('mcdonalds', 'burger')
food.describe_restaurant()
food.restaurant_name = 'popeyes'
food.describe_restaurant()