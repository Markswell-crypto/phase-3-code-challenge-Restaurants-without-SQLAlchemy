from review import Review
from restaurant import Restaurant
class Customer:
    all_customers = []

    def _init_(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def get_full_name(self):
        return f'{self.given_name} {self.family_name}'

    def all(self):
        return Customer.all_customers

    # Object Relationship Methods
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    def restaurants(self):
        reviewed_restaurants = set()
        for review in self._reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    # Aggregate and Association Methods
    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls.all_customers:
            if customer.get_full_name() == full_name:
                return customer
            else:
                return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.get_given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers


# Example usage:
# Create a customer
customer1 = Customer("Joyce", "Mwangi")

# Access customer information
given_name = customer1.get_given_name()
family_name = customer1.get_family_name()
full_name = customer1.get_full_name()

# Print customer details
print("Given Name:", given_name)
print("Family Name:", family_name)
print("Full Name:", full_name)