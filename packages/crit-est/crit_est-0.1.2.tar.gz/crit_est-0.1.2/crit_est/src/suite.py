from abc import ABC, abstractmethod
import typing as t

from sortedcontainers import SortedSet



# criterion

Estimand = t.TypeVar("Estimand")
Predicate = t.Callable[[Estimand], bool]
Estimation = t.TypeVar("Estimation")

class Criterion(t.Generic[Estimand, Estimation]):
	def __init__(self, estimation: Estimation, pred: Predicate) -> None:
		self.__estimation = estimation
		self.__pred = pred


	def __lt__(self, other: t.Any) -> bool:
		if isinstance(other, Criterion):
			return self.__estimation < other.__estimation
		raise TypeError(Criterion.__lt__, other)


	def __hash__(self) -> int:
		return hash(self.__estimation)

	
	def __call__(self, estimand: Estimand) -> Estimation:
		if self.__pred(estimand):
			return self.__estimation
		raise AssertionError(self)



# suite base class

class Suite(ABC, t.Generic[Estimand, Estimation]):
	@abstractmethod
	def __call__(self, estimand: Estimand) -> Estimation:
		pass



class SuiteFactory(ABC, t.Generic[Estimand, Estimation]):
	@abstractmethod
	def __call__(self) -> Suite[Estimand, Estimation]:
		raise NotImplementedError(SuiteFactory.__call__)



# minimal suite implementation

class BasicSuite(SortedSet, Suite[Estimand, Estimation]):
	def __init__(
		self,
		*additionalCriteria: Criterion[Estimand, Estimation],
		criteria: t.Iterable[Criterion[Estimand, Estimation]] = []
	) -> None:
		super().__init__(criteria)
		self.update(additionalCriteria)


	def __call__(self, estimand: Estimand) -> Estimation:
		for criterion in self:
			try:
				return criterion(estimand)
			except AssertionError:
				pass
		raise AssertionError(self)


class BasicSuiteFactory(SuiteFactory[Estimand, Estimation]):
	@abstractmethod
	def getCriteria(self) -> t.Iterable[Criterion[Estimand, Estimation]]:
		raise NotImplementedError()

	
	def __call__(self) -> Suite[Estimand, Estimation]:
		criteria = self.getCriteria()
		return BasicSuite(criteria=criteria)



# decorators

class DefaultedSuite(Suite[Estimand, Estimation]):
	def __init__(
		self, baseSuite: Suite[Estimand, Estimation], defaultEst: Estimation
	) -> None:
		self.__baseSuite = baseSuite
		self.__defaultEst = defaultEst

	
	def __call__(self, estimand: Estimand) -> Estimation:
		try:
			return self.__baseSuite(estimand)
		except AssertionError:
			return self.__defaultEst


class DefaultedSuiteFactory(SuiteFactory[Estimand, Estimation]):
	def __init__(
		self,
		baseSuiteFactory: SuiteFactory[Estimand, Estimation],
		defaultEst: Estimation
	) -> None:
		self.baseSuiteFactory = baseSuiteFactory
		self.defaultEst = defaultEst

	
	def __call__(self) -> Suite[Estimand, Estimation]:
		baseSuite = self.baseSuiteFactory()
		return DefaultedSuite(baseSuite, self.defaultEst)



class ValidatedSuite(Suite[Estimand, Estimation]):
	def __init__(self, baseSuite: Suite[Estimand, Estimation]) -> None:
		self.__baseSuite = baseSuite

	
	def __call__(self, estimand: Estimand) -> Estimation:
		self.validateEstimand(estimand)
		return self.__baseSuite(estimand)


	@abstractmethod
	def validateEstimand(self, estimand: Estimand) -> bool:
		raise NotImplementedError()
