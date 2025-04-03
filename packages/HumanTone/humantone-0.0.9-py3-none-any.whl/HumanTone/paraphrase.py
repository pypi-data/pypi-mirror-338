import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class HumanToneParaphraser:
    MODEL_NAME = "humarin/chatgpt_paraphraser_on_T5_base"
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.MODEL_NAME, torch_dtype=torch.float32)

    def paraphrase(self, text: str, max_length: int = 128, num_return_sequences: int = 5) -> list:
        """
        Generates multiple paraphrased versions of the given text while maintaining meaning.
        """
        prompt = f"paraphrase: {text} </s>"
        encoding = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

        with torch.no_grad():
            output = self.model.generate(
                input_ids=encoding["input_ids"],
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                do_sample=True,
                temperature=1.2,
                top_k=50,
                top_p=0.9,
                repetition_penalty=2.5
            )
        
        paraphrased_texts = list(set([self.tokenizer.decode(o, skip_special_tokens=True) for o in output]))
        paraphrased_texts = [para for para in paraphrased_texts if para.lower() != text.lower()]
        
        return paraphrased_texts or ["Paraphrasing failed, try again."]

# Example usage
if __name__ == "__main__":
    paraphraser = HumanToneParaphraser()
    sample_text = "The weather is nice today, perfect for a walk."
    results = paraphraser.paraphrase(sample_text)
    print(f"Original: {sample_text}")
    for i, paraphrased in enumerate(results, 1):
        print(f"Paraphrased {i}: {paraphrased}")
