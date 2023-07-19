```python
from typing import List
from openai_function_call import OpenAISchema, MultiTask, User, openai
import json

def extract_users_from_stream(stream: str) -> List[User]:
    data = json.loads(stream)
    users = []
    for item in data:
        user = User(name=item['name'], age=item['age'])
        users.append(user)
    return users

def create_chat_completion(input: str) -> str:
    MultiUser = MultiTask(User)
    completion = openai.ChatCompletion.create(
        model="gpt-4-0613",
        temperature=0.1,
        stream=True,
        functions=[MultiUser.openai_schema],
        function_call={"name": MultiUser.openai_schema["name"]},
        messages=[
            {
                "role": "system",
                "content": "You are a perfect entity extraction system",
            },
            {
                "role": "user",
                "content": (
                    f"Consider the data below:\n{input}\n"
                    "Correctly segment it into entities\n"
                    "Make sure the JSON is correct"
                ),
            },
        ],
        max_tokens=1000,
    )
    return completion
```