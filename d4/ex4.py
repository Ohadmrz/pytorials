def sort_strings_by_len(strs_list: list[str]) -> list[str]:
    return list(sorted(strs_list, key=len))


if __name__ == '__main__':
    print(sort_strings_by_len(['clouds', 'sun', 'weather', 'rain', 'snow', 'heat', 'freeze']))