import streamlit as st
import difflib
import string

knowledge_base = {
    "what is photosynthesis": "Photosynthesis is the process by which plants make their food using sunlight.",
    "define gravity": "Gravity is a force that attracts two bodies toward each other.",
    "what is newton's first law": "Newton's first law states that an object remains at rest or in uniform motion unless acted upon by a force.",
    "what is electricity": "Electricity is the flow of electric charge through a conductor.",
    "what is the pythagorean theorem": "In a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides.",
    "what is the boiling point of water": "Water boils at 100 degrees Celsius under normal atmospheric pressure.",
    "what is an atom": "An atom is the smallest unit of ordinary matter that forms a chemical element.",
    "who discovered penicillin": "Penicillin was discovered by Alexander Fleming in 1928.",
    "what is the earth's atmosphere made of": "Earth's atmosphere is made of nitrogen (78%), oxygen (21%), and other gases.",
    "what is the formula of water": "The chemical formula of water is H2O.",
    "what causes tides": "Tides are caused mainly by the gravitational pull of the moon and the sun on Earth's oceans.",
    "what is acceleration": "Acceleration is the rate of change of velocity of an object.",
    "what is force": "Force is any interaction that, when unopposed, changes the motion of an object.",
    "what is energy": "Energy is the capacity to do work.",
    "what is the speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "who is isaac newton": "Isaac Newton was a physicist and mathematician who formulated the laws of motion and universal gravitation.",
    "what is evolution": "Evolution is the process by which different kinds of living organisms developed and diversified from earlier forms.",
    "what is an ecosystem": "An ecosystem is a community of interacting organisms and their physical environment.",
    "what is climate change": "Climate change refers to long-term changes in temperature, precipitation, and other atmospheric conditions on Earth.",
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What would you like to learn about?",
    "hey": "Hey! Ask me anything about your studies.",
    "how are you": "I'm just a bot, but I'm here to help you learn!",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "No problem! Feel free to ask more questions.",
    "bye": "Goodbye! Keep up the great work with your studies!",
    "goodbye": "See you later! Don't hesitate to come back with questions.",
    "what is your name": "I am StudyBot, your friendly study assistant.",
}

def preprocess(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def find_best_answer(question):
    question = preprocess(question)
    all_questions = knowledge_base.keys()
    matches = difflib.get_close_matches(question, all_questions, n=1, cutoff=0.5)
    if matches:
        return knowledge_base[matches[0]]
    else:
        return "Sorry, I don't have an answer for that yet. Can you try asking differently?"

def main():
    st.title("StudyBot: Friendly Study Chatbot")
    st.write("Ask me any study-related question or say hello!")

    # Input text box
    user_input = st.text_input("You:", "")

    if user_input:
        answer = find_best_answer(user_input)
        st.markdown(f"**Bot:** {answer}")

if __name__ == "__main__":
    main()
