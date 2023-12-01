from customer import Customer
from restaurant import Restaurant
class Review(Customer, Restaurant):

    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

