#Streamlit
import streamlit as st
st.set_page_config(page_title="Growth Mindset Challenge",project_icon="★")
st.title("Growth Mindset Challenge")

st.header("🚀 Welcome to the Growth Mindset Challenge")
st.markdown("🌟🌟🌟")
st.write("Keep pushing your boundaries and always believe in your potential to grow and succeed! 🌱💪")

#quote 
st.header("💡Today's Mindset")
st.write("Your potential is endless; grow through what you go through.")

st.header("🦴 What's Your Challenge Today?")
user_input = st.text_input("Enter your challenge here:")

#Conditional statement
if user_input:
    st.write(f"Your challenge today is: {user_input}.Keep pushing your boundaries and always believe in your potential to grow and succeed! 🌱💪")


else:
    st.warning(" Please enter your challenge to get started!")

    #Reflaction
    st.header("Reflect on Your Challenge")
    reflection= st.text_area("Write your reflection here:")

    if reflection:
        st.success(f"🏆 Great Insight! Your Reflection : {reflection}")
    else:
        st.info("The best way to move forward is to learn from where you've been!Share Your difficulties")

    #Success and Acheivement
    st.header("🎉Celebrate Your Success🎉 ")
    acheivement = st.text_input("Share Your recent acheivement:")

    if acheivement:
        st.success(f"🎉 Great! You acheived:")
        st.info("If you love what you are doing, you will be successful - Albert Schweitzer")

    #footer
    st.write("---")    
    st.write("Keep pushing forward, and you'll get there! 🚀")
    