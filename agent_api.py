from fastapi import FastAPI
import requests
import os

app = FastAPI()

def calculator(expression: str):
    try:
        return eval(expression)
    except Exception as e:
        return f"Invalid calculation: {e}"

def chat_agent(user_input):
    prompt = f"""
You are an AI agent.

Available tools:
1. calculator(expression)

Rules:
- If calculation is needed, respond exactly in this format:
ACTION: calculator
INPUT: <expression>

- Otherwise, reply normally.

User: {user_input}
"""

    res = requests.post(
        url=os.getenv("AGENT_MODEL_API"),
        params={"prompt": prompt}
    )

    reply = res.json()["response"]

    if reply.startswith("ACTION: calculator"):
        expression = reply.split("INPUT:")[1].strip()
        result = calculator(expression)
        return f"🧮 Result: {result}"

    return reply







# from fastapi import FastAPI
# import requests

# app = FastAPI()

# AGENT_MODEL_API = "http://127.0.0.1:8000/generate"


# def calculator(expression):
#     try:
#         return str(eval(expression))
#     except Exception as e:
#         return f"Error: {e}"


# def agent_logic(user_input):
#     prompt = f"""
# You are an AI agent.

# Available tools:
# 1. calculator(expression)

# Rules:
# - If calculation is needed, respond exactly:
# ACTION: calculator
# INPUT: <expression>

# - Otherwise reply normally.

# User: {user_input}
# """

#     res = requests.post(
#         AGENT_MODEL_API,
#         params={"prompt": prompt}
#     )

#     reply = res.json()["response"]

#     if reply.startswith("ACTION: calculator"):
#         expression = reply.split("INPUT:")[1].strip()
#         return f"🧮 Result: {calculator(expression)}"

#     return reply


# @app.post("/chat")
# def chat(user_input: str):
#     return {
#         "response": agent_logic(user_input)
#     }
