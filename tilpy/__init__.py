from types import GeneratorType
from typing import TypeVar, Generic, Tuple, Type, Iterator, List, Any, Generator, Union

import immutables

T = TypeVar('T')


class Til(Generic[T]):
    _contents: immutables.Map[T]
    _length: int
    _type: Type[T]

    def __init__(self, *elements: T, element_type: Type[T] = None):
        self._length = 0
        if not element_type and len(elements) == 0:
            raise SyntaxError("Empty TILs must have an explicit type")
        self._type = element_type or type(elements[0])

        with immutables.Map().mutate() as map_builder:
            for element in elements:
                self._assert_type(element)
                map_builder[self._length] = element
                self._length += 1
        self._contents = map_builder.finish()

    def as_list(self) -> List[T]:
        return list(self._contents.values())

    def __eq__(self, other):
        if not isinstance(other, Til):
            return False
        return self.as_list() == other.as_list()

    def append(self, new_element: T):
        self._assert_type(new_element)
        new_til = Til(element_type=self._type)
        new_til._contents = self._contents.set(self._length, new_element)
        new_til._length = self._length + 1
        return new_til

    def __iter__(self) -> Iterator[T]:
        return iter(self._contents.values())

    def __contains__(self, x: T) -> bool:
        return x in self.as_list()

    def __len__(self):
        return self._length

    def __reversed__(self):
        return Til(*reversed(self.as_list()), element_type=self._type)

    def _assert_type(self, element: Any):
        if not isinstance(element, self._type):
            raise TypeError("Elements must all be the same type")


def til(*generator_or_items: Union[Generator[T, None, None], T], element_type: Type[T] = None) -> Til[T]:
    if len(generator_or_items) == 0:
        return Til(element_type=element_type)
    if isinstance(generator_or_items[0], GeneratorType):
        contents = []
        for element in generator_or_items[0]:
            contents.append(element)
        return Til(*contents, element_type=element_type)
    # The first item wasn't a generator so we'll treat them as
    # a collection of elements to go in the list.
    contents = []
    for source in generator_or_items:
        contents.append(source)
    return Til(*contents, element_type=element_type)
