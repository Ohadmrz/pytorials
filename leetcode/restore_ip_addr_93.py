def restore_ip_addresses(s: str) -> list[str]:
    if len(s) > 12 or len(s) < 4:
        return []

    restore_options = []
    # _restore_ips_rec(s, 4, restore_options, [""])
    _restore_ips_rec(s, 4, restore_options, [])

    print(restore_options)


def _is_valid_ip_part(s: str):
    return 0 <= int(s) <= 255 and ((int(s) == 0 and len(s) == 1) or not s.startswith('0'))



def _restore_ips_rec(s: str, ip_digits_num: int, restore_options: list[str], curr_ip: list):

    # stop condition - if the string is empty, and we need to detect 0 ip parts,
    # then the current restoration succeeded, and we can append the curr_ip to the list
    if not s and ip_digits_num == 0:
        restore_options.append(".".join(curr_ip))
    else:
        # iterate from 1 to 3 possible digits, or less if the string is shorter
        for i in range(1, min(4, len(s)+1)):

            # check whether we have valid first ip part
            if _is_valid_ip_part(s[:i]):

                # add current part to the ip
                curr_ip.append(s[:i])

                # run recursively on the remainder of the ip
                _restore_ips_rec(s[i:], ip_digits_num-1, restore_options, curr_ip)

                # remove current (last) part of the ip
                curr_ip.pop()



if __name__ == '__main__':
    restore_ip_addresses('101023')
    restore_ip_addresses("25525511135")
    restore_ip_addresses("0000")