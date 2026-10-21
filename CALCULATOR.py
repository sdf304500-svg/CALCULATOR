def calculator():
    print("--- Mini Python Calculator ---")

    while True:
        print("\nSelect an operation:")
        print("1. додати (+)")
        print("2. відняти (-)")
        print("3. множити (*)")
        print("4. ділити (/)")
        print("5. вийти")

        choice = input("Введіть вибір (1/2/3/4/5): ").strip()

        if choice == '5':
            print("До зустрічі:)")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Неприпустимий вибір ! Будь ласка, оберіть  1, 2, 3, 4, або 5.")
            continue

        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("ПоМиЛкА ._. : Будь ласка, обирайте тількі числа!")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("ПоМиЛкА ._. : Не можна ділити на нуль!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")


if __name__ == "__main__":
    calculator()
