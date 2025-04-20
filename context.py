from openai import OpenAI  # must install openai package
import os,json



from dotenv import load_dotenv


load_dotenv()

client=OpenAI()

def summary(chat):
    if len(chat)>=10:
        short="summary of previous convo->"
        for message in chat[:-5]:
            if message["role"]=="system":
                short+="system:"+message['content']
                
            elif message["role"]=="user":
                short+="user:"+message['content']

        chat=[{"role":"system","content":"you are a helpfull assistent"},
          {"role":"system","content":short}]+chat[-5:]
    return chat

def ask(question,chat):
    chat.append({"role":"user","content":question})
    response=client.chat.completions.create(
        messages=chat,
        model="gpt-4o",
        temperature=0.7
    )
    
    ans=response.choices[0].message.content
    chat.append({"role":"assistant","content":ans})
    return ans


def load_data():
    if os.path.exists("db.json"):
        with open("db.json", "r") as file:
            return json.load(file)
    return [{"role": "system", "content": "You are a helpful assistant."}]

# Step 3: Save current chat
def save(chat):
    with open("db.json", "w") as file:
        json.dump(chat, file,indent=4)  
    
    


def chat_bot():
    while True:
        
        question=input("ask->")
        if question in ["exit","quit"]:
            break
        chat=load_data()
        chat=summary(chat)
        reply=ask(question,chat)
        print(reply)
        save(chat)
    
chat_bot()
    
    
    