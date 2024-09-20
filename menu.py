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
              '\n26. exercício 20'              +
              '\n27. exercício 21'              +
              '\n28. exercício 22'              +
              '\n29. exercício 23'              +
              '\n30. exercício 24'              +
              '\n31. exercício 25'              +
              '\n32. exercício 26'              +
              '\n33. exercício 27'              +
              '\n34. exercício 28'              +
              '\n35. exercício 29'              +
              '\n36. exercício 30'              +
              '\n37. exercício 31'              +
              '\n38. exercício 32'              +
              '\n39. exercício 33'              +
              '\n40. exercício 34'              +
              '\n41. exercício 35'              +
              '\n42. exercício 36'              +
              '\n43. exercício 37'              +
              '\n44. exercício 38')

    def coletar(self):
         self.num1 = int(input("Informe o primeiro número: "))
         self.num2 = int(input("Informe o segundo número: "))

    def coletar1(self):
        self.num1 = int(input("Informe o primeiro número: "))

    def base(self):
         self.num1 = int(input("Informe a base: "))
         self.num2 = int(input("Informe a altura: "))

    def idade(self):
         self.num1 = int(input("Informe quantos anos: "))
         self.num2 = int(input("Informe quantos meses: "))
         self.num3 = int(input("Informe quantos dias: "))

    def votos(self):
         self.num1 = int(input("Informe quantos votos no total: "))
         self.num2 = int(input("Informe quantos votos em branco: "))
         self.num3 = int(input("Informe quantos votos em nulo: "))
         self.num4 = int(input("Informe quantos votos válidos: "))

    def salario(self):
         self.num1 = int(input("Informe o sálario atual : "))
         self.num2 = int(input("Informe o percentual de ajuste: "))

    def nota(self):
         self.num1 = int(input("Informe a primeira nota : "))
         self.num2 = int(input("Informe a segunda nota : "))
         self.num3 = int(input("Informe a terceira nota : "))

    def coletar6(self):
        self.num1 = int(input("Informe o custo de fábrica: "))

    def maca(self):
        self.num1 = int(input("Informe o total de maçãs: "))

    def saldo(self):
        self.num1 = int(input("Informe o número da conta: "))
        self.num2 = int(input("Informe o saldo da conta: "))
        self.num3 = int(input("Informe o crédito da conta: "))
        self.num4 = int(input("Informe o débito da conta: "))

    def valores(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))

    def neg(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))

    def salario2(self):
        self.num1 = int(input("Informe o salário: "))
        self.num2 = int(input("Informe o valor das vendas: "))

    def quanti(self):
        self.num1 = int(input("Informe a quantidade de números: "))

    def numeros(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))
        self.num11 = int(input("Informe o décimo primeiro número: "))
        self.num12 = int(input("Informe o décimo segundo número: "))
        self.num13 = int(input("Informe o décimo terceiro número: "))
        self.num14 = int(input("Informe o décimo quarto número: "))
        self.num15 = int(input("Informe o décimo quinto número: "))
        self.num16 = int(input("Informe o décimo sexto número: "))
        self.num17 = int(input("Informe o décimo sétimo número: "))
        self.num18 = int(input("Informe o décimo oitavo número: "))
        self.num19 = int(input("Informe o décimo nono número: "))
        self.num20 = int(input("Informe o vigéssimo número: "))

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

            elif self.opcao == 27:
                print(f'\n  {self.opera.exercicio21()}')

            elif self.opcao == 28:
                self.coletar1()
                print(f'\n  {self.opera.exercicio22(self.num1)}')

            elif self.opcao == 29:
                self.base()
                print(f'\n  {self.opera.exercicio23(self.num1,self.num2)}')

            elif self.opcao == 30:
                self.idade()
                print(f'\n A idade em dias é:  {self.opera.exercicio24(self.num1,self.num2,self.num3)}')

            elif self.opcao == 31:
                self.votos()
                print(f'\n  {self.opera.exercicio25(self.num1,self.num2,self.num3,self.num4)}')

            elif self.opcao == 32:
                self.salario()
                print(f'\n  {self.opera.exercicio26(self.num1,self.num2)}')

            elif self.opcao == 33:
                self.coletar6()
                print(f'O custo final é: \n{self.opera.exercicio27(self.num1)}\n')


            elif self.opcao == 34:
                self.nota()
                print(f'\n  {self.opera.exercicio28(self.num1, self.num2,self.num3)}')

            elif self.opcao == 35:
                self.maca()
                print(f'\n  {self.opera.exercicio29(self.num1)}')

            elif self.opcao == 36:
                self.valores()
                print(f'\n  {self.opera.exercicio30(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')

            elif self.opcao == 37:
                self.salario2()
                print(f'O salário é: \n  {self.opera.exercicio31(self.num1, self.num2)}')


            elif self.opcao == 38:
                self.saldo()
                print(f'\n  {self.opera.exercicio32(self.num1,self.num2,self.num3,self.num4)}')


            elif self.opcao == 39:
                self.neg()
                print(f'\n  {self.opera.exercicio33(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')

            elif self.opcao == 40:
                self.neg()
                print(
                    f'A soam dos numeros menores que 4 é: \n  {self.opera.exercicio34(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')


            elif self.opcao == 41:
                print(f'\n  {self.opera.exercicio35()}')

            elif self.opcao == 42:
                self.quanti()
                print(f'\n  {self.opera.exercicio36(self.num1)}')


            elif self.opcao == 43:
                self.numeros()
                print(
                    f'\n  {self.opera.exercicio37(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10, self.num11, self.num12, self.num13, self.num14, self.num15, self.num16, self.num17, self.num18, self.num19, self.num20)}')


            elif self.opcao == 44:
                 print(f'\n  {self.opera.exercicio38()}')


        else:
            print("Código escolhido não é válido!")













