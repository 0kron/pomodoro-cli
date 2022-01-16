from time import ctime, sleep
from os import system
from term_avanzada import coloredPrint, tcolor 

#Default terminal size = 79 <- change this value to allocate your default terminal size no less than 50 columns
terminal_size = 79

formato = [
'''  ██████
  ██  ██
  ██  ██
  ██  ██
  ██████''',

'''    ██  
  ████  
    ██  
    ██  
  ██████''',

'''  ██████
      ██
  ██████
  ██    
  ██████''', 

'''  ██████
      ██
    ████
      ██
  ██████''', 

'''  ██  ██
  ██  ██
  ██████
      ██
      ██''', 

'''  ██████
  ██    
  ██████
      ██
  ██████''', 

'''  ██████
  ██    
  ██████
  ██  ██
  ██████''', 

'''  ██████
      ██
      ██
      ██
      ██''',

'''  ██████
  ██  ██
  ██████
  ██  ██
  ██████''', 
'''  ██████
  ██  ██
  ██████
      ██
      ██''', 
'''        
    ██  
        
    ██  
        ''']

def toMinutes(segundos): 
    horas = segundos//3600
    segundos -= horas*3600
    minutos = segundos//60
    segundos -= minutos*60
    
    if segundos < 10: segundos = f"0{segundos}"
    if minutos < 10: minutos=f"0{minutos}"

    if horas < 1: return f"{minutos}:{segundos}"
    else: return f"{horas}:{minutos}:{segundos}"

def toSeconds(minutos): 
    minutos = str(minutos)
    formato = minutos.find(":")
    try:
        if formato > -1:
            seg = int(minutos[:formato])*60 + int(minutos[formato+1:])
        else: seg = int(minutos)*60
        return seg

    except: print("-Entrada inválida-".center(terminal_size))

def terminalClock(segundos, color=tcolor.WHITE): 
    ##Current clock to display
    reloj = toMinutes(segundos)

    ##Saving the format needed for every character in reloj
    termReloj = []
    for char in reloj: 
        switch={
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            ":": 10       
        }
        termReloj.append(switch.get(char, "categoría inválida"))

    inicio = 0
    final = 9
    for i in range(5): 
        out = color+""
        for index in termReloj:
            out += formato[index][inicio:final].replace("\n", "")
        
        print(out.center(terminal_size))
        inicio +=9
        final +=9

def pomodoro(ptime, ttime, rtime=300):
    for i in range(ttime):
      for j in range(ptime):
          curr = ctime()
          system("clear")
          print("\n")
          print(("-"+curr[11:19]+"-").center(terminal_size))
          terminalClock(ptime-j)
          print(f"- Remaining consentration time -".center(terminal_size)) 
          sleep(1)
      
      system("notify-send 'you can rest now my friend...'") ##Message of the break
      
      for j in range(rtime): 
          curr = ctime()
          system("clear")
          print("\n")
          print(("-"+curr[11:19]+"-").center(terminal_size))
          terminalClock((rtime-j),tcolor.GREEN)
          print(f"{tcolor.WHITE}- Remaining break time -".center(terminal_size))
          sleep(1)
      
      system("notify-send 'focus now, you idolent creature'") ##Message of restart

def main():
    choice = ""#Acción del usuario - User input

    #Menú de la aplicación - Program menu
    while choice != "quit": 
    
        #Imprimimos el menú de acciones
        system("clear") #Puede tener cambios con respecto a que OS se está utilizando
        coloredPrint("Pomodoro by 0miKron".center(terminal_size), tcolor.UNDERLINE)
        coloredPrint("\nMain menu: ", tcolor.BOLD)
        coloredPrint("\t[1] Default 45:00min :: 5 times.", tcolor.GREEN)
        coloredPrint("\t[2] Shorter 20:00min :: 3 times.", tcolor.CYAN)
        coloredPrint("\t[3] Customized.", tcolor.BLUE)
        coloredPrint("\t[quit] Leave program.", tcolor.GREY)
        choice = input(": ").lower()

        if choice == "1": pomodoro(toSeconds(45), 5)
        elif choice == "2": pomodoro(toSeconds(20), 3)
        elif choice == "3": 
          system("clear")
          ptime = toSeconds(input("Minutes: "))
          ttime = int(input("Repetitions: "))
          rtime = toSeconds(input("Rest time:"))
          choice = input("Confirm (y/n): ").lower()
          if choice.find("y") > -1: pomodoro(ptime, ttime, rtime)
          else: 
            choice = "3"
            continue
    
    system("clear")
    coloredPrint("\n\nNos vemos pronto, vaquero...\n", tcolor.REVERSE)

if __name__=="__main__":
  main()
