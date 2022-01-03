msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"

result = None
memory = "0"
msg_index = None


def is_one_digit(v):
    if -10 < float(v) < 10 and (float(v) - round(float(v)) == 0):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg += msg_7

    if (v1 == "0" or v2 == "0") and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    calc = input(msg_0)
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    if not x.replace('.', '', 1).isnumeric() or not y.replace('.', '', 1).isnumeric():
        print(msg_1)
    else:
        if oper not in "+-*/":
            print(msg_2)
        else:
            check(x, y, oper)

        if oper == "+":
            result = float(x) + float(y)
        elif oper == "-":
            result = float(x) - float(y)
        elif oper == "*":
            result = float(x) * float(y)
        elif oper == "/" and float(y) != 0:
            result = float(x) // float(y)
        else:
            print(msg_3)
            continue

        print(result)

        answer = ""
        while True:
            answer = input(msg_4)
            if len(answer) != 1 and answer not in "yn":
                continue
            elif answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        answer = input(eval(f"msg_{msg_index}"))
                        if len(answer) != 1 and answer not in "yn":
                            continue
                        elif answer == "y":
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = str(result)
                                break
                        elif answer == "n":
                            break
                else:
                    memory = str(result)
            elif answer == "n":
                pass

            answer = input(msg_5)

            if len(answer) != 1 and answer not in "yn":
                continue

            break

        if answer == "n":
            break
