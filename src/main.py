## Open AI integration

import os
import openai

from config.keys import openai_key
from langchain.llms import OpenAI
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("Lang Chain with Open AI api")
