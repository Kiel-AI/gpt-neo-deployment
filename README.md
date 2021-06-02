# GPT-Neo Deployment using Docker and Opyrator (API & Streamlit UI)

GPT-Neo Deployment using Docker and Opyrator. Opyrator is building a Streamlit-based UI as well as a Rest-API with online a few lines of code. The deployment is done using Docker and traefik as a reverse-proxy; so it should work on every Cloud-Hoster or local machine. The repository is assuming you use a Nvidia GPU with CUDA for fast inference (If not, see section `CPU vs. GPU` for details how to use a CPU).

Unfortunately opyrator doesn't currently support running both UI and API at the same time, so in this project we set up an API and a separate UI opyrator project that calls the API-endpoint. The UI and API run on different domains.

## About GTP-Neo

[GTP-Neo](https://github.com/EleutherAI/gpt-neo) is an Open-Source Machine-Learning model for text generation (similar to GPT-3) developed and pre-trained by EleutherAI. In this repository the [EleutherAI/gpt-neo-2.7B](https://huggingface.co/EleutherAI/gpt-neo-2.7B) from Huggingface is used. You can change the model used in `docker-compose.yml` if you prefer using a smaller one.

## How to setup

First clone the repository

```
git clone https://github.com/Kiel-AI/gpt-neo-deployment.git && cd gpt-neo-deployment
```

Create an `.env` file and customize your environment variables. You can copy the `.env.example` file and customize it:

```
cp .env.example .env && nano .env
```

Make the domains point to your instance and ports 80 & 443 are open on your server. You also need to create an empty acme.json for traefik to save the certificates to:

```
touch acme.json && chmod 600 acme.json
```

## CPU vs. GPU

The current setup assumes that you are running the code on a machine with a Nvidia GPU with CUDA-support (e.g. `p2-2xlarge` instance on AWS with `AWS Deep Learning Base AMI`).
Using a GPU is recommended for much faster inference speed. If you would like to use CPU, check the comments in `api/app.py` and `docker-compose.yml` to see how you can switch to CPU-only.

## How to run

Simply use `docker-compose up`. That is going to trigger the build process for the images and starts the containers. The code downloads the GPT-Neo model on building the container and stores the model inside the container, so it doesn't need to download every time you start the container.

```
docker-compose up -d
```

After that your GPT-Neo API & UI should be available under your provided domains.
