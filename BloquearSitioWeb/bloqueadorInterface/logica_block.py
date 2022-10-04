class Logica:

    def clicked():
        lbl.configure(text="Button was clicked !!")

    def comparaHorario(x,y):
        if x==y:
            print("no debe permitir guardar el horario")
        
        elif (x<y):
            print("No puede ser menor el horario de incio que el final")
        
        else:
            print("todo Okay")

