def task2():
    line = input()
    # Реализуем автоматический выход, если была передана пустая строка
    while rule := input():
        from_, to_ = rule.split("->")
        print(line := line.replace(from_, to_))


if __name__ == "__main__":
    task2()
