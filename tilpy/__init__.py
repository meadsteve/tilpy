from copy import copy
from types import GeneratorType
from typing import TypeVar, Generic, Tuple, Type, Iterator, List, Any, Generator, Union

T = TypeVar('T')


class Til(Generic[T]):
    _contents: List[T]
    _type: Type[T]

    def __init__(self, *elements: T, element_type: Type[T] = None, skip_typing=False):
        self._contents = list(elements)
        if not element_type and len(elements) == 0:
            raise SyntaxError("Empty TILs must have an explicit type")
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
        new_til = Til(element_type=self._type, skip_typing=True)
        new_til._contents = copy(self._contents)
        new_til._contents.append(new_element)
        return new_til

    def __iter__(self) -> Iterator[T]:
        return iter(self._contents)

    def __contains__(self, x: T) -> bool:
        return x in self._contents

    def __len__(self):
        return len(self._contents)

    def __reversed__(self):
        return Til(*reversed(self._contents), element_type=self._type, skip_typing=True)

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
