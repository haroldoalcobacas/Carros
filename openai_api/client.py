import openai
from django.conf import settings

def get_car_ai_bio(model, brand, year):
    prompt='''
    Crie uma Bio de descrição de venda para {}{}{} em 250 caracteres, com especificações técnicas, como motor, consumo, capacidade do porta malas
    '''
    openai.api_key = settings.OPENAI_API_KEY
    prompt = prompt.format(brand, model, year)
    response =  openai.Completion.create(
        model='text-davinci-003',
        prompt='',
        max_tokens=10,
    )
    return response['choices'][0]['text']
