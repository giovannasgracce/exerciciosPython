from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao= -1 #NÃO PODE POR A MESMA OPÇÃO QUE DO MENU EX:0 SERIA O FIM
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n------- MENU -------\n\n'      +
              "Escolha uma das opções abaixo: " +
              '\n0. Sair'                       +
              '\n1. Somar'                      +
              '\n2. Subtrair'                   +
              '\n3. Dividir'                    +
              '\n4. Multiplicar'                +
              '\n5. Potência'                   +
              '\n6. Raiz'                       +
              '\n7. Tabuada'                    +
              '\n8. exercício 01'               +
              '\n9. exercício 02'               +
              '\n10. exercício 03'              +
              '\n11. exercício 04'              +
              '\n12. exercício 05'              +
              '\n13. exercício 06'              +
              '\n14. exercício 08'              +
              '\n15. exercício 09'              +
              '\n16. exercício 10'              +
              '\n17. exercício 11'              +
              '\n18. exercício 12'              +
              '\n19. exercício 13'              +
              '\n20. exercício 14'              +
              '\n21. exercício 15'              +
              '\n22. exercício 16'              +
              '\n23. exercício 17'              +
              '\n24. exercício 18'              +
              '\n25. exercício 19'              +
              '\n26. exercício 20')

    def coletar(self):
         self.num1 = int(input("Informe o primeiro número: "))
         self.num2 = int(input("Informe o segundo número: "))

    def coletar1(self):
        self.num1 = int(input("Informe o primeiro número: "))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # chamar opções
            self.opcao = int(input('Escolha uma opção acima: '))

            if self.opcao == 0:
                print('Obrigada!!!')
            if self.opcao == 1:
                self.coletar() #chamar o input por meio do coletar
                print(f'\nA soma dos números é: {self.opera.somar(self.num1,self.num2)}')

            elif self.opcao == 2:
                self.coletar()
                print(f'\nA subtração dos números é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'\nA divisão dos números é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'\nA multiplicação dos números é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'\nA potência do número é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz de {self.num1}  é: {self.opera.raiz(self.num1)}')
                print(f'\nA raiz de {self.num2}  é: {self.opera.raiz1(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'\nA tabuada do  {self.num2} número é: {self.opera.raiz(self.num1)}')

            elif self.opcao == 8:
               print(f'\n Os valores de 1 ate 10 é: {self.opera.exercicio01()}')

            elif self.opcao == 9:
               print(f'\n Os valores pares de 1 ate 20 é: {self.opera.exercicio02()}')

            elif self.opcao == 10:
               print(f'\n O da soma de 1 ate 100 é: {self.opera.exercicio03()}')

            elif self.opcao == 11:
               print(f'\n Os multiplos de 5 de 1 ate 50 é: {self.opera.exercicio04()}')

            elif self.opcao == 12:
               self.coletar1()
               print(f'\n O número digitado é: {self.opera.exercicio05(self.num1)}')

            elif self.opcao == 13:
               self.coletar1()
               print(f'\n O número digitado é: {self.opera.exercicio06(self.num1)}')

            elif self.opcao == 14:
               self.coletar1()
               print(f'\n  {self.opera.exercicio08(self.num1)}')

            elif self.opcao == 15:
               self.coletar1()
               print(f'\n  {self.opera.exercicio09(self.num1)}')

            elif self.opcao == 16:
               print(self.opera.exercicio10())

            elif self.opcao == 17:
               self.coletar1()
               print(f'\n  {self.opera.exercicio11(self.num1)}')


            elif self.opcao == 18:
                self.coletar1()
                print(f'\n :  {self.opera.exercicio12(self.num1)}')

            elif self.opcao == 19:
                self.coletar1()
                print(f'\n :  {self.opera.exercicio13()}')

            elif self.opcao == 20:
                self.coletar1()
                print(f'\n{self.opera.exercicio14(self.num1)}\n')

            elif self.opcao == 21:
                self.coletar1()
                print(f'\n A soma dos digitos é:  {self.opera.exercicio15(self.num1)}')

            elif self.opcao == 22:
                self.coletar1()
                print(f'\n  {self.opera.exercicio16(self.num1)}')

            elif self.opcao == 23:
                self.coletar1()
                print(f'\n  {self.opera.exercicio17(self.num1)}')

            elif self.opcao == 24:
                self.coletar1()
                print(f'\n  {self.opera.exercicio18(self.num1)}')

            elif self.opcao == 25:
                self.coletar1()
                print(f'\n{self.opera.exercicio19(self.num1)}\n')

            elif self.opcao == 26:
                self.coletar1()
                print(f'\n  {self.opera.exercicio20(self.num1)}')


        else:
            print("Código escolhido não é válido!")













