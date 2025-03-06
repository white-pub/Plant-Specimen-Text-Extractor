from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()


img_path = "test-images/20250220_143727.jpg"
result, _ = engine(img_path)  # Using _ to ignore the elapse time

# Extract just the text from the result
corpus = ""
if result:
    text_only = [item[1] for item in result]
    for text in text_only:
        corpus += text + " "
        print(text)
else:
    print("No text detected")


print(corpus)
