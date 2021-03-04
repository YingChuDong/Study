import random
import datetime as ti
import time


a = 6
while a > 0:
    a = a - 1
    if a == 0:
        print("                                  今天注册机会以及用完，明天再试")

    else:
        print("" * 10)
        print("" * 10)
        print("" * 10)
        print("                                                 中国星辰航空公司用户注册系统           ")
        print("                                             ")
        print("（提示：欢迎选择星辰航空公司，你可以在这里注册你的账号密码，但是用户名首位必须是“a”，且字符在6-15之间 ,密码只能包括英文以及数字，否则无效！）")
        print("" * 10)
        print("" * 10)
        print("" * 10)
        xm = str(input("请输入你的姓名："))
        IDC = str(input("请输入你的身份证号："))
        age1 = IDC[6:10]
        age = (2020-int(age1))
        birthN = IDC[6:10]
        birthY = IDC[10:12]
        birthR = IDC[12:14]

        if len(IDC) != 18:
            print("身份证格式错误，请重新注册"
                  "")
            break

        print("请选择你的性别：①-男，②-女")
        gender = int(input("输入所对应的序号："))
        if gender == 1:
            gender1 = "男"
        else:
            gender1 = "女"
        if 2 < gender:
            print("输入错误，请重新注册！")
            break
        name = input("请输入你的用户名：")
        
        print("" * 10)
        password = str(input("请输入你的密码："))
        print("" * 10)
        password2 = str(input("请再次输入你的密码："))
        print("" * 10)
        email = str(input("请输入你的邮箱地址："))
        VC = random.randint(1000, 9999)
        print("本次验证码是：", VC)
        print("" * 10)
        print("" * 10)

        print("请输入本次验证码：")
        VC1 = int(input())
        if name[0].isalpha():
            print("账号允许使用")
        if password.isalnum():
            print("密码格式正确")
        else:
            print("          密码错误信息：密码只能包含英文及数字")
        if VC1 != VC:
            print("          验证码错误信息：验证码输入不一致!")
        if 6 > len(name) or len(name) > 15:
            print("          用户名错误信息：长度需在3-10字符之间!")
        elif password != password2:
            print("          密码错误信息：两次密码不一致!")
        elif VC1 != VC:
            print("          验证码错误信息：验证码输入不一致!")
        elif name[0] != "a":
            print("          用户名错误信息：用户名首位必须先是“a”")
        else:

            if password.isalnum():

                print("请再次确认你的注册信息：")
                B1=print("你的名字是：", xm,"你的证件号码是：",IDC," 性别是： ", gender1, "你的用户名是：",name,"你的密码是",password,"你的邮箱是：",email, )
                Verification = int(input("信息正确输入①，错误输如②并退出重新注册："))
                if Verification == 1:
                    l = ["20%", "40%", "60%", "80%", "100%"]
                    for i in range(len(l)):
                        print("数据处理中----------------------", l[i])
                        time.sleep(1)
                    print("***数据处理完成！***")
                    print("==================================================================================================================")
                    print("                                                 恭喜你，注册成功，欢迎您选择星辰航空！")
                    print("你的名字是：", xm,"--" "你的证件号码是：",IDC,"--"
                          "你的出生日期是：",birthN,"年",birthY,"月",birthR,"日""--"
                          "你的年龄是：",age,"--" "性别是： ", gender1,"--" "你的用户名是：", name,"--"
                          "你的密码是", password, "--""你的邮箱是：", email,"--" "请妥善保存！")
                    now_time = ti.datetime.now().strftime("%F %T")
                    print("注册时间：")
                    print(now_time)

                    break
                    input()
                else:
                    print("==================================================================================================================")
                    print("                              注册系统已经退出，请重新打开！")
                    input()
                    break

            else:
                print("==================================================================================================================")
                print("                              请重新注册!")




input()
