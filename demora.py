import asyncio
import random

async def demorada():
    await asyncio.sleep(random.randint(0,20))
    return random.randint(0, 10000)


def ok(num):
    test = ""
    if(num == 0):
        test = "passa"
    return test



async def main(timeout=1):
   #Abre um loop de duração indeterminada...
   while True:
       tarefa = asyncio.create_task(demorada())          #Agenda a execução da atividade demorada
       print('Fazendo uma tentativa...')               #Imprime mensagem
       #Abre um bloco de tratamento de exceções...
       try:
           await asyncio.wait_for(tarefa, timeout)       #Aguarda a execução da Task com timeout.
       except asyncio.TimeoutError:                    #Havendo exceção de timeout...
           tarefa.cancel()                               #Cancela a atividade.
           print('Time out...')                        #Imprime mensagem permanecendo no loop.
       else:
           return tarefa.result()                        #Retorna o resultado da atividade.


req = asyncio.run(main(5))
print(f'Resultado da chamada {req}')
