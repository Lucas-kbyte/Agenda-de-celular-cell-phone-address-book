import time
import os

agenda = []

while True:
    os.system('cls')
    print("—————————— Menu ——————————")
    time.sleep(1)
    print("1 - Ver contatos")
    time.sleep(1)
    print("2 - Adicionar contato")
    time.sleep(0.5)
    print("    ou remover contato")
    time.sleep(1)
    print("3 - Apagar todos contatos")
    print("4 - Sair")
    print("——————————————————————————")
    opcao = input()

    if opcao == "1":
     if len(agenda) == 0:
       os.system("cls")
       print("Desculpe mas a agenda está vazia, tente colocar mais pessoas em seus contatos")
       time.sleep(1)
       continue
     else:
      os.system("cls")

      print("—————————— Contatos ——————————")
      print(f"Você tem {len(agenda)} contatos salvos.")
      for contatos in agenda:
       print(f"| Nome: {contatos['Nome']}|")
       time.sleep(0.3)
       print(f"| Número: {contatos['Número']}|")
       time.sleep(0.3)
       print(f"| Email: {contatos['Email']}|")
       print("——————————————————————————————")
       time.sleep(3.5)
       continue
       

    elif opcao == "2":
     os.system("cls")
     print("——————————— Adicionar e Remover ———————————")
     print("1 - Adicionar")
     print("2 - Remover")
     opcao2 = input()

     if opcao2 == "1":
      print("Digite o nome do contato")
      nome = input()
      print("Agora digite o número do contato")
      numero = input()
      print("Digite o email do contato")
      email = input()

      contatoclonado = False

      for contatos in agenda:
        if contatos['Número'].strip().lower() == numero.strip().lower():
          contatoclonado = True
          break
         
      if contatoclonado:
        print(f"Calma ai, clonagem ainda não existe então esse número não pode ter 2 iguais")
        time.sleep(3)
        
      else:
        contatos = {
          "Nome": nome,
          "Número": numero,
          "Email": email
         }
        agenda.append(contatos)
        print(f"{nome} adicionado com sucesso")
        time.sleep(1)
        continue
     elif opcao2 == "2":
      if len(agenda) == 0:
        print("Ops, desculpe mas você não tem nenhum contato")
        time.sleep(1)
        continue
      else:
       print("Digite o número da pessoa que gostaria de remover")
       remover = input()
       if remover == numero in agenda:
        agenda.pop(remover == numero)
        print("Remoção de contato bem sucedida")
        time.sleep(1)
        continue
       elif remover != numero:
        print("Ops, pelo visto você está querendo apagar alguem que não existe, tente de novo")
        time.sleep(1.5)
        continue


    elif opcao == "3":
      os.system("cls")
      agenda.clear()
      print("A agenda foi limpa!")
      time.sleep(3)

    elif opcao == "0":
      os.system("cls")
      print("Finalizando aplicação...")
      time.sleep(3)
      break

    elif opcao == "4":
     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema.")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema..")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema...")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema.")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema..")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema...")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema.")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema..")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema...")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema.")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema..")
     print("———————————————————————————————")
     time.sleep(0.9)

     os.system("cls")
     print("———————————————————————————————")
     print("Parando o sistema...")
     print("———————————————————————————————")
     time.sleep(0.9)
     break

    else:
      os.system("cls")
      print("Aconteceu em erro, porfavor tente de novo")
      time.sleep(2)
      continue