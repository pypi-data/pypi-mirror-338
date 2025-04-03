from zhipuai import ZhipuAI

model = "glm-4-0520:786930709::nrhfajpf"
api_key = "168cd85678c265c616ba8a38739e7ada.33yZxE7hx2gQXlSd"


def get_answer(question):
    messages = [
        {"role": "system", "content": "你是一位资深且专业的财税AI助手。"},
        {
            "role": "user",
            "content": question,
        },
    ]
    tools = [
        {
            "type": "web_search",
            "web_search": {
                "enable": True  # 默认为关闭状态（False） 禁用：False，启用：True。
            },
        }
    ]

    client = ZhipuAI(api_key=api_key)  # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model=model,  # 填写需要调用的模型名称
        messages=messages,
        stream=False,
        tools=tools,
    )
    return response.choices[0].message.content



if __name__ == "__main__":
    question = "车辆维修定点合同交印花税属于哪个税目？"
    answer = get_answer(question)
print(answer)


# for chunk in response:
#     print(chunk)
