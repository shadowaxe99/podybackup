from typing import List
from openai.api_resources.abstract.api_resource import APIResource
from pydantic import BaseModel

class OpenAISchema(BaseModel):
    pass

class User(OpenAISchema):
    name: str
    age: int

class MultiTask(OpenAISchema):
    def __init__(self, schema):
        self.schema = schema
        self.openai_schema = {"name": schema}

    @staticmethod
    def from_streaming_response(response):
        for message in response['choices'][0]['message']['role']:
            yield User(**message)

def stream_extract(input: str) -> List[User]:
    openai = APIResource(api_key="your-api-key")
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
    users = []
    for user in MultiUser.from_streaming_response(completion):
        assert isinstance(user, User)
        users.append(user)
    return users