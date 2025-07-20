# custom list implementation - self
class MyList:

    def __init__(self, data):
        if data:
            self._data = data
        else:
            self._data = []

    def __getitem__(self, idx):
        if len(self._data) > idx:
            return self._data[idx]
        return False

    def __setitem__(self, key, value):
        if len(self._data) > key:
            self._data[key] = value
            return True
        return False

    def __contains__(self, item):
        return item in self._data

    def __delitem__(self, key):
        if len(self._data) > key:
            del self._data[key]
            return True
        return False

    def __repr__(self):
        return "Custom List : " + str(self._data)

    def __str__(self):
        return str(self._data)



def main():
    mList1 = MyList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(mList1[8])
    mList1[8] = 100
    print(mList1[8])
    print(2 in mList1)
    print('myList():\n', mList1)
    del mList1[2]
    print('myList():\n', mList1)


if __name__ == '__main__':
    main()


