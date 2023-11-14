# VideoLlama_X_OOPS_Prompt_Eng

Welcome to the VideoLlama_X_OOPS project! 🎥🦙

## Overview

This repository explores the application of the [VideoLlama model](https://github.com/DAMO-NLP-SG/Video-LLaMA) to YouTube fail videos extracted from the OOPS dataset. Leveraging prompt engineering techniques from three influential papers ( [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/pdf/2205.11916.pdf), [LARGE LANGUAGE MODELS ARE HUMAN-LEVEL
PROMPT ENGINEERS](https://openreview.net/pdf?id=92gvk82DE-), [The Dawn of LMMs:
Preliminary Explorations with GPT-4V(ision)](https://arxiv.org/pdf/2309.17421.pdf) ), I aim to unlock the latent capabilities of Language Models (LLMs) to extract key events in a video.

## Dataset - OOPS

The dataset used in this project is OOPS ([oops! Predicting Unintentional Action in Video](https://arxiv.org/pdf/1911.11206.pdf)). Specifically, I [filtered out](https://github.com/Hasnat79/Oops_extractor) videos from the OOPS dataset that depict failed actions. 

## Experiment Results

The detailed experiment results and observations can be found in the [result docs](https://docs.google.com/document/d/1vhloS4wbOLrCiMKxJ_ELirZ4gJAhkBqeWvM0UwyuIvA/edit?usp=sharing) and [exp_data.json](exp_data.json) file. It's worth noting that the documentation includes additional experiment results that are not present in the JSON file.

## Experimental Process

I employed the VideoLlama model's [Hugging Face interface](https://huggingface.co/spaces/DAMO-NLP-SG/Video-LLaMA) to generate and fine-tune prompts. The refined prompts were crucial in finding out the model's performance and improvement sectors on identifying and understanding fail events in the videos.





## Citation
If you use the experiment results from this repository in your work, please consider citing this project. Thank you <3

## Contact
Feel free to reach out if you have any questions or suggestions!
- 📧 Email: hasnatabdullah79@gmail.com
- 💼 LinkedIn: [Hasnat Md Abdullah ](https://www.linkedin.com/in/hasnat-md-abdullah/)
Happy experimenting! 🚀