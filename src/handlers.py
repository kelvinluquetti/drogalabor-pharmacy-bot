def handle_inquiry(inquiry):
    """
    Process customer inquiries and provide appropriate responses.
    
    Parameters:
    inquiry (str): The customer's inquiry string.
    
    Returns:
    str: Response message to the customer.
    """
    # Example inquiry processing logic
    if "hours" in inquiry.lower():
        return "Our pharmacy is open from 9 AM to 9 PM, Monday to Saturday."
    elif "location" in inquiry.lower():
        return "We are located at 123 Pharmacy Lane, Health City."
    else:
        return "Thank you for reaching out! Please provide more details."


def handle_faq(question):
    """
    Provide answers to frequently asked questions.
    
    Parameters:
    question (str): The FAQ question.
    
    Returns:
    str: Answer to the FAQ question.
    """
    # Example FAQ handling logic
    faqs = {
        "What payment methods are accepted?": "We accept cash, credit, and debit cards.",
        "What are the store hours?": "We are open from 9 AM to 9 PM, Monday to Saturday.",
        "Do you offer delivery services?": "Yes, we offer delivery within a 5-mile radius.",
    }
    return faqs.get(question, "Sorry, I don't have that information yet.")