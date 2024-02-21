import math

def menu():

     print('''
            MENU:

            1 -  Calcule as componentes nos eixos x e y da velocidade inicial da bola. (V0x e V0y)
            
            2 - Calcule o tempo em que a bola permanece no ar.
            
            3 - Ache a posição da bola no instante.
            
            4 - Calcule a velocidade e suas componentes nos eixos x e y no instante
            
            5 - Altura máxima alcançada pela bola.
            
            6 - Alcance horizontal.
            
            7 - Calcule a velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y (Vx, Vy, módulo).

            8 - Calcule a velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y (Vx, Vy, módulo).  

            9 - Distância Horizontal em problemas que dão apenas H e V0

            10 - Questões com input de apenas v0 e ang
            
            0 - Sair
        ''')

def escolha():
    print('\n')
    A = int(input('Escolha uma opção: '))
    print('\n')
    return A

def V0x_V0y():

  V0 = float (input('Entre com o valor de V0: '))
  print('\n')

  q1 = input('O valor de V0 está em metros por segundo ? ')
  print('\n')

  if q1 == "S" or q1 == "s" or q1 == "sim" or q1 == 'Sim':
  
    ang = float(input("Entre com o valor do ângulo: "))
    print('\n')
  
    angulo = math.radians(ang)

    cos = math.cos(angulo)

    sen =  math.sin(angulo)

    v0x = V0 * cos

    v0y = V0 * sen

  else:
    
    V0 = (V0/3.6)

    ang = float(input("Entre com o valor do ângulo: "))
    print('\n')
  
    angulo = math.radians(ang)

    cos = math.cos(angulo)

    sen =  math.sin(angulo)

    v0x = V0 * cos

    v0y = V0 * sen

  print('Seu V0x é: ',v0x) #V0x também é a velocidade para qualquer outro instante de tempo em X

  print('\n')

  print('Seu V0y é: ',v0y)

  return v0x, v0y

def tempo_ar(v0y):
  
  y = float (input('Entre com o valor da altura em metros: '))
  print('\n')

  gravi_metade = -0.5*9.8
  
  t1 = v0y**2 -(4*gravi_metade*y)

  t2 = (-v0y - math.sqrt(t1))/(2*gravi_metade)

  print('O tempo que a bolinha permanece no ar é de: ', t2)

  return t2

def p_inst(v0x, v0y):

  g = 9.8

  y = float (input('Entre com o valor da altura em metros: '))
  print('\n')
  
  minuto = float(input('Entre com o tempo: '))
  print('\n')
  
  posicaox =  (0+v0x*minuto)

  posicaoy = (y + v0y * minuto -0.5 * g *minuto**2)

  print('X em {} segundos é : {} '.format(minuto, posicaox))

  print('\n')

  print('Y em {} segundos é : {}'.format(minuto,posicaoy))

def velo_inst(v0x, v0y):
    
    g = 9.8
  
    minuto = float(input('Entre com o tempo em segundos: '))
    
    print('\n')


    vx = v0x
    vy =  (v0y - g * minuto)
    
    m_v = math.sqrt((v0x*v0x)+(vy*vy))
    
    print ('Velocidade em X com o tempo de {} segundo:{}'.format(minuto, vx))

    print('\n')
    
    print ('Velocidade em Y com o tempo de {} segundos:{} '.format(minuto,vy))

    print('\n')

    print('Módulo da velocidade no tempo de {} segundos: {}'.format(minuto,m_v))

def altura_max():
    
    g = 9.8
    
    V0 = float (input('Entre com o valor de V0: '))
    print('\n')
    q1 = input ("V0 está em metros por segundo? ")

    if q1 == 'n' or q1=='não' or q1 == 'N':

      V0 = V0/3.6
      
    print('\n')
    
    ang = float(input("Entre com o valor do ângulo: "))
    print('\n')
    
    y = float (input('Entre com o valor da altura em metros: '))
    print('\n')
  
    angulo = math.radians(ang)

    sen =  math.sin(angulo)
    
    v0_quadrado = V0*V0

    sen_quadrado = sen*sen

    altura_max = 1/2*((v0_quadrado*sen_quadrado)/g)
    
    print('A altura máxima alcançada pela bola é de {}'.format(altura_max+y))

