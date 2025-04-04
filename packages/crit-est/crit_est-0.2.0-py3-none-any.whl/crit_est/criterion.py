from abc import ABC, abstractmethod
import typing as t
import inspect

from sortedcontainers import SortedList



# criterion

Estimation = t.TypeVar("Estimation")

class Criterion(ABC, t.Generic[Estimation]):
	@abstractmethod
	def __call__(self, **attributes: t.Any) -> Estimation:
		pass
	


class ComparableCriterion(Criterion[Estimation]):
	@abstractmethod
	def __lt__(self, other: t.Any) -> bool:
		pass


	@abstractmethod
	def __hash__(self) -> int:
		pass



Predicate = t.Callable[..., bool]


class PredicatedCriterion(ComparableCriterion[Estimation]):
	def __init__(
		self,
		estimation: Estimation,
		predicate: Predicate,
	) -> None:
		self.estimation = estimation
		self.predicate = predicate


	@property
	def estimation(self) -> Estimation:
		return self.__estimation
	

	@estimation.setter
	def estimation(self, estimation: Estimation) -> None:
		self.__estimation = estimation


	@property
	def predicate(self) -> Predicate:
		return self.__pred


	@predicate.setter
	def predicate(self, predicate: Predicate) -> None:
		self.__pred = predicate


	def __call__(self, **attributes: t.Any) -> Estimation:
		requiredAttributes = self.getRequiredAttributes(**attributes)
		if self.predicate(**requiredAttributes):
			return self.__estimation
		raise AssertionError()


	def getRequiredAttributes(
		self, **attributes: t.Any
	) -> t.Mapping[str, t.Any]:
		signature = inspect.signature(self.predicate)
		requiredAttributeNames = signature.parameters.keys()
		return {
			name: attributes[name]
			for name in requiredAttributeNames
		}


	def __lt__(self, other: t.Any) -> bool:
		return \
			isinstance(other, PredicatedCriterion) \
			and self.__estimation < other.__estimation


	def __hash__(self) -> int:
		return hash(self.__estimation)



# decorators

class DefaultedCriterion(Criterion[Estimation]):
	def __init__(
		self, baseCriterion: Criterion[Estimation], defaultEst: Estimation
	) -> None:
		self.__baseCriterion = baseCriterion
		self.__defaultEst = defaultEst

	
	def __call__(self, **attributes: t.Any) -> Estimation:
		try:
			return self.__baseCriterion(**attributes)
		except AssertionError:
			return self.__defaultEst



class Suite(Criterion[Estimation]):
	def __init__(
		self,
		*additionalCriteria: Criterion[Estimation],
		criteria: t.Iterable[Criterion[Estimation]] = []
	):
		self.criteria = SortedList(criteria)
		self.criteria.update(additionalCriteria)


	def __call__(self, **attributes: t.Any) -> Estimation:
		for criterion in self.criteria:
			try:
				return criterion(**attributes)
			except AssertionError:
				pass
		raise AssertionError(self)
