class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_name = customer
        self.restaurant_name = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    def customer(self):
        return self.customer_name

    def restaurant(self):
        return self.restaurant_name

    @classmethod
    def all(cls):
        return cls.all_reviews


# Test-case:
customer1 = "Maxy"
restaurant1 = "Max-brunch"
rating1 = 4

review1 = Review(customer1, restaurant1, rating1)

print(review1.customer())  # Output: Maxy
print(review1.restaurant())  # Output: Max-brunch
print(review1.rating())  # Output: 4
