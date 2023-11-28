from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"  # 或者 "gpt2-small" 也可以
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 验证模型是否成功下载
print("模型下载成功！")
