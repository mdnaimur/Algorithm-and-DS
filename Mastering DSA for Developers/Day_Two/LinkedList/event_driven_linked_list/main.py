from linked_list.SingleLinkList import SingleLinkList

from events.Handler import handle_insert, handle_delete, handle_update


def main():
    lst = SingleLinkList()
    lst.set_on_insert(handle_insert)
    lst.set_on_update(handle_update)
    lst.set_on_delete(handle_delete)

    lst.insert(10)
    lst.insert(20)
    lst.insert(30)
    lst.insert(50)
    lst.insert(36)
    lst.insert(90)

    print("Current list", lst)
    lst.delete(10)
    print("affter normal delete", lst)
    lst.update(45, 2)
    print("afater update: ", lst)


if __name__ == "__main__":
    main()
