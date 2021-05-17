from pydantic import BaseModel, Field
from transformers import pipeline
import os

# Load model
generator = pipeline("text-generation", model=os.environ['GPT_MODEL'], device=0) # remove device=0 for CPU usage

class TextGenerationInput(BaseModel):
    text: str = Field(
        ...,
	title="Text Input",
        description="The input text to use as basis to generate text.",
        max_length=8000,
    )
    temperature: float = Field(
        1.0,
	gt=0.0,
        multiple_of=0.001,
        description="The value used to module the next token probabilities.",
    )
    min_length: int = Field(
        50,
	ge=0,
	le=500,
        description="The minimum length of the sequence to be generated.",
    )
    max_length: int = Field(
        100,
	ge=0,
	le=500,
        description="The maximum length of the sequence to be generated.",
    )
    do_sample: bool = Field(
        True,
	description="Whether or not to use sampling ; use greedy decoding otherwise.",
    )


class TextGenerationOutput(BaseModel):
    generated_text: str = Field(...)


def generate_text(input: TextGenerationInput) -> TextGenerationOutput:
    """Generate text based on a given prompt."""

    res = generator(
        input.text,
        do_sample=input.do_sample,
        temperature=input.temperature,
        min_length=input.min_length,
        max_length=input.max_length,
    )
    return TextGenerationOutput(generated_text=res[0]["generated_text"])