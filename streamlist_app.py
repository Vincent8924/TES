import streamlit as st
import clips
import logging

#setup working environment
logging.basicConfig(level =15, format='%(message)s')

env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

#input
name = st.text_input("Enter your name")