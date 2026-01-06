def recommend(user_history, items):
    recommendations = []

    for item in items:
        if item not in user_history:
            recommendations.append(item)

    return recommendations

def main():
    user_history = ["Python", "JavaScript"]
    all_items = ["Python", "Java", "C++", "JavaScript", "Go"]

    result = recommend(user_history, all_items)

    print("User history:", user_history)
    print("Recommended items:")
    for item in result:
        print("-", item)

if __name__ == "__main__":
    main()
