import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            # key が　str であるのに見つかってないのであれば KeyError を発生させる
            raise KeyError(key)
        # key から str を生成し、サーチする
        return self[str(key)]

    def __contains__(self, key):
        # 格納されているキーはすべて str であると仮定できる
        return key in self.data

    def __setitem__(self, key, item):
        # 全ての key を str に変換する
        self.data[str(key)] = item


if __name__ == '__main__':
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d['4'])
    # print(d['1'])

    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))

    # print(2 in d)
    # print(1 in d)
