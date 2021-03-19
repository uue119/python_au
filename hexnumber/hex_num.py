from copy import deepcopy


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = char_to_num(value)
        self.next = next


class HexNumber:
    def __init__(self, string=None) -> None:
        if check_num(string):
            num = list(string)
            self.last_dec = Node(num[-1])
            cur = self.last_dec
            for i in range(len(num) - 2, -1, -1):
                cur.next = Node(num[i])
                cur = cur.next
            self.len = len(string)
        else:
            print('Некорректный ввод')
            exit()

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        res = ''
        cur = self.last_dec
        while cur:
            res += num_to_char(cur.value)
            cur = cur.next
        return res[::-1]

    def __add__(self, other):
        if len(self) >= len(other):
            res = deepcopy(self)
        else:
            res = deepcopy(other)
        pointer1 = res.last_dec
        pointer2 = other.last_dec
        while pointer1 and pointer2:
            pointer1.value += pointer2.value
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        res.hex_place()
        return res

    def hex_place(self) -> None:
        cur = self.last_dec
        while (cur):
            if (cur.value > 15):
                if cur.next:
                    cur.next.value += 1
                    cur.value -= 16
                else:
                    cur.next = Node('1')
                    cur.value -= 16
            cur = cur.next


def check_num(string) -> bool:
    for char in string:
        if not check_char(char):
            return False
    return True


def check_char(char) -> bool:
    if char.isdecimal() or char.isupper():
        return True
    return False


def char_to_num(char) -> hex:
    if ord(char) - ord('A') < 0:
        return int(char)
    return int(ord(char) - ord('A') + 10)


def num_to_char(num) -> str:
    if num < 10:
        return str(num)
    return chr(num - 10 + ord('A'))
