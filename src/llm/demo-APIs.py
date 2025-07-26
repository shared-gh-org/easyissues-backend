from openai import OpenAI

####################################################################
###                        REASONING MODELS                      ###
####################################################################

client = OpenAI()

# The reasoning models require you to fill out something with openAI for them to verify identity. Not able to look at a free version of this 

# prompt = """
# Write a bash script that takes a matrix represented as a string with 
# format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
# """

# response = client.responses.create(
#     model="o4-mini",
#     reasoning={"effort": "medium"},
#     input=[
#         {
#             "role": "user", 
#             "content": prompt
#         }
#     ]
# )

#######################################################################
####                      CHAT models                            ######   
#######################################################################

## This is the example on their website 
response = client.responses.create(
    model="gpt-4o-mini" ,
    input=[
        {"role": "user", "content": "knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
)

print(response.output_text)

print(f"The output text available to users: {response.output_text}")
print(f"The outputs available to us: \n {vars(response)}")
# Took 28 tokens for this respone 

# Noticed a few fields related to reasoning here. Let's see what happens when you give the reasoning example here 
# Attempting chat models with reasoning 
prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.responses.create(
    model="gpt-4o-mini",
    # reasoning={"effort": "medium"}, Reasoning is not supported with this model. Welp
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(f"The output text available to users: {response.output_text}")
print(f"The outputs available to us: \n {vars(response)}")
# Total number of tokens it took was: 647, 584 524, 
# A spame of the response object we receive: 
# response_demo= {
#     'id': 'resp_6884cdeed89481a080b41c4375fe9b1000f85658a690eb4c', 
#     'created_at': 1753533934.0, 
#     'error': None, 
#     'incomplete_details': None, 
#     'instructions': None,           # instructions sounds interesting. I wonder if we can give it instructions to do something. 
#     'metadata': {}, 
#     'model': 'gpt-4o-mini-2024-07-18', 
#     'object': 'response', 
#     'output': [
#         ResponseOutputMessage(
#             id='msg_6884cdef0f8881a0a58176dcea4bc97800f85658a690eb4c', 
#             content=[
#                 ResponseOutputText(
#                     annotations=[],
#                     text= "<RESPONSE PRESENT IN README>",
#                     type='output_text', logprobs=[]
#                 )
#             ], 
#             role='assistant',                   # This denotes that the response if from the chatbot
#             status='completed', 
#             type='message'
#         )
#     ], 
#     'parallel_tool_calls': True, 
#     'temperature': 1.0, 
#     'tool_choice': 'auto', 
#     'tools': [], 
#     'top_p': 1.0, 
#     'background': False, 
#     'max_output_tokens': None,                  # Might have to use this if LLM is looking pricey 
#     'max_tool_calls': None, 
#     'previous_response_id': None, 
#     'prompt': None,                             # I guess this is a field to give more inputs? For example, if we wanted to maintain context, we would attach a further prompt here, and send this object back to GPT
#     'reasoning': Reasoning(effort=None, generate_summary=None, summary=None),       # Reasoning dosen't seem to be supported for free models. I wonder if it makes that big a difference 
#     'service_tier': 'default', 
#     'status': 'completed', 
#     'text': ResponseTextConfig(format=ResponseFormatText(type='text')), 
#     'top_logprobs': 0, 
#     'truncation': 'disabled', 
#     'usage': ResponseUsage(input_tokens=45, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=602, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=647), 
#     'user': None, 
#     '_request_id': 'req_f7f5aee81617c9d69a4e9f5ac2ed445c'
# }

###########################################################################
###            TRY SAME AS ABOVE WITH INSTRUCTIONS SET                 ####
###########################################################################
prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.responses.create(
    model="gpt-4o-mini",
    # reasoning={"effort": "medium"}, Reasoning is not supported with this model. Welp
    input=[
        {
            "role": "system",
            "content": "You're purpose is not to solve the problems, but to break it down into elementary components which might be involved in solving it, and walk the user through those. Give the tools to solve, but not the solution itself."
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(f"The output text available to users: {response.output_text}")
print(f"The outputs available to us: \n {vars(response)}")

# Total number of tokens: 784, 
# Response recorded in the readme. 

###############################################################################
###                 Let's try an actual issue now                          ####
###############################################################################
