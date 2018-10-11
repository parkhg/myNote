"""
Object : 연락처 관리하기
------------------------------------------------------------

Study : Class Design,
        Console Menu,
        File Handling.

Revision
2018.07.23 init version
"""

class Contact:
    # 초기화
    def __init__(self, name, phoneno, email, addr):
        self.name = name
        self.phoneno = phoneno
        self.email = email
        self.addr = addr

    # print test
    def print_info(self):
        print("{0:>10}".format("Name") + " : ", self.name)
        print("{0:>10}".format("Phone No") + " : ", self.phoneno)
        print("{0:>10}".format("E-Mail") + " : ", self.email)
        print("{0:>10}".format("Address") + " : ", self.addr)


# insert contact
def set_contact():
    name = input('Name : ')
    phoneno = input('Phone No : ')
    email = input('E-Mail : ')
    addr = input('Address : ')
    print(name, phoneno, email, addr)
    contact = Contact(name, phoneno, email, addr)
    return contact

# Print Conatct
def print_contact(contact_list):
        for contact in contact_list:
            contact.print_info()

# delete contact
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# Save Contact.
def store_contact(contact_list):
    f = open('contact_db.txt','wt')
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phoneno + '\n')
        f.write(contact.email + '\n')
        f.write(contact.addr + '\n')
    f.close()


# load Contact
def load_contact(contact_list):
    f = open('contact_db.txt','rt')
    lines = f.readlines()
    num = len(lines)/4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phoneno = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')

        contact = Contact(name, phoneno, email, addr)
        contact_list.append(contact)
    f.close()


# Menu 구성하기
def print_menu():
    print('-'*60)
    print('연락처 관리')
    print('-'*60)
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 연락처 저장')
    print('5. 종료')
    print('\n')
    menu = input("메뉴선택 : ")
    return int(menu)

# Program Execute.
def run():
    # con = Contact("Baguju",'010-3360-5717','parkhg@gmail.com','전주시 덕진구 석소로 77')
    # con.print_info()
    # set_contact()
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
        elif menu == 5:
            break

if __name__ == '__main__':
    run()
