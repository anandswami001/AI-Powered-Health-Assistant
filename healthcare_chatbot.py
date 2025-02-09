import streamlit as st
from transformers import pipeline
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response logic with more information and solutions
def healthcare_chatbot(user_input):
    # Rule-based responses with detailed information and possible solutions
    if "symptom" in user_input:
        return (
            "It seems like you're experiencing symptoms. Symptoms can indicate a variety of conditions, "
            "ranging from minor illnesses to more serious issues. Please consult a doctor for accurate advice. "
            "In the meantime, rest, stay hydrated, and monitor your symptoms. If symptoms persist, seek medical attention."
        )
    elif "appointment" in user_input:
        return (
            "Would you like me to schedule an appointment with a doctor? You can book a telemedicine consultation "
            "or visit your primary care physician for an in-person appointment. Make sure to have your health insurance "
            "details ready, and don't forget to mention your symptoms and concerns."
        )
    elif "medication" in user_input:
        return (
            "It's important to take your prescribed medications regularly to ensure their effectiveness. "
            "If you're having trouble with your medication, such as side effects or difficulty adhering to the schedule, "
            "consult your doctor. They may adjust your treatment plan or recommend alternatives. Also, keep track of your medications "
            "using a medication reminder app or calendar."
        )
    elif "health tips" in user_input:
        return (
            "Stay hydrated, exercise regularly, and eat a balanced diet for better health! In addition, make sure to get enough "
            "sleep, manage stress through activities like meditation or mindfulness, and avoid smoking and excessive alcohol consumption. "
            "Small daily habits can lead to long-term improvements in your health."
        )
    elif "nutrition" in user_input or "diet" in user_input:
        return (
            "A balanced diet is key to good health. Focus on fruits, vegetables, lean proteins, and whole grains. "
            "Avoid processed foods and excess sugar. Try to include a variety of colors on your plate to ensure you're getting a range of nutrients. "
            "If you're unsure about your diet, consider consulting a registered dietitian for personalized advice."
        )
    elif "exercise" in user_input or "workout" in user_input:
        return (
            "Exercise is important for your overall health. Aim for at least 150 minutes of moderate-intensity exercise per week, "
            "such as brisk walking, cycling, or swimming. Additionally, include strength training exercises at least two days a week. "
            "If you're new to exercise, start slow and gradually increase intensity. Always listen to your body and consult a fitness professional if needed."
        )
    elif "mental health" in user_input:
        return (
            "Mental health is just as important as physical health. Practice relaxation techniques like deep breathing, meditation, "
            "or journaling to manage stress. If you're feeling overwhelmed, it’s okay to reach out to a mental health professional. "
            "Therapists can help you develop coping strategies for anxiety, depression, and other emotional struggles."
        )
    elif "fever" in user_input:
        return (
            "Fever is a common symptom that typically signals the body is fighting an infection. If the fever is mild, rest, hydrate, "
            "and monitor it closely. If it persists for more than 48 hours or is accompanied by severe symptoms like shortness of breath, "
            "chest pain, or confusion, seek medical care immediately."
        )
    elif "headache" in user_input:
        return (
            "Headaches can have many causes, from stress to dehydration to underlying conditions. Ensure you're staying hydrated, "
            "getting enough sleep, and managing stress. Over-the-counter pain relievers like ibuprofen can help, but if headaches are "
            "chronic or severe, consider seeing a healthcare provider for further evaluation."
        )
    elif "cold" in user_input or "flu" in user_input:
        return (
            "If you have flu symptoms like fever, cough, sore throat, and body aches, rest and stay hydrated. Over-the-counter "
            "medications can help relieve symptoms, but the flu typically resolves on its own within 1-2 weeks. If your symptoms "
            "worsen or you're at higher risk (e.g., elderly or immunocompromised), contact your healthcare provider for guidance. "
            "Get a flu vaccine next season to protect yourself."
        )
    elif "first aid" in user_input:
        return (
            "For basic first aid, start by assessing the situation. Clean and cover wounds to prevent infection. For burns, cool the area "
            "with running water. Apply ice to sprains or strains, and elevate the injured area if possible. In case of a medical emergency, "
            "call for professional help immediately, especially for head injuries, broken bones, or severe bleeding."
        )
    elif "stress" in user_input:
        return (
            "Managing stress is vital for both mental and physical health. Try incorporating relaxation techniques such as deep breathing, "
            "mindfulness, or yoga. Regular physical activity can also help reduce stress levels. If stress is impacting your daily life, "
            "consider seeking support from a therapist or counselor who can provide strategies for coping."
        )
    elif "vaccine" in user_input:
        return (
            "Vaccines are essential for preventing infectious diseases. Speak with your healthcare provider about recommended vaccines "
            "based on your age, health conditions, and travel plans. Keep track of your vaccination schedule and ensure you're up-to-date "
            "on routine vaccines like the flu shot, MMR (measles, mumps, rubella), and COVID-19."
        )
    elif "chronic condition" in user_input:
        return (
            "If you have a chronic condition like diabetes, hypertension, or asthma, it’s crucial to follow your doctor’s advice and "
            "stick to your treatment plan. Regular check-ups, monitoring your condition, and maintaining a healthy lifestyle can help manage symptoms. "
            "Don’t hesitate to reach out to your healthcare provider if you experience any changes in your condition."
        )
    elif "allergy" in user_input:
        return (
            "If you're experiencing an allergic reaction, avoid the allergen and consult a healthcare provider if symptoms worsen. "
            "For mild reactions, antihistamines can help alleviate symptoms like itching or swelling. In cases of severe reactions, like "
            "anaphylaxis, seek immediate medical attention and use an epinephrine injection if prescribed."
        )
    else:
        # Default response when no keyword matches, using the chatbot
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        return (
            f"Here’s a general response: {response[0]['generated_text']}. However, for health-specific advice, "
            "please consult a healthcare professional."
        )

