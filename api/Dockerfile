FROM huggingface/transformers-pytorch-gpu

WORKDIR /app

COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install -r requirements.txt

RUN python3 download_model.py

EXPOSE 8000

CMD ["opyrator", "launch-ui", "app:generate_text", "--port", "8000"]