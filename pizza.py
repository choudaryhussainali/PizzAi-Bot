# pizza.py  🚀  Streamlit “Pizza Order Processing Bot”
import os
import sys
import streamlit as st
from streamlit_chat import message
from groq import Groq
from dotenv import load_dotenv, find_dotenv

# -----------------------------------------------------------------------
# 1. Load secrets (.env OR OS env). Abort early if no key is found.
# -----------------------------------------------------------------------
load_dotenv(find_dotenv(), override=True)          # finds .env even from sub‑folders
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY is missing. Add it to a `.env` file or your "
             "environment variables and restart the app.")
    sys.exit("GROQ_API_KEY not set – exiting.")    # stops Streamlit from continuing

# -----------------------------------------------------------------------
# 2. Groq client
# -----------------------------------------------------------------------
client = Groq(api_key=GROQ_API_KEY)

# -----------------------------------------------------------------------
# 3. Helper functions
# -----------------------------------------------------------------------
def get_initial_message() -> list[dict]:
    """First system + greeting messages that seed the conversation."""
    return [
        {
            "role": "system",
            "content": (
                "You are OrderBot, an automated service to collect orders "
                "for a pizza restaurant. You first greet the customer, then "
                "collect the order, and then ask if it's a pickup or delivery. "
                "You wait to collect the entire order, then summarize it and "
                "check for a final time if the customer wants to add anything "
                "else. If it's a delivery, you ask for an address. Finally, "
                "you collect the payment. Make sure to clarify all options, "
                "extras, and sizes to uniquely identify the item from the menu. "
                "The menu includes:\n"
                "- Pepperoni pizza: 12.95, 10.00, 7.00\n"
                "- Cheese pizza: 10.95, 9.25, 6.50\n"
                "- Eggplant pizza: 11.95, 9.75, 6.75\n"
                "- Fries: 4.50, 3.50\n"
                "- Greek salad: 7.25\n"
                "Toppings:\n"
                "- Extra cheese: 2.00\n"
                "- Mushrooms: 1.50\n"
                "- Sausage: 3.00\n"
                "- Canadian bacon: 3.50\n"
                "- AI sauce: 1.50\n"
                "- Peppers: 1.00\n"
                "Drinks:\n"
                "- Coke: 3.00, 2.00, 1.00\n"
                "- Sprite: 3.00, 2.00, 1.00\n"
                "- Bottled water: 5.00"
            ),
        },
        {"role": "user", "content": "assalam o alaikum"},
        {"role": "assistant", "content": "Walaikum Salam, How are you?"},
    ]


def groq_chat_completion(messages: list[dict]) -> str:
    """Call Groq LLaMA‑3 and return the assistant’s reply."""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
    )
    return response.choices[0].message.content


def push_message(messages: list[dict], role: str, content: str) -> None:
    """Append a new message to the conversation."""
    messages.append({"role": role, "content": content})


# -----------------------------------------------------------------------
# 4. Streamlit UI
# -----------------------------------------------------------------------
st.set_page_config(page_title="Pizza Order Processing Bot", page_icon="🍕")
st.title("🍕 Pizza Order Processing Bot")

# Session‑state initialisation
if "messages" not in st.session_state:
    st.session_state.messages = get_initial_message()
if "past" not in st.session_state:
    st.session_state.past = []
if "generated" not in st.session_state:
    st.session_state.generated = []

# User input
user_input = st.text_input("Order Please 🍕:", key="input")

# When the user sends a message
if user_input:
    with st.spinner("Generating response…"):
        # 1) Add user message, 2) get bot reply, 3) store both
        push_message(st.session_state.messages, "user", user_input)
        bot_reply = groq_chat_completion(st.session_state.messages)
        push_message(st.session_state.messages, "assistant", bot_reply)

        st.session_state.past.append(user_input)
        st.session_state.generated.append(bot_reply)

# Display chat history (newest at bottom)
for i in range(len(st.session_state.generated)):
    message(st.session_state.past[i], is_user=True, key=f"user_{i}")
    message(st.session_state.generated[i], key=f"bot_{i}")
