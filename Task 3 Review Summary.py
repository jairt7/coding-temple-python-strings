# Task 3: Review Summary

def first_thirty(reviews):
    
    for review in reviews:
        less_than_thirty = True
        character_index = 30
        while less_than_thirty:
            if review[character_index] != ' ':
                character_index += 1
            else:
                less_than_thirty = False
                review = review[:character_index]
                print(review + "...")

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

first_thirty(reviews)