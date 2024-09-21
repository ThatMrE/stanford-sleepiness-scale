import streamlit as st

# Title of the app
st.title("Stanford Sleepiness Scale (SSS)")

# Description
st.write("""
The Stanford Sleepiness Scale (SSS) is a simple, quick, and effective tool used to assess an individual's current state of alertness and sleepiness. 
It can help you gauge your alertness levels at different times of the day. 
Select your current level of sleepiness below.
""")

# List of SSS levels
sss_levels = [
    "1 - Feeling active, vital, alert, or wide awake",
    "2 - Functioning at high levels, but not at peak; able to concentrate",
    "3 - Awake, but relaxed; responsive but not fully alert",
    "4 - Somewhat foggy, let down",
    "5 - Foggy; losing interest in remaining awake; slowed down",
    "6 - Sleepy, woozy, fighting sleep; prefer to lie down",
    "7 - No longer fighting sleep, sleep onset soon; having dream-like thoughts"
]

# Dropdown selection for SSS level
selected_level = st.selectbox("Select your current level of sleepiness:", sss_levels)

# Interpretation of the selected level
if selected_level:
    st.subheader("Interpretation:")
    st.write(f"You selected: {selected_level}")
    if selected_level.startswith("1"):
        st.write("You are very alert and wide awake. Great for focus-intensive tasks!")
    elif selected_level.startswith("2"):
        st.write("You are functioning well, but not at your peak. It's a good time for routine tasks.")
    elif selected_level.startswith("3"):
        st.write("You are awake but relaxed. You may not be at your sharpest for complex tasks.")
    elif selected_level.startswith("4"):
        st.write("You are starting to feel a bit foggy. It's a good time for a break or some light tasks.")
    elif selected_level.startswith("5"):
        st.write("You are feeling quite foggy and are losing interest in staying awake. A short nap may help.")
    elif selected_level.startswith("6"):
        st.write("You are very sleepy and finding it hard to stay awake. It's best to rest or take a nap.")
    elif selected_level.startswith("7"):
        st.write("You are on the verge of falling asleep. It's crucial to find a safe place to rest.")

# Note for medical use
st.write("""
*This tool is intended for educational purposes and should not be used as a diagnostic tool. 
If you are experiencing excessive sleepiness or fatigue, consult a healthcare professional.*
""")

# Footer
st.write("Created with ❤️ using [Streamlit](https://streamlit.io/)")
