import streamlit as st

# Page configuration
st.set_page_config(page_title="Drug Repurposing Prototype")

# Title
st.title("RAG Drug Repurposing Engine")

# Description
st.write("This is a basic prototype project developed as part of academic learning.")
st.write("The aim is to explore how existing drugs can be studied for new disease indications.")

# Input section
st.subheader("Search Module")

disease_name = st.text_input("Enter Disease Name")

# Button
if st.button("Search"):
    if disease_name:
        st.success(f"Searching related information for: {disease_name}")
        st.info("Result section will be enhanced in the next phase of development.")
    else:
        st.warning("Please enter a disease name before searching.")

# Footer
st.markdown("---")
st.write("Project Version: 1.0 (Prototype Stage)")