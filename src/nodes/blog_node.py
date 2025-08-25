from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogstate import Blog

class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm=llm

    
    def title_creation(self,state:BlogState):
        """
        create the title for the linkedin content
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert linkedin content writer. Use Markdown formatting. Generate
                   a content title for the {topic}. This title should be creative 
                   and Linkedin SEO friendly

                   """
            
            sytem_message=prompt.format(topic=state["topic"])
            print(sytem_message)
            response=self.llm.invoke(sytem_message)
            print(response)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """
            You are an expert LinkedIn content creator.  
Write a LinkedIn post for the {topic} following these rules in bullet points:  

1. **Hook** – First 2 lines must stop the scroll. Use a surprising fact, bold statement, or intriguing question (max 80 characters).  
2. **Readability** – Use short paragraphs (1–2 sentences) with blank lines between them for mobile reading.  
3. **Value** – Provide 2–4 actionable insights, lessons, or tips. Use a numbered list or bullet points.  
4. **Tone** – Conversational yet professional. Avoid jargon unless audience-specific.  
5. **Engagement** – End with a thought-provoking question to invite comments.  
6. **Hashtags** – Add exactly 4 relevant hashtags (2 broad, 2 niche).  
7. **Emojis** – Use 1–3 emojis max for structure or emphasis, not decoration.
8. **Code** - create python code for the {topic} with example 

Example format:  

[HOOK]

[Short context or story]

1. Insight/Tip #1  
2. Insight/Tip #2  
3. Insight/Tip #3  
4. create python code with example

[Closing statement]  

[Engagement question]  
            """
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
        