# Streamlit web app interface
def main():
    # Set up the web app title and input area
    st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="💬")
    st.title("💬 AI-Powered Health Assistant")
    st.markdown("### Ask your health-related questions below 👇")
    
    # Initialize session state for user input, response, and submitted flag if not already set
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "response" not in st.session_state:
        st.session_state.response = ""
    if "submitted" not in st.session_state:  # Initialize 'submitted' if not already in session state
        st.session_state.submitted = False

    # Create a form to handle input and submission
    with st.form(key='health_query_form'):
        # Input field for user query
        user_input = st.text_input("Your question:", st.session_state.user_input)

        # Buttons for submitting or clearing the input
        col1, col2 = st.columns([3, 1])

        with col1:
            submit_button = st.form_submit_button(label="Submit")

        with col2:
            clear_button = st.form_submit_button(label="Clear")

        # Logic for when the user clicks "Clear"
        if clear_button:
            st.session_state.user_input = ""  # Clear the input field from session state
            st.session_state.response = ""  # Clear the response from session state
            st.session_state.submitted = False  # Reset the submission state

            # No need for st.experimental_rerun(), since Streamlit auto-reruns when session state changes

    # Handle submission and display the response
    if submit_button:
        if user_input:
            st.session_state.user_input = user_input  # Save user input in session state
            response = healthcare_chatbot(user_input)
            st.session_state.response = response  # Save the response in session state
            st.session_state.submitted = True  # Mark that submission has occurred

            # Display the result
            st.write(f"**User**: {user_input}")
            st.write(f"**Healthcare Assistant**: {response}")
        else:
            st.warning("Please enter a question first!")

    # Show the response if present and only after submission
    if st.session_state.submitted and st.session_state.response:
        # This part should no longer duplicate responses
        pass  # We already display the response directly when the submit button is clicked

    # Add some additional features for the user
    st.markdown("---")
    st.markdown("### How can I help you?")
    st.markdown(""" 
    - **Symptom**: Provides general guidance about symptoms.
    - **Appointment**: Helps schedule doctor appointments.
    - **Medication**: Gives tips on taking medication properly.
    - **Health Tips**: Offers health advice for well-being.
    """)

if __name__ == "__main__":
    main()
