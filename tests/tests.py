from abc import ABC

import pgapp


if __name__ == '__main__':
    tuple(["test"])
    test_conf = pgapp.config.Config(file_path="tests/test.config")
    test_conf.write()
    print(test_conf)
