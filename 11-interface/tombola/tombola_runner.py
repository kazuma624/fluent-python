import doctest

from tombola import Tombola

# module to test
import bingo, lotto, tombolist, drum

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    # __subclasses__() はそのクラス直下のサブクラスをリストで返す。仮想サブクラスは含まれない
    real_subclasses = Tombola.__subclasses__()
    """
    _abc_registry で抽象クラスに登録された仮想サブクラスに弱参照を持つ WeakSet にバインドされる
    virtual_subclasses = list(Tombola._abc_registry)
    とあるが、 Python 3.9.5 だとエラー
    AttributeError: type object 'Tombola' has no attribute '_abc_registry'
    多分実装が変わってるのかな
    https://github.com/fluentpython/example-code-2e/blob/master/13-protocol-abc/tombola_runner.pyz
    """
    virtual_subclasses = [tombolist.TomboList]

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys
    main(sys.argv)
