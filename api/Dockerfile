FROM huggingface/transformers-pytorch-gpu

ARG GPT_MODEL
ENV GPT_MODEL $GPT_MODEL

WORKDIR /app

COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install -r requirements.txt

RUN python3 download_model.py

EXPOSE 8000

CMD ["opyrator", "launch-api", "app:generate_text", "--port", "8000"]