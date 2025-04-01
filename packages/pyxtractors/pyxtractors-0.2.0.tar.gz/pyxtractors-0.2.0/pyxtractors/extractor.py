import typing as t
import inspect

from .processor import Processor, Result



Key = t.TypeVar("Key")
Value = t.TypeVar("Value")
Mapping = t.Mapping[Key, Value]

Extractor = Processor[Mapping[Key, Value], Result]



class KeyExtractor(Extractor[Key, Value, Value]):
	def __init__(self, key: Key, default: Value) -> None:
		self.__key = key
		self.__default = default

	
	def __call__(self, mapping: Mapping[Key, Value]) -> Value:
		return mapping.get(self.__key, self.__default)



class HardKeyExtractor(Extractor[Key, Value, Value]):
	def __init__(self, key: Key) -> None:
		self.__key = key

	
	def __call__(self, mapping: Mapping[Key, Value]) -> Value:
		return mapping[self.__key]



class FuncExtractor(Extractor[str, Value, Result]):
	def __init__(self, func: t.Callable[..., Result]) -> None:
		self.__func = func


	def __call__(self, mapping: Mapping[str, Value]) -> Result:
		requiredParams = map(
			lambda name: (name, mapping[name]),
			self.getRequiredArgNames()
		)
		return self.__func(**dict(requiredParams))
		
	
	def getRequiredArgNames(self) -> t.Iterable[str]:
		signature = inspect.signature(self.__func)
		return signature.parameters.keys()