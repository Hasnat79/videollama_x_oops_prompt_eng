import json
curr_dir="./"

def load (file):
    with open(file,'r') as f: 
        data = json.load(f)
    return data
def dump (file,data):
    with open(file,'w') as f: 
        json.dump(data, f, indent = 4 )
exp_data = load("/scratch/user/hasnat.md.abdullah/videollama_x_oops_prompt_eng/exp_data.json")

while (True):
    #need to add .mp4 at the end 
    video_file_name = input("Paste the file name: ")
    prompts = []
    answers = []
    comment = ""
    i = 1
    while i<999999:
        p = input(f"prompt {i}: ")
        ans = input(f"Answre for prompt {i}: ")
        prompts.append(p)
        answers.append(ans)

        print("-----press 'xx' to move write comment or enter to write next prompt-----")

        if input() == "xx":
            comment = input("comment: ")

            break
        i+=1
    print("------------------------------------------")

    temp_dic = {
        "file_name": video_file_name,
        "prompts": prompts,
        "answers": answers,
        "comment": comment
    }
    exp_data.append(temp_dic)


    dump("/scratch/user/hasnat.md.abdullah/videollama_x_oops_prompt_eng/exp_data.json",exp_data)


    if input("done(y/n): ")=="y":
        break
    


