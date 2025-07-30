import flet as ft
from flet import Colors, Icons

def main(page: ft.Page):
    page.window.max_width = 288
    page.window.max_height = 448
    page.window.width = 288
    page.window.height = 448
    page.bgcolor=ft.Colors.BLUE_ACCENT
    page.title = 'Calculadora'
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.CrossAxisAlignment.END
    parentese = 0
    def porcentagem(e):
        nonlocal campo_num
        campo_num.value += str('%')
        page.update()
    def parenteses(e):
        nonlocal parentese
        if parentese == 1:
            
            campo_num.value += str(')')
            parentese = 0
            page.update()
        else:
            campo_num.value += str("(")
            parentese = 1
            page.update()
    
    texto = ' '
    campo_num = ft.TextField(str(texto), text_align=ft.TextAlign.END, width=255, bgcolor=Colors.WHITE, color=Colors.BLACK, text_style=ft.TextStyle(size=25), border_color=Colors.BLACK, read_only=True)
    def clicou_mais(e):
    
        campo_num.value += str(' + ')
        page.update()
    def tecla_pressionada(e: ft.KeyboardEvent):
        if e.key == 'Enter':
            igual(None)
        elif e.key == 'Backspace':
            campo_num.value = campo_num.value[:-1]
            page.update()
        elif e.key == '1' or e.key == '2' or e.key == '3' or e.key == '4' or e.key == '5' or e.key == '6' or e.key == '7' or e.key == '8' or e.key == '9' or e.key == '0' or e.key == '+' or e.key == '-' or e.key == 'x' or e.key == '%' or e.key == '(' or e.key == ')':
            campo_num.value += e.key
            page.update()
    page.on_keyboard_event = tecla_pressionada
    def igual(e):
        nonlocal campo_num
        resultado = campo_num.value.strip()
        resultado = resultado.replace('x', '*')
        resultado = resultado.replace('÷', '/')
        conta = resultado.replace('%', '* 1/100 *')
        resultado = eval(conta)
        if isinstance(resultado, float) and resultado.is_integer():
            campo_num.value = str(int(resultado))
        else:
            campo_num.value = str(resultado)
        page.update()
    def clicou_menos(e):
        campo_num.value += str(' - ')
        page.update()
    def botao(texto, func):
        return ft.FloatingActionButton(content=ft.Text(
            str(texto),
            size=25,
            color=Colors.BLACK,
        ),
        bgcolor=Colors.WHITE,
        on_click=func,
        )
    def ponto(e):
        nonlocal campo_num
        campo_num.value += '.'
        page.update()
    def limpar(e):
        nonlocal campo_num
        campo_num.value = ' '
        page.update()
    def clicou_multiplicar(e):
        nonlocal campo_num
        campo_num.value += str(' x ')
        page.update()
    def divide(e):
        nonlocal campo_num
        campo_num.value += str(' ÷ ')
        page.update()
    def um(e):
        nonlocal campo_num
        campo_num.value += str('1')
        page.update()
    def dois(e):
        nonlocal campo_num
        campo_num.value += str('2')
        page.update()
    def tres(e):
        nonlocal campo_num
        campo_num.value += str('3')
        page.update()
    def quatro(e):
        nonlocal campo_num
        campo_num.value += str('4')
        page.update()
    def cinco(e):
        nonlocal campo_num
        campo_num.value += str('5')
        page.update()
    def seis(e):
        nonlocal campo_num
        campo_num.value += str('6')
        page.update()
    def sete(e):
        nonlocal campo_num
        campo_num.value += str('7')
        page.update()
    def oito(e):
        nonlocal campo_num
        campo_num.value += str('8')
        page.update()
    def nove(e):
        nonlocal campo_num
        campo_num.value += str('9')
        page.update()
    def zero(e):
        nonlocal campo_num
        campo_num.value += str('0')
        page.update()


    coluna1 = ft.Row(controls=[
        botao(7, sete),
        botao(8, oito),
        botao(9, nove),
        ft.FloatingActionButton(icon=ft.Icons.REMOVE,foreground_color=ft.Colors.BLACK, bgcolor=ft.Colors.WHITE, on_click=clicou_menos),
        
    ])
    coluna2 = ft.Row(controls=[
        botao(4, quatro),
        botao(5, cinco),
        botao(6, seis),
        ft.FloatingActionButton(icon=ft.Icons.CLOSE,foreground_color=ft.Colors.BLACK, bgcolor=ft.Colors.WHITE, on_click=clicou_multiplicar),
    ])
    coluna3 = ft.Row(controls=[
        botao(1, um),
        botao(2, dois),
        botao(3, tres),
        botao('÷', divide)
        
    ])
    zeroo = ft.Row(controls=[
        ft.FloatingActionButton(content=ft.Text(
            '.',
            size=30,
            color=Colors.BLACK,
        ),
        bgcolor=Colors.WHITE,
        on_click=ponto
        ),
        botao(0, zero),
        ft.ElevatedButton(
            content=ft.Text('=',size=35,color=Colors.BLACK,height=56),
            expand=True,
            bgcolor=Colors.WHITE,
            on_click=igual,
            
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=15),
            )
            ),
        
    ],
    )
    coluna0 = ft.Row(controls=[
        botao('CE', limpar),
        botao('()', parenteses),
        botao('%', porcentagem),
        ft.FloatingActionButton(icon=ft.Icons.ADD,foreground_color=ft.Colors.BLACK, bgcolor=ft.Colors.WHITE, on_click=clicou_mais),
    
    ]
    )
    organização = ft.Column(controls=[
            campo_num,
            coluna0,
            coluna1,
            coluna2,
            coluna3,
            zeroo
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START
        )
    page.add(organização)



    
ft.app(target=main)

