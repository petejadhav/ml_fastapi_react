import transformers
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_jp_to_en(text:str):
    model_jp_en = "Helsinki-NLP/opus-mt-jap-en"
    tokenizer = AutoTokenizer.from_pretrained(model_jp_en)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_jp_en)
    text ='これは私の帽子です'
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    translation = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=False)[0]
    return translated_text

class Translator():
    def __init__(self) -> None:
        self.translator_en_de = pipeline("translation_en_to_de")
        
    def translate_en_to_de(self, text: str):
        translation = self.translator_en_de(text, max_length=40)
        return translation[0]['translation_text']