import streamlit as st
import time
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Multiverse",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("🌌 AI Multiverse")
    st.write("Welcome to the upgraded Identity Echo Interface.")

    ai_mode = st.selectbox(
        "Choose AI Personality",
        ["🤖 Assistant", "👨‍🏫 Teacher", "💼 Professional", "😂 Funny"]
    )

# -----------------------------
# Main Title
# -----------------------------
st.title("🌌 Upgrading the AI Multiverse")
st.write("Enter your details and transmit your message across the multiverse.")

st.markdown("""
### 🌌 Welcome to the AI Multiverse

This upgraded interface simulates how AI systems receive, process, and analyze user messages while estimating token usage in real time.

Choose an AI personality, send your message, and explore transmission analytics including token estimation and message history.
""")
# -----------------------------
# Form
# -----------------------------
with st.form("message_form"):

    user_name = st.text_input("👤 Enter Your Name")

    user_message = st.text_area(
        "💬 Enter Your Message",
        height=150
    )

    submit = st.form_submit_button("🚀 Transmit")

# -----------------------------
# Processing
# -----------------------------
if submit:

    if user_name.strip() == "":
        st.error("❌ Please provide your name.")

    elif user_message.strip() == "":
        st.warning("⚠️ Please type a message.")

    elif len(user_message) < 5:
        st.warning("Message should contain at least 5 characters.")

    else:

        with st.spinner("Transmitting through the AI Multiverse..."):
            time.sleep(2)

        # Statistics
        characters = len(user_message)
        words = len(user_message.split())
        tokens = characters / 4

        # AI Responses
        if "Assistant" in ai_mode:
            reply = "Your message has been successfully received."

        elif "Teacher" in ai_mode:
            reply = "Excellent! Keep learning and improving every day."

        elif "Professional" in ai_mode:
            reply = "Your request has been processed successfully."

        else:
            reply = "😂 Mission accomplished! The universe approves your message."

        # Success
        st.success(
            f"""
Transmission Successful!

Hello **{user_name}**

Your Message:
> {user_message}

AI Response:
{reply}
"""
        )

        # Metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Characters", characters)
        col2.metric("Words", words)
        col3.metric("Estimated Tokens", f"{tokens:.2f}")

        st.info(
            f"System Check: Approximately **{tokens:.2f}** AI tokens will be consumed."
        )

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.write("### 📅 Transmission Details")

        st.write(f"**Time:** {timestamp}")

        # Save History
        st.session_state.history.append({
            "Name": user_name,
            "Message": user_message,
            "Time": timestamp
        })

        # Download
        download_text = f"""
Name : {user_name}

Message :
{user_message}

Characters : {characters}
Words : {words}
Tokens : {tokens:.2f}

Time : {timestamp}
"""

        st.download_button(
            "📥 Download Transmission",
            download_text,
            file_name="Transmission.txt"
        )

# -----------------------------
# History
# -----------------------------
if st.session_state.history:

    st.divider()

    st.subheader("📜 Transmission History")

    for item in reversed(st.session_state.history):

        st.markdown(
            f"""
**👤 {item['Name']}**

💬 {item['Message']}

🕒 {item['Time']}

---
"""
        )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption("🚀 Developed by Ansh Choudhary | Virtual Summer Internship 2026")