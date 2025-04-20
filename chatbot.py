from openai import OpenAI
import json
import time
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI (replace with your key if needed)
client=OpenAI()
model_name="gpt-4o"

    





def log_event(log_data, file_name="chat_logs.json"):
    with open(file_name, "a") as log_file:
        # json.dump(log_data,log_file)
        log_file.write(json.dumps(log_data,indent=4))
        # log_file.write("\n")
        
        
        
        
def generate_log(prompt):
    
    try:
        st_time=time.time()
        
        response=client.chat.completions.create(
            messages=[{"role":"user","content":prompt}],
            model=model_name,
            temperature=0.8
        )
        
        end_time=time.time()
        
        ans=response.choices[0].message.content
        token=response.usage.total_tokens
        
        log_event({
            "timestamp":datetime.utcnow().isoformat(),
            "user_input":prompt,
            "bot_answer":ans,
            "token_used":token,
            "time_duration":(end_time-st_time)*1000,
            "model":model_name,
            
            "error":None
        })
        return ans
    except Exception as e:
        log_event({
            "timestamp":datetime.utcnow().isoformat(),
            "user_input":prompt,
            "bot_answer":None,
            "token_used":None,
            "time_duration":0,
            "model":model_name,
            "error":str(e)
        })
        return "something went wrong"
    
print("press exit or quit to stop.....")  
while True:
    user_input=input("you:->")
    if user_input in ["exit","quit"]:
        break
    res=generate_log(user_input)
    print(f"Bot:->{res}")
        
        
        
        
        

# def generate_response(prompt):
#     try:
#         start_time = time.time()

#         # Send prompt to LLM
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[{"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}]
#         )
        
#         end_time = time.time()
#         answer = response.choices[0].message.content
#         tokens = response.usage.total_tokens

#         # Log success
#         log_event({
#             "timestamp": datetime.utcnow().isoformat(),
#             "user_input": prompt,
#             "model_response": answer,
#             "response_time_ms": int((end_time - start_time) * 1000),
#             "tokens_used": tokens,
#             "error": None
#         })

#         return answer

#     except Exception as e:
#         # Log error
#         log_event({
#             "timestamp": datetime.utcnow().isoformat(),
#             "user_input": prompt,
#             "model_response": None,
#             "response_time_ms": 0,
#             "tokens_used": 0,
#             "error": str(e)
#         })

#         return "Oops! Something went wrong."

# # Main chat loop
# print("Chatbot ready. Type 'exit' to quit.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
#     response = generate_response(user_input)
#     print("Bot:", response)
