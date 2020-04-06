from typing import TypeVar, Generic, Tuple, Type, Iterator, List

T = TypeVar('T')


class Til(Generic[T]):
    _contents: Tuple[T, ...]
    _type: Type[T]

    def __init__(self, *elements: T, element_type:Type[T]=None):
        self._contents = elements
        self._type = element_type or type(elements[0])
        for element in self._contents:
            if type(element) is not self._type:
                raise TypeError("Elements must all be the same type")

    def as_list(self) -> List[T]:
        return list(self._contents)

    def __eq__(self, other):
        if not isinstance(other, Til):
            return False
        return self._contents == other._contents

    def append(self, new_element: T):
        new_conents = (list(self._contents) + [new_element])
        return Til(*new_conents, element_type=self._type)

    def __iter__(self) -> Iterator[T]:
        return iter(self._contents)

    def __contains__(self, x: T) -> bool:
        return x in self._contents
