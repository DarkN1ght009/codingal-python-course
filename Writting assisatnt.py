from hf import generate_response

def get_essay_details():
    print("\n=== AI Writing Assistant ===")
    topic = input("What is the topic of your essay? ").strip()
    essay_type = input("What type of essay are you writing? ").strip()
    
    lengths = ["300 words", "900 words", "1200 words", "2000 words"]
    print("Select essay word count:")
    for i, length in enumerate(lengths, 1):
        print(f"{i}) {length}")
        
    try:
        idx = int(input("> ").strip())
        length = lengths[idx - 1] if 1 <= idx <= len(lengths) else "300 words"
    except ValueError:
        length = "300 words"
        
    target_audience = input("Target audience (e.g., High school students): ").strip()
    
    return {
        "topic": topic, 
        "essay_type": essay_type, 
        "length": length, 
        "target_audience": target_audience
    }

def generate_essay_content(details):
    try:
        temp = float(input("Enter temperature (0.1 structured, 0.7 creative): ").strip())
        if not (0.0 <= temp <= 1.0):
            raise ValueError
    except ValueError:
        print("Invalid temperature. Using 0.3.")
        temp = 0.3
    intro_p = input(f"Writean introduction to {details['essay_type']} about {details['topic']}on the topic {details['length']}")

    intro = generate_response(intro_p, temperature=temp,max_tokens=1024)
    print('\n=== Generated response===\n')
    print (intro)
    print('\n Would you like the body  written as a full draft or step by step')
    print('1.Full Draft , 2.Step by Step')
    choice = input('>').strip()

    if choice == "1" :
        body_p = f"Write a full body essay on {details['topic']}with the stance of {details['target audiance']}"
        body = generate_response(body_p, temperature=temp,max_token=1024)
        print('\n===Generated Full Body===\n')
        print (body)
    else :
        