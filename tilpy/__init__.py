from typing import TypeVar, Generic, Tuple, Type, Iterator, List, Any

T = TypeVar('T')


class Til(Generic[T]):
    _contents: Tuple[T, ...]
    _type: Type[T]

    def __init__(self, *elements: T, element_type: Type[T] = None, skip_typing = False):
        self._contents = elements
        self._type = element_type or type(elements[0])
        if not skip_typing:
            for element in self._contents:
                self._assert_type(element)

    def as_list(self) -> List[T]:
        return list(self._contents)

    def __eq__(self, other):
        if not isinstance(other, Til):
            return False
        return self._contents == other._contents

    def append(self, new_element: T):
        self._assert_type(new_element)
        return Til(*self._contents, new_element, element_type=self._type, skip_typing=True)

    def __iter__(self) -> Iterator[T]:
        return iter(self._contents)

    def __contains__(self, x: T) -> bool:
        return x in self._contents

    def _assert_type(self, element: Any):
        if not isinstance(element, self._type):
            raise TypeError("Elements must all be the same type")
