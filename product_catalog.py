from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[:3])


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
print(customer_preferences) 

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    matches = product_tags.intersection(customer_tags)
    return len(matches)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            recommendations.append([match_count, product["name"]])

    recommendations.sort(reverse=True)
    return recommendations

# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_preferences)
print("Recommended Products:")
for match_count, product_name in results:
    print(f"- {product_name} ({match_count} match(es))")

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?

# For this project, I used lists, sets, loops, if statements, and intersections. 
# I started with a list because it was like a basket that let me add customers' choices one at a time.
# Afterward, I converted the list into a set, since a set is useful as it eliminates duplicate choices and makes comparisons simpler.
# To find which customer choices were also included in a product's tags,
# I used intersection() to see what the two groups had in common.
# Then I used len() to count the number of matches.
# I used a while loop to keep asking the customer for more choices until they entered N.
# I used for loops to look at each product one at a time.
# I also used an if statement so the program only kept products that had at least one match.
# Finally, I sorted the results so the products with more matches appeared first.

# 2. How might this code change if you had 1000+ products?

# If I had over 1,000 products, then I would have to find ways of making the program both faster and easier to manage.
# One idea would be to group the products according to their tags so that the program looks at the most likely matches before checking each product individually. 
# I might also keep the product details in a separate file or database, since this would make it simpler to update a large catalog.
# Another option would be to display only the top few recommendations rather than giving every matching product.
