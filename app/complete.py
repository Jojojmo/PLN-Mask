import logging
from transformers import BertTokenizer, BertForMaskedLM
import torch

logging.getLogger("transformers").setLevel(logging.ERROR)

def complete_sentence(sentence):
    tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
    model = BertForMaskedLM.from_pretrained("neuralmind/bert-base-portuguese-cased")
    input_ids = tokenizer.encode(sentence, return_tensors="pt")
    mask_token_indices = [i for i, token_id in enumerate(input_ids[0]) if token_id == tokenizer.mask_token_id]
    
    with torch.no_grad():
        logits = model(input_ids).logits

    for mask_token_index in mask_token_indices:
        predicted_token_id = logits[0, mask_token_index].argmax().item()
        input_ids[0][mask_token_index] = predicted_token_id

    completed_sentence = tokenizer.decode(input_ids[0], skip_special_tokens=True)
    return completed_sentence

if __name__ == "__main__":
    input_sentence = "estimar o efeito preciso que a inteligência ultra teve na guerra mas foi estimado que este trabalho encurtou a guerra na Europa em mais de dois anos e salvou mais de [MASK] milhões de vidas"
    completed = complete_sentence(input_sentence)
    print(completed)
