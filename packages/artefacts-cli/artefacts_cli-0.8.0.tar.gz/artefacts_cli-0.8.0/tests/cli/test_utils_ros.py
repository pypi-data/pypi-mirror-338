from artefacts.cli.utils_ros import parse_tests_results


def test_parse_tests_results():
    # Create a XML file for testing
    test_file = "test.xml"
    results, _ = parse_tests_results(test_file)
    assert type(results) is list
    assert len(results) == 1
