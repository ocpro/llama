import requests


# generate
def generate():
    url = "http://localhost:9000/generate"  # Replace with the actual URL of your API endpoint
    data = {
        "prompts": [
            "I believe the meaning of life is",
            "Simply put, the theory of relativity states that ",
            """A brief message congratulating the team on the launch:

            Hi everyone,

            I just """,
            """Translate English to French:

            sea otter => loutre de mer
            peppermint => menthe poivrée
            plush girafe => girafe peluche
            cheese =>""",
        ],
        "max_gen_len": 64,
        "temperature": 0.6,
        "top_p": 0.9
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        generated_texts = response.json()["generated_texts"]
        for generated_text in generated_texts:
            print(generated_text["prompt"])
            print("> " + generated_text["generation"])
            print("\n==================================\n")
    else:
        print("Error:", response.status_code, response.text)


# =============================
# chat
def chat():
    url = "http://localhost:9000/chat"  # Replace with the actual URL of your API endpoint
    data = {
        "dialogs": [
            [{"role": "user", "content": "what is the recipe of mayonnaise?"}],
            [
                {"role": "user", "content": "I am going to Paris, what should I see?"},
                {
                    "role": "assistant",
                    "content": """\
    Paris, the capital of France, is known for its stunning architecture, art museums, historical landmarks, and romantic atmosphere. Here are some of the top attractions to see in Paris:
    
    1. The Eiffel Tower: The iconic Eiffel Tower is one of the most recognizable landmarks in the world and offers breathtaking views of the city.
    2. The Louvre Museum: The Louvre is one of the world's largest and most famous museums, housing an impressive collection of art and artifacts, including the Mona Lisa.
    3. Notre-Dame Cathedral: This beautiful cathedral is one of the most famous landmarks in Paris and is known for its Gothic architecture and stunning stained glass windows.
    
    These are just a few of the many attractions that Paris has to offer. With so much to see and do, it's no wonder that Paris is one of the most popular tourist destinations in the world.""",
                },
                {"role": "user", "content": "What is so great about #1?"},
            ],
            [
                {"role": "system", "content": "Always answer with Haiku"},
                {"role": "user", "content": "I am going to Paris, what should I see?"},
            ],
            [
                {
                    "role": "system",
                    "content": "Always answer with emojis",
                },
                {"role": "user", "content": "How to go from Beijing to NY?"},
            ],
        ],
        "max_gen_len": None,
        "temperature": 0.6,
        "top_p": 0.9
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        generated_dialogs = response.json()["generated_dialogs"]
        for generated_dialog in generated_dialogs:
            dialog = generated_dialog["dialog"]
            generation = generated_dialog["generation"]
            for msg in dialog:
                print(f"{msg['role'].capitalize()}: {msg['content']}\n")
            print(
                f"> {generation['role'].capitalize()}: {generation['content']}"
            )
            print("\n==================================\n")
    else:
        print("Error:", response.status_code, response.text)


if __name__ == '__main__':
    generate()
    chat()
