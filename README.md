# AUTOGEN: Conversational AI for Game Development - A Study

## Introduction

Hello and welcome to my study project on using the `autogen` library. Here, I am exploring the fascinating intersection of Conversational AI and Game Development. Leveraging the power of OpenAI, I aim to understand and experiment with automatic code generation for creating games.

## Objective of the Study

The primary focus of this study is:
- Understanding the `autogen` framework and its components.
- Using Conversational AI to generate code snippets for game development.
- Evaluating the generated code's effectiveness and accuracy.

## How It Works

Below is a brief demonstration of how I utilized the `autogen` library to instruct the AI to create a 2D Pong game:

```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create the assistant agent
assistent = AssistantAgent(name="assistant", llm_config={"config_list": config_list})

# Establish the user proxy agent
user_proxy = UserProxyAgent(name="user_proxy", code_execution_config={"work_dir":"coding"})

# Kickstart the conversation with the AI
user_proxy.initiate_chat(
    assistent, message="Create the game pong in 2D with a AI running in one side of the screen"
)
