import logging
from dotenv import load_dotenv
import os
import openai
import azure.functions as func


# sample request


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI our secret key

    # Load environment variables from the .env file
    load_dotenv()

    # get variables from the HTTP request req_body
    req_body = req.get_json()
    logging.info(type(req_body))

    # call the OpenAI API
    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature'])

    # format the response

    output_text = output['choices'][0]['text']

    # echo the response

    return func.HttpResponse(f"output_text",
                             status_code=200)
