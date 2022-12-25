import csv
def read_user():
    '''
    :return: 列表
    '''
    with open("account.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        user_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            user_list.append(user_cur)
    return user_list
def write_user(user_list):
    f = open('account.csv', 'w', encoding='gbk', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id", "account", "password", "性别", "地址", "电话", "邮箱", "状态"])
    for i in range(0, len(user_list)):
        user_cur = user_list[i]
        csv_writer.writerow(
            [user_cur.id, user_cur.account, user_cur.password, user_cur.gender, user_cur.place, user_cur.telephone,
             user_cur.mail, user_cur.state])
    f.close()

def read_item(type):
    '''
    :return: 列表
    '''
    path = type + ".csv"
    with open(path, encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        item_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            item_cur = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8])
            item_list.append(item_cur)
    return item_list
def write_item(item_list,type):
    path = type + ".csv"
    f = open(path, 'w', encoding='gbk', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id", "物品名", "具体描述", "存放地点", "联系人电话", "联系人邮箱", "物品类型", "物品主人","属性"])
    for i in range(0, len(item_list)):
        item_cur = item_list[i]
        csv_writer.writerow([item_cur.id,item_cur.name,item_cur.detail,item_cur.place,item_cur.telephone,item_cur.mail,item_cur.type,item_cur.owner,item_cur.property])
    f.close()
class User:
    def __init__(self,id='',account='',password='',gender='',place='',telephone='',mail='',state=''):
        self.id = id
        self.account = account
        self.password = password
        self.gender = gender
        self.place = place
        self.telephone = telephone
        self.mail = mail
        self.state = state
    def register(self):
        user_list = read_user()
        user_num = len(user_list)
        print("请输入你的姓名？")
        account_input = input()
        print("请输入你的密码？")
        password_input = input()
        print("请输入你的性别？")
        gender_input = input()
        print("请输入你的地址？")
        place_input = input()
        print("请输入你的电话？")
        telephone_input = input()
        print("请输入你的邮箱？")
        mail_input = input()
        user_num = user_num + 1
        new_user = User(str(user_num), account_input, password_input, gender_input, place_input, telephone_input,
                        mail_input,
                        str(0))
        user_list.append(new_user)
        write_user(user_list)
        print ("申请已提交！")
    def login(self):
        print("请输入账户")
        account_input = input()
        print("请输入密码")
        password_input = input()
        user_list = read_user()
        user_num = len(user_list)
        for i in range(0,user_num):
            user_cur = user_list[i]
            if (user_cur.account == account_input) and (user_cur.password == password_input):
                print ("登录成功！")
                user_list[i].state = 2
                write_user(user_list)
                return True,user_cur
        print ("登录失败！")
        return False,None
    def logout(self):
        user_list = read_user()
        user_num = len(user_list)
        for i in range(0,user_num):
            user_cur = user_list[i]
            if user_cur.account == self.account:
                print ("退出登录！")
                user_list[i].state = 1
                write_user(user_list)
    def add_item(self):
        print("物品类型")
        type_input = input()
        if type_input in list(stock.types_dic.keys()):
            print("物品名称")
            name_cur = input()
            print("具体描述")
            detail_cur = input()
            print("存放地点")
            place_cur = input()
            print("联系人电话")
            telephone_cur = input()
            print("联系人邮箱")
            mail_cur = input()
            print("物品主人")
            owner_cur = input()
            print("属性")
            property_dic = {}
            property_list = stock.types_dic[type_input].split(',')
            for i in range (0,len(property_list)):
                property_cur = property_list[i]
                print (property_cur)
                property_input = input()
                property_dic[property_cur] = property_input
            num_cur = len(stock.items_dic[type_input])+1
            new_item = Item(str(num_cur),name_cur,detail_cur,place_cur,telephone_cur,mail_cur,type_input,owner_cur,str(property_dic))
            stock.items_dic[type_input].append(new_item)
            write_item(stock.items_dic[type_input],type_input)
            stock.read_stock()
            print ("添加成功!")
        else :
            print("物品类型不存在")

    def delete_item(self):
        print("物品类型")
        type_input = input()
        if type_input in list(stock.types_dic.keys()):
            print("物品名称")
            name_cur = input()
            item_list = stock.items_dic[type_input]
            for i in range (0,len(item_list)):
                if item_list[i].name == name_cur:
                    del stock.items_dic[type_input][i]
            write_item(stock.items_dic[type_input], type_input)
            #stock.read_stock()
            print("取出成功!")
        else:
            print("物品类型不存在")
    def search_item(self):
        print("物品类型")
        type_input = input()
        if type_input in list(stock.types_dic.keys()):
            print("关键字")
            keyword_cur = input()
            item_list = stock.items_dic[type_input]
            for i in range(0, len(item_list)):
                if (item_list[i].name == keyword_cur) or (item_list[i].detail == keyword_cur):
                    print("-----------------------")
                    print("物品名称", item_list[i].name)
                    print("具体描述", item_list[i].detail)
                    print("存放地点", item_list[i].place)
                    print("联系人电话", item_list[i].telephone)
                    print("联系人邮箱", item_list[i].mail)
                    print("物品主人", item_list[i].owner)
                    print("属性", item_list[i].property)
            print("以上为全部搜索结果!")
        else:
            print("物品类型不存在")
class Manager:
    def __init__(self):
        self.account="lyf"
        self.password="123456"
    def approve(self):
        user_list = read_user()
        user_num = len(user_list)
        for i in range (0,user_num):
            user_cur = user_list[i]
            if user_cur.state == '0' :
                  print ("是否批准",user_cur.account,"注册？(Y/N)")
                  approval = input()
                  if approval == 'Y':
                      user_list[i].state = 1
                      write_user(user_list)
                  elif approval == 'N':
                      user_list.pop(i)
                      write_user(user_list)
                  else :
                      print ("输入错误，请重试！")
    def login(self):
        print("请输入账户")
        account_input = input()
        print("请输入密码")
        password_input = input()
        if (account_input == self.account) and (password_input == self.password):
                print ("登录成功！")
                return True
        print ("登录失败！")
        return False

    def add_type(self):
        print ("请输入新类型名称")
        type_name = input()
        print ("请输入新类型属性（不同属性之间以,分隔）")
        property_name = input()
        stock.types_dic[type_name] = property_name
        stock.items_dic[type_name] = []
        stock.write_stock()
        print ("添加类型成功！")
    def change_type(self):
        print("请输入要修改的类型名称")
        type_name = input()
        if type_name in list(stock.types_dic.keys()):
            print("请输入修改后的类型属性（不同属性之间以,分隔）")
            property_name = input()
            stock.types_dic[type_name] = property_name
            stock.write_stock()
            print("修改类型成功！")
        else:
            print("物品类型不存在")
class Item:
    def __init__(self, id, name, detail, place, telephone, mail, type, owner,property):
        self.name = name
        self.detail = detail
        self.place = place
        self.telephone = telephone
        self.mail = mail
        self.type = type
        self.owner = owner
        self.id = id
        self.property = property
class Stock:
    def __init__(self):
        self.types_dic = {}
        self.items_dic = {}
    def read_stock(self):
        with open("types.csv", encoding='gbk') as csvfile:
            csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
            for row in csv_reader:
                type_cur = row[0]
                property_cur = row[1]
                self.types_dic[type_cur] = property_cur
                self.items_dic[type_cur] = read_item(type_cur)
    def write_stock(self):
        f = open('types.csv', 'w', encoding='gbk', newline='')
        csv_writer = csv.writer(f)
        types_list = list(self.types_dic.keys())
        for i in range(0, len(types_list)):
            type_cur = types_list[i]
            property_cur = self.types_dic[type_cur]
            item_list_cur = self.items_dic[type_cur]
            csv_writer.writerow([type_cur,property_cur])
            write_item(item_list_cur,type_cur)
        f.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print ("欢迎进入你帮我助系统！")
        stock = Stock()
        stock.read_stock()
        print ("a 我是管理员 b 我是用户 c 退出系统")
        identity = input()
        if identity == 'a':
            manager = Manager()
            log_state = manager.login()
            if log_state :
                   manager.approve()
                   while True :
                         print("操作选项：")
                         print("a 建立新的物品类型 b 修改既有的物品类型 c 退出登录")
                         choice = input()
                         if choice == 'a':
                             manager.add_type()
                         elif choice == 'b':
                             manager.change_type()
                         elif choice == 'c':
                             break
                         else :
                             print ("输入错误，请重试！")
        elif identity == 'b':
            print ("请问你要注册（a）还是登录(b)？")
            choice1 = input()
            if choice1 == 'a':
                  new = User()
                  new.register()
            elif choice1 == 'b':
                  user = User()
                  log_state,user = user.login()
                  if log_state:
                      while True:
                          print("操作选项：")
                          print("a 添加物品 b 搜寻物品 c 取出物品 d 退出登录")
                          choice = input()
                          if choice == 'a':
                              user.add_item()
                          elif choice == 'b':
                              user.search_item()
                          elif choice == 'c':
                              user.delete_item()
                          elif choice == 'd':
                              user.logout()
                              break
                          else:
                              print("输入错误，请重试！")
            else:
                  print ("输入错误，请重试！")
        elif identity == 'c':
            print("已退出系统！")
            break
        else :
            print('输入错误，请重试!')