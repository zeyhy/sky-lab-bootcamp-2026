from block import Block


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(
            index=0,
            transactions=[],
            previous_hash="0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction.to_dict())

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            print("There are no pending transactions.")
            return

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash,
            difficulty=self.difficulty
        )

        print(f"\nMining Block #{new_block.index}...")
        new_block.mine_block()

        self.chain.append(new_block)
        self.pending_transactions = []

        print("Block successfully added to blockchain.\n")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        print("\n" + "=" * 50)
        print("                 BLOCKCHAIN")
        print("=" * 50)

        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)