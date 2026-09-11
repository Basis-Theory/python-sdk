from basis_theory.environment import BasisTheoryEnvironment


def test_environment_urls():
    """Pins the host each environment resolves to.

    US and EU both resolved to the compatibility host until the spec grew
    per-region servers, so the enum existed but selected nothing. These
    assertions fail if a regeneration collapses them back.
    """
    assert BasisTheoryEnvironment.DEFAULT.value == "https://api.basistheory.com"
    assert BasisTheoryEnvironment.US.value == "https://api.us.basistheory.com"
    assert BasisTheoryEnvironment.EU.value == "https://api.eu.basistheory.com"
    assert BasisTheoryEnvironment.TEST.value == "https://api.test.basistheory.com"


def test_regional_environments_are_distinct():
    urls = {env.value for env in BasisTheoryEnvironment}
    assert len(urls) == len(list(BasisTheoryEnvironment))
