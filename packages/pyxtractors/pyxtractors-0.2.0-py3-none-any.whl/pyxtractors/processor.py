from abc import ABC, abstractmethod
import typing as t

import logging
import traceback



# base


Arg = t.TypeVar("Arg")
Result = t.TypeVar("Result")

class Processor(ABC, t.Generic[Arg, Result]):
	@abstractmethod
	def __call__(self, arg: Arg) -> Result:
		raise RuntimeError("Processor.__call__")



# children


class Returner(Processor[Arg, Result]):
	def __init__(self, value: Result) -> None:
		self.__value = value

	
	def __call__(self, _: Arg) -> Result:
		return self.__value



class Mirror(Processor[Arg, Arg]):
	def __call__(self, arg: Arg) -> Arg:
		return arg



# decorators


class SafeProcessor(Processor[Arg, Result]):
	def __init__(
		self,
		processor: Processor[Arg, Result],
		default: Result,
		toExcept: t.Tuple[t.Type[BaseException]] = (Exception,)
	) -> None:
		self.__processor = processor
		self.__default = default
		self.__toExcept = toExcept
		self.journal: t.List[BaseException] = []

	
	def __call__(self, arg: Arg) -> Result: 
		try:
			return self.__processor(arg)
		except self.__toExcept as err:
			logging.debug(traceback.format_exc())
			logging.error(err)
			self.journal.append(err)
			return self.__default



Key = t.TypeVar("Key")

class MassProcessor(
	Processor[Arg, t.Mapping[Key, Result]],
	t.Dict[Key, Processor[Arg, Result]]
):
	def __init__(
		self,
		extractors: t.Mapping[Key, Processor[Arg, Result]] = {},
		mappingFactory: t.Callable[
			[t.Iterable[t.Tuple[Key, Result]]],
			t.Mapping[Key, Result]
		] = dict,
		**kwextractors: Processor[Arg, Result]
	) -> None:
		super().__init__(extractors, **kwextractors)
		self.__mappingFactory = mappingFactory

	
	def __call__(self, arg: Arg) -> t.Mapping[Key, Result]:
		items = ((key, processor(arg)) for key, processor in self.items())
		return self.__mappingFactory(items)



class ProcessingChain(
	Processor[Arg, Result],
	t.List[Processor[Arg, Arg]]
):
	def __init__(
		self,
		*preproc: Processor[Arg, Arg],
		finalProc: Processor[Arg, Result],
		preprocContainer: t.Iterable[Processor[Arg, Arg]] = []
	) -> None:
		super().__init__(preproc)
		self.extend(preprocContainer)
		self.finalProc = finalProc

	
	def __call__(self, arg: Arg) -> Result:
		for proc in self:
			arg = proc(arg)
		return self.finalProc(arg)
