import re


def validate_ticket(rows: int, seats_in_row: int, ticket: str):
    # numbers [A-G]
    # 52
    # 1-9 8A / 3C
    # 1-4 | 0-9 -> 10 => 49
    # 5 | 0-2

    if rows < 10:
        digits = r"[1-9]"
        # [1-9][A-G]
    else:
        msn = rows // 10
        lsn = rows % 10
        # [1-9] | [1-4][0-9] | 5[0-2]
        digits = f"(([1-9])|([1-{msn-1}][0-9])|({msn}[0-{lsn}]))"

    last_letter = chr(ord('A') + seats_in_row)
    r = re.compile(f"{digits}[A-{last_letter}]")
    print(r)
    return r.match(ticket)


if __name__ == '__main__':
    print(validate_ticket(52, 6, '5B'))
    print(validate_ticket(52, 6, '53B'))
    print(validate_ticket(52, 6, '49D'))