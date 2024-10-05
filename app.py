#pacotes e importa as bibliotecas para mostrar os dados do note
import platform as p
import winapps as w

#exebir o sistema operacional do usuário
print(f'Sitema operacional do usuário: {p.system()} {p.release()}.')

#listar todos os programas instalados no computador
print('\nLista de todos os programas instalados:\n')
for programa in w.list_installed():
    print(f'Programa: {programa.name}.')
    print(f'Versão: {programa.version}.')
    print(f'Data da instalção: {programa.install_date}.')
    print(f'Data da publicação: {programa.publisher}.')
    print(f'Local da desinstalação: {programa.uninstall_string}.')
    print(f"{'-'*30}")
    

