from autogen import AssistantAgent,UserProxyAgent, config_list_from_json

# import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# create assistent agent
assistent = AssistantAgent(name="assistant", llm_config={"config_list": config_list})


# create user proxy agent
user_proxy = UserProxyAgent(name="user_proxy", code_execution_config={"work_dir":"coding"})

# Start the conversation
user_proxy.initiate_chat(
	assistent, message="Create the game pong in 2D with a AI running in one side of the screen"
)