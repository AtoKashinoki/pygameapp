import pgapp
from pgapp.descriptor import ContainerValidateDecorator, ValidatorFramework


@ContainerValidateDecorator(int, initial_assignment=True)
class Test1(dict, ValidatorFramework):
    def validator(self, key: str | int | tuple, value: any) -> None: ...


@ContainerValidateDecorator(str, built_in_validate_key_types=(int, ))
class Test2(list, ValidatorFramework):
    def validator(self, key: str | int | tuple, value: any) -> None: ...


if __name__ == '__main__':
    test1 = Test1({"test2": "test2"})
    test1["test"] = 1
    print(test1)
    test2 = Test2()
    test2.append("test")
    print(test2)
