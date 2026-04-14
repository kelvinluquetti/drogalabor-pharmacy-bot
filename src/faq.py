class FAQ:
    def __init__(self):
        # Example FAQ database
        self.faq_data = {
            "What are your opening hours?": "We are open from 9 AM to 9 PM every day.",
            "Where are you located?": "We are located at 123 Pharmacy St, Your City.",
            "Do you offer delivery services?": "Yes, we offer delivery services within a 5-mile radius.",
        }

    def search(self, question):
        """Search for an FAQ answer based on the question asked."""
        response = self.faq_data.get(question)
        if response:
            return response
        else:
            return "I'm sorry, I don't have the answer to that question."

# Example usage
if __name__ == "__main__":
    faq = FAQ()
    question = "What are your opening hours?"
    print(faq.search(question))
