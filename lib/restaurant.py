from review import Review
class Restaurant:

    all_restaurants=[]
    
    def _init_(self, name):
        self.name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self, name):
        return self.name
    
    # Object Relationship Methods
    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        new_customers = set()
        for review in self._reviews:
            new_customers.add(review.customer())
        return list(new_customers)


# Aggregate and Association Methods
    def average_star_rating(self):
        if len(self._reviews) == 0:
            return 0
        total_ratings = sum(review.rating() for review in self._reviews)
        return total_ratings / len(self._reviews)
    



#Test-case
restaurant = Restaurant("Max-brunch")
review = Review("Maxy", restaurant, 9)
restaurant.add_review(review)

# Print details of the latest review
latest_review = restaurant.reviews()[-1]
print("Customer:", latest_review.customer)
print("Restaurant:", latest_review.restaurant.name)
print("Rating:", latest_review.rating)

# Print average star rating
print("Average star rating:", restaurant.average_star_rating())