def simple_chatbot(user_query):
    if user_query == "What is the total revenue for 2025?":
        return "In 2025, Apple reported total revenue of 416161, Microsoft reported 281724, and Tesla reported 94827."
    
    elif user_query == "How has net income changed from 2024 to 2025?":
        return (
            "From 2024 to 2025, Microsoft’s net income increased from 88136 to 101832. "
            "Apple’s net income increased from 93736 to 112010. "
            "Tesla’s net income decreased from 7091 to 3794."
        )
    
    elif user_query == "Which company had the highest revenue in 2025?":
        return "Apple had the highest revenue in 2025 with 416161."
    
    elif user_query == "Which company had the highest net income in 2025?":
        return "Apple had the highest net income in 2025 with 112010."
    
    else:
        return "Sorry, I can only provide information on predefined queries."


if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    print("You can ask one of the predefined questions.")
    user_input = input("Enter your question: ")
    response = simple_chatbot(user_input)
    print(response)