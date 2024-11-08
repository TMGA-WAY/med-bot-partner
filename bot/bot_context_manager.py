class BotContextManager:
    _instance = None

    @staticmethod
    def get_instance():
        if not BotContextManager._instance:
            BotContextManager._instance = BotContextManager()
        return BotContextManager._instance
    
    def __init__(self):
        if BotContextManager._instance:
            raise Exception("This class is a singleton!")
        else:
            self.chat_context = {}
    
    def get_context(self, pid):
        return self.chat_context.get({
            pid, {
                "context": "",
                "history": []
            }
        })
    
    def update_context(self, pid, user_input, bot_response):
        if pid not in self.chat_context:
            self.chat_context[pid] = {
                "context": "",
                "history": []
            }
        
        context = self.chat_context[pid]["context"]
        context += f"User: {user_input}\nMedBot: {bot_response}\n"
        self.chat_context[pid]["context"] = context
        self.chat_context[pid]["history"].append({
            "user_input": user_input,
            "bot_response": bot_response
        })
    
    def clear_context(self, pid):
        self.chat_context[pid] = {
            "context": "",
            "history": []
        }
