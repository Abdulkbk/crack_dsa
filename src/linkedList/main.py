class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty Linked list")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0

        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next  # type: ignore
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # type: ignore
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(0)
            return

        if index == self.get_length() - 1:
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    llist = LinkedList()
    # llist.print()
    # llist.insert_at_beginning(8)
    # llist.insert_at_beginning(1)
    # llist.insert_at_end(7)
    llist.insert_values(["Banana", "Mango", "Orange"])
    llist.insert_at_beginning("Grape")
    llist.print()
    llist.remove_at(0)
    llist.insert_at(1, "Pineapple")
    llist.insert_at(0, "Lettuce")
    llist.insert_at(4, "Cabbage")
    print(llist.get_length())
    llist.print()
