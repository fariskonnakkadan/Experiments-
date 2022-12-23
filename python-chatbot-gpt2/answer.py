import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def generate_response(prompt, model, tokenizer, max_length=128, ignore_errors=True):
  # Encode the prompt as input to the model
  input_ids = tokenizer.encode(prompt, return_tensors='pt')
  # Create an attention mask
  attention_mask = input_ids.ne(0).type(input_ids.type())
  # Generate a response
  response = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length)
  # Decode the response
  response_text = tokenizer.decode(response[0], skip_special_tokens=True)
  return response_text


# Example usage
prompt = ("hi")
while(True):
    response = generate_response(prompt, model, tokenizer)
    print("Chatbot:"+response)
    prompt=response
