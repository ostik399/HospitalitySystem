bd_user = {
    "customer@gmail.com": "customer",
    "1": "1",
    "2": "2"
}
       
def AddUserToDb():
    email = input("email: ")
    password = input("password: ")
    
    bd_user[email] = password
    print("Вас додали до бази")

def deleting ():
    email = input("email: ")
    password = input("password: ")
    if email in bd_user and bd_user[email] == password:
       del bd_user[email]
       print ("Ви успішно видалели користувача")
    else:
        print("такого користувача не існує")
        
def doctor():
    try:
        count = 0
        
        while count < 3:
            check = False
            email = input('email -> ')
            password = input('password -> ')
            
            if email in bd_user and bd_user[email] == password:
                check = True
            
            if check:
                print("Вас авторизовано")
                for i,j in bd_user.items():
                    print (f" email - {i}, password - {j}")
                return True
            
            elif count < 2:
                print("Повторіть спробу")
            else:
                print("Вас заблоковано")
                return False
            count += 1
    except:
        print('error')       
def newpassword():
    try:
        count=0
        while count < 3:
            check = False
            email = input('email -> ')
            password = input('password -> ')
                        
            if email in bd_user and bd_user[email] == password:
                check = True
            if check:
                
                change=input("ви хочете змінити пароль? ")
                if change=="так":
                    newpassword=input("напишіть новий пароль+: ")
                    bd_user[email] = newpassword
                    print(" ви оновили свій пароль")
                elif change=="ні":
                    print("гарного дня")
                return True
            elif count < 2:
                print("Повторіть спробу")
            else:
                print("Вас заблоковано")
                return False
            count += 1
    except:
        print("error")
def main():
    while True:
        print("Якщо ви хочете подивитись всіх користувач, напишіть 1\n" +
            "Якщо ви хочете додати користувача, напишіть 2\n" +
            "Якщо ви хочете видалити користувача, напишіть 3\n" + 
            "якщо ви хочете змінити пароль, напишіть 4\n" +
            "Якщо ви хочете завершити програму, напишіть 0")

        check = int(input())
        if check == 0:
            print("Гарного дня!")
            break
        elif check == 1:
            doctor()
        elif check == 2:
            AddUserToDb()
        elif check == 3:
            deleting()
        elif check == 4:
            newpassword()
        else:
            print("Оберіть ще раз")

main()
