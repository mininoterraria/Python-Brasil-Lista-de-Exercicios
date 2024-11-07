#05) Você está desenvolvendo o sistema de login para o "Buscante". O sistema deve pedir ao usuário para inserir um nome de usuário e senha. O nome de usuário deve ter pelo menos 5 caracteres e a senha deve ter pelo menos 8 caracteres. Caso as condições não sejam atendidas, o sistema deve continuar pedindo as informações até que o usuário insira dados válidos.
flag = True #A flag será utilizada para mudar o curso do loop quando a condição exata for atendida.
while flag:
  usuario = input("Insira o usuário:")
  senha = input("Insira a senha: ")
  if(len(usuario) < 5 or len(senha) < 8):
    print("Um ou mais dados inválidos!")
  else:
    print("Acesso liberado!")
    flag = False
