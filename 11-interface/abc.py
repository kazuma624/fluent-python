import abc

class SampleABC(abc.ABC):

    @abc.abstractmethod
    def hoge(self):
        """hoge method"""

class Smaple(SampleABC):

    # def hoge(self):
    #     print('hogehoge')

    def fuga(self):
        print('fugafuga')


def main():
    # a = SampleABC()
    # a.hoge()
    b = Smaple()
    # b.hoge()
    b.fuga()


if __name__ == '__main__':
    main()
