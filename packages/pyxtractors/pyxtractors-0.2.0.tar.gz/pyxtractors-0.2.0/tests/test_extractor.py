import pytest

import typing as t

from pyxtractors import \
	KeyExtractor, HardKeyExtractor, SafeProcessor, FuncExtractor, \
	MassProcessor, ProcessingChain



@pytest.fixture
def data() -> t.Mapping[str, t.Any]:
	return {
		"first-name": "John",
		"last-name": "Doe",
		"age": 32,
		"address": {
			"country": "UK",
			"street": "Baker st."
		},
		"married": True
	}



def testExtractByKey(data):
	extractor = KeyExtractor("last-name", None)
	assert "Doe" == extractor(data)



def testExtractWithDefault(data):
	basicExtractor = HardKeyExtractor("middle-name")
	extractor = SafeProcessor(basicExtractor, "UNKNOWN")
	assert "UNKNOWN" == extractor(data)
	assert isinstance(extractor.journal[0], KeyError)



def testExtractTransformed(data):
	extractor = FuncExtractor(lambda age: "even" if age % 2 == 0 else "odd")
	assert "even" == extractor(data)



def testMassExtraction(data):
	countryNames = {
		"FR": "France",
		"US": "United States",
		"UK": "United Kingdom"
	}

	extractor = MassProcessor[t.Mapping[str, t.Any], str, t.Any]({
			"name": KeyExtractor("first-name", None),
			"surname": KeyExtractor("last-name", None)
		},
		old = FuncExtractor(lambda age: age >= 60),
		country = ProcessingChain(
			KeyExtractor[str, t.Any]("address", {"country": "UNKNOWN"}),
			finalProc=FuncExtractor(lambda country: str(countryNames[country]))
		)
	)

	expected: t.Dict[str, t.Any] = {
		"name": "John",
		"surname": "Doe",
		"old": False,
		"country": "United Kingdom"
	}

	extracted = extractor(data)
	assert expected == extracted
