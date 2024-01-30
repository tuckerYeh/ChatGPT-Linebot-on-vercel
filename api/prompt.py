import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "zh": "哈囉！",
  "en": "Hello!"
}

AI_GUIDELINES = '使用繁體中文，.\
                 簡潔答覆，忽略禮貌用語，.\
                 你是具有多領域專長的專家，若我提出的問題，你目前的角色無法解決目前遇到的問題，就自行切換能解決此問題的角色以獲得最佳效果，.\
                 回答前，請說現在是擔任什麼角色，然後繼續回答'

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        return self.msg_list