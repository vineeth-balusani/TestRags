import os
import streamlit

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

from embedchain import App
app = App.from_config("mistral.yaml")

streamlit.write("Hey")