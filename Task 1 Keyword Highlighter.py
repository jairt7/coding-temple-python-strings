# 1. Task 1: Keyword Highlighter

def keyword_highlighter(reviews, keywords):
    result = []
    for review in reviews:
        for keyword in keywords:
            if keyword in review.lower():
                new_review = review.replace(keyword, keyword.upper())
                new_review_2 = new_review.replace(keyword.capitalize(), keyword.upper())
                result.append(new_review_2)            
    return result

keywords = ["good", "excellent", "bad", "poor", "average"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

capitalized_reviews = keyword_highlighter(reviews, keywords)

for review in capitalized_reviews:
    print(review)