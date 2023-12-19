You are an AI developer and your goal is to execute this objective:\n"
Title: {current_objective['title']}.\n"
Description: {current_objective['description']}.\n"
This objective is part of the development of this application:\n"
{config.app_description}.\n\n"
The following steps were sucessufully completed before the objective:\n"
{ObjectivesSerializer.serialize(memory.objetives)}.\n\n"
So you should not repeat the same steps you did in the past.\n"
Think step by step, break the objective in intermediate steps and justify your step.\n"
Make a action using tools if necessary. Your action should be align with your current step.\n"
Each action should be independent from each other."
Tools:\n"
{json.dumps(Tool.list_tools(), indent=4)}\n\n"
You must consider the current files when making an action.\n"
Current files:\n"
{list_file_structure(config.path)}\n\n"
States history:\n"
                f"Your action should be a continuation of the following actions and learn from past actions:\n"
                f"{StatesSerializer.serialize(memory.states)}\n\n"
                f"You should only respond in JSON format as described below:\n"
                f"Response Format:\n"
                f"{json.dumps(response_format, indent=4)}\n"
                f"Ensure the response can be parsed by Python json.loads. Only return the json!\n"
            )

            executor_respone = llm.generate(prompt_string)
        else:
            executor_respone = {
                "thought": current_objective["description"],
                "action": current_objective["action"],
            }

        return executor_respone
