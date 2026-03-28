import streamlit as st

st.title("Model response test")

explanation = r"""
First, calculate the volume of the aquarium: \(4 \times 6 \times 3 = 72\) cubic feet. Since Nancy fills it halfway, there is initially \(72 / 2 = 36\) cubic feet of water. When the cat knocks it over, half of this is spilled, so \(36 / 2 = 18\) cubic feet remain. Nancy then triples this amount, resulting in \(18 \times 3 = 54\) cubic feet of water.
"""

st.markdown(explanation)