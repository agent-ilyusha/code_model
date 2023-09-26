# --coding: utf-8
from typing import List


def detective(code: str) -> List[str]:
    """
    this is code is search all code +- 1 vertical/horizontal line
    :param code:
    :return:
    """
    keyboard = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['', '0', '']
    ]
    code_set = list(sym for sym in code)
    mb_code_list = list()  # mb -> may be
    for sym_i, sym in enumerate(code_set):
        for line_i, line in enumerate(keyboard):
            code_list = list(code_set)
            if sym in line:
                num_i = line.index(sym)
                if num_i != 0 and num_i != 2 and line_i == 0:
                    code_list[sym_i] = keyboard[line_i][num_i - 1]
                    mb_code_list.append(''.join(code_list))

                    code_list[sym_i] = keyboard[line_i + 1][num_i]
                    mb_code_list.append(''.join(code_list))

                    code_list[sym_i] = keyboard[line_i][num_i + 1]
                    mb_code_list.append(''.join(code_list))

                if num_i != 0 and line_i != 0 and num_i != 2 and line_i != 3:
                    code_list[sym_i] = keyboard[line_i - 1][num_i]
                    mb_code_list.append(''.join(code_list))

                    code_list[sym_i] = keyboard[line_i][num_i - 1]
                    mb_code_list.append(''.join(code_list))

                    code_list[sym_i] = keyboard[line_i + 1][num_i]
                    mb_code_list.append(''.join(code_list))

                    code_list[sym_i] = keyboard[line_i][num_i + 1]
                    mb_code_list.append(''.join(code_list))

    return mb_code_list


if __name__ == '__main__':
    print("Возможные коды: " + ', '.join(detective('52')))