def alcance_horizontal():
    
    g = 9.8
    
    V0 = float (input('Entre com o valor de V0: '))
    print('\n')
    q1 = input ("V0 está em metros por segundo ?")

    if q1 == 'n' or q1=='não' or q1 == 'N':

      V0 = V0/3.6
    
    print('\n')
    
    ang = float(input("Entre com o valor do ângulo: "))
    
    print('\n')

    ang1 = 2*ang
    
    ang2 = math.radians(ang1)
    
    sen1 = math.sin(ang2)
    
    v0_quadrado = V0*V0

    alcance = (v0_quadrado*sen1)/g
    
    print('O alcance horizontal é de: {}'.format(alcance))

def antes_do_chão(v0x, v0y, t2):

  print('A velocidade da bola imediatamente antes de alcançar o solo e suas componentes no eixo x é de: {}'.format(v0x))

  vy = v0y - 9.8* t2

  print('\n')

  print('A velocidade da bola imediatamente antes de alcançar o solo e suas componentes no eixo é de: {}'.format(vy))

  print('\n')
  
  conta = math.sqrt(v0x*v0x+v0y*v0y)
  
  print('Módulo: {}'.format(conta))
  
def velo_altura_max(v0x):

  print('A velociadade em X quando o projetil atinge a altura máxima é de: {}'.format(v0x))

  print('\n')

  print('A velocidade em Y quando o projetil atinge a altura máxima é de: 0')

  print("\n")
  
  print('O módulo é: {} '.format(math.sqrt(v0x**2)))

def H_V0():
  V0 = float (input('Entre com o valor de V0: '))
  print('\n')

  q1 = input('O valor de V0 está em metros por segundo ? ')
  print('\n')

  if q1 == "n" or q1 == "N" or q1 == "nao" or q1 == 'Nao' or q1 == 'não' or q1=='Não':
    V0 = V0 / 3.6

  h = float(input('Altura: '))

  a = 9.8
  
  t = math.sqrt(2*h/a)

  d = V0*t

  print('Distância horizontal: {}'.format(d))

  vy = 0 + (-a)*t 

  modulo = math.sqrt(V0**2 + vy**2)

  print('Vx: {}'.format(V0))

  print('Vy: {}'.format(vy))

  print('Módulo: {}'.format(modulo))

def V0_O():
  V0 = float (input('Entre com o valor de V0: '))
  print('\n')

  q1 = input('O valor de V0 está em metros por segundo ? ')
  print('\n')

  if q1 == "n" or q1 == "N" or q1 == "nao" or q1 == 'Nao' or q1 == 'não' or q1=='Não':
    V0 = V0 / 3.6

  ang = float(input('Entre com o ângulo:'))

  angulo = math.radians(ang)

  tan = math.tan(angulo)

  y = tan / V0
  
  g = 9.8

  cos = math.cos(angulo)

  sen =  math.sin(angulo)

  v0x = V0 * cos

  v0y = V0 * sen

  print('\n')
  
  minuto = float(input('Entre com o tempo: '))
  
  print('\n')
  
  posicaox =  (0+v0x*minuto)

  posicaoy = (y + v0y * minuto -0.5 * g *minuto**2)

  print('X em {} segundos é : {} '.format(minuto, posicaox))

  print('\n')

  print('Y em {} segundos é : {}'.format(minuto,posicaoy))
  

  
def sair():

    print('Você saiu !')

while True: 

    menu()

    x = escolha()

    if(x==1):

      v0x, v0y = V0x_V0y()
        
    if(x==2):

      t2 = tempo_ar(v0y)

    if (x == 3):

      p_inst(v0x, v0y)

    if (x==4):

      velo_inst(v0x, v0y)

    if (x==5):

      altura_max()
      
    if (x==6):

      alcance_horizontal() 

    if (x==7):
      
      antes_do_chão(v0x, v0y, t2)

    if (x==8):

      velo_altura_max(v0x)

    if (x == 9):
      H_V0()

    if (x == 10):
      V0_O()

    if(x==0):

      sair()
      break 