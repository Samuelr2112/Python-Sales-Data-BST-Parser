import csv


# Represents a single bid record
class Bid:
    def __init__(self, bidId="", title="", fund="", amount=0.0):
        self.bidId = bidId
        self.title = title
        self.fund = fund
        self.amount = float(amount)

# Node for the Binary Search Tree
class Node:
    def __init__(self, bid):
        self.bid = bid
        self.left = None
        self.right = None

# Binary Search Tree to manage bids
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new bid into the tree
    def insert(self, bid):
        if not self.root:
            self.root = Node(bid)
        else:
            self._insert(self.root, bid)

    # Recursive insert helper
    def _insert(self, node, bid):
        if bid.bidId < node.bid.bidId:
            if node.left:
                self._insert(node.left, bid)
            else:
                node.left = Node(bid)
        else:
            if node.right:
                self._insert(node.right, bid)
            else:
                node.right = Node(bid)

    # Perform in-order traversal and print bids
    def in_order(self):
        self._in_order(self.root)

    # Recursive in-order helper
    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(f"{node.bid.bidId}: {node.bid.title} | ${node.bid.amount}")
            self._in_order(node.right)

    # Search for a bid by ID
    def search(self, bidId):
        return self._search(self.root, bidId)

    # Recursive search helper
    def _search(self, node, bidId):
        if not node:
            return None
        if node.bid.bidId == bidId:
            return node.bid
        elif bidId < node.bid.bidId:
            return self._search(node.left, bidId)
        else:
            return self._search(node.right, bidId)

# Load bid data from a CSV file
def load_bids(csv_path):
    bids = []
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bids.append(Bid(row['bidId'], row['title'], row['fund'], row['amount']))
    except FileNotFoundError:
        print("CSV file not found.")
    return bids

# Main program with command-line menu
def main():
    bst = BinarySearchTree()
    bids_loaded = False

    while True:
        print("\n=== Bid Management System ===")
        print("1. Load Bids from CSV")
        print("2. Display All Bids (In Order)")
        print("3. Search for a Bid by ID")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bids = load_bids("bids.csv")
            for bid in bids:
                bst.insert(bid)
            bids_loaded = True
            print(f"Loaded {len(bids)} bids.")

        elif choice == "2":
            if not bids_loaded:
                print("Please load bids first.")
            else:
                print("\nAll Bids:\n")
                bst.in_order()

        elif choice == "3":
            if not bids_loaded:
                print("Please load bids first.")
            else:
                bidId = input("Enter bid ID to search: ")
                bid = bst.search(bidId)
                if bid:
                    print(f"\nFound: {bid.bidId} | {bid.title} | {bid.fund} | ${bid.amount}")
                else:
                    print("Bid not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
