

#METTENDO LA VARIABILE FILE ALLA FIUNE E CREANDOLA AL MOMENTO SAREBBE COME SCRIVERE file=open("Lezione15/file.txt")


with open("Lezione15/file.txt") as file :
    pass



# IN QUESTO MODO SI DEFINISCE LA CLASSE PER DEFINIRE IL CPOMPORTAMENTO DI <WITH>
class ContextManager:
    def __enter__(self):
        print("risorsa acquisita!")
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is not None:
            pass

        print("risorsa rilasciata")

        return False
    



with ContextManager() as manager:
    print("Sono dentro with")