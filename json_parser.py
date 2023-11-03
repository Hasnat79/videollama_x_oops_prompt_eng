import json
with open("./exp_data.json", 'r') as f: 
    data = json.load(f)


with open('parsed_exp_data.txt', 'w') as file:
    for item in data:
        file.write(f"File Name: {item['file_name']}\n")
        for prompt, answer in zip(item['prompts'], item['answers']):
            file.write(f"Question: {prompt}\n")
            file.write(f"Answer: {answer}\n\n")
        file.write(f"Comment: {item['comment']}\n")
        file.write("---------------------------------------\n\n")