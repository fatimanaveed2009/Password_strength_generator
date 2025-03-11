import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        message, feedback = check_password_strength(password)
        st.subheader(message)
        for item in feedback:
            st.write(item)
    else:
        st.warning("⚠️ Please enter a password.")

