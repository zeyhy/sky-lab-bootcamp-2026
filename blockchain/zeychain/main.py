from blockchain import Blockchain
from transaction import Transaction


def show_menu():
    print("\n" + "=" * 40)
    print("              ZEYCHAIN")
    print("=" * 40)
    print("1. Create transaction")
    print("2. Mine pending transactions")
    print("3. Display blockchain")
    print("4. Validate blockchain")
    print("5. Show pending transactions")
    print("6. Exit")
    print("=" * 40)


def main():
    zeychain = Blockchain(difficulty=4)

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            sender = input("Sender: ")
            receiver = input("Receiver: ")

            try:
                amount = float(input("Amount (TL): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            transaction = Transaction(
                sender,
                receiver,
                amount
            )

            zeychain.add_transaction(transaction)

            print("\nTransaction added successfully!")
            print(transaction)

        elif choice == "2":
            zeychain.mine_pending_transactions()

        elif choice == "3":
            zeychain.display_chain()

        elif choice == "4":
            if zeychain.is_chain_valid():
                print("\n✓ Blockchain is valid.")
            else:
                print("\n✗ Blockchain is NOT valid.")

        elif choice == "5":
            if not zeychain.pending_transactions:
                print("\nThere are no pending transactions.")
            else:
                print("\nPending Transactions:")

                for transaction in zeychain.pending_transactions:
                    print(
                        f"{transaction['sender']} -> "
                        f"{transaction['receiver']}: "
                        f"{transaction['amount']} TL"
                    )

        elif choice == "6":
            print("\nZeyChain closed.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()