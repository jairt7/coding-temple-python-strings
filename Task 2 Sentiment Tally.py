# 1. Task 2: Sentiment Tally
def count_words(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    p_total = 0
    n_total = 0
    for string in reviews:
        string = string.lower()
        for word in positive_words:
            p_count = string.count(word)
            p_total += p_count
        for word in negative_words:
            n_count = string.count(word)
            n_total += n_count
    print("There are", p_total, "positive words, and", n_total, "negative words.")
        

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

count_words(reviews)