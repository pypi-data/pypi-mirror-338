"""Tests for the autograder module"""

import matplotcheck.autograde as ag


def test_autograde_runs_assert_pass(pt_scatter_plt):
    """Test that a normal test is run with autograder and passes"""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["Plot"],
    )
    assert result["description"] == "assert_title_contains"
    assert result["pass"]
    assert result["message"] == "default correct"
    assert result["points"] == 2


def test_autograde_runs_assert_fail(pt_scatter_plt):
    """Test that a when a test fails, an assertion error is returned"""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["NotAWord"],
    )
    assert result["description"] == "assert_title_contains"
    assert not result["pass"]
    assert result["message"] == "default error"
    assert result["points"] == 0
    assert isinstance(result["traceback"], AssertionError)


def test_autograde_runs_assert_pass_custom_message(pt_scatter_plt):
    """Test that when a custom message is provided, it is correctly returned
    to the user."""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["Plot"],
        correct_message="This is correct!",
    )
    assert result["message"] == "This is correct!"


def test_autograde_runs_assert_fail_custom_message(pt_scatter_plt):
    """Test that a custom message for a failed test gets returned"""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["NotAWord"],
        error_message="This is wrong!",
    )
    assert result["message"] == "This is wrong!"


def test_output_results_pass(pt_scatter_plt, capsys):
    """Test that the correct number of points are returned when a test
    passes"""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["Plot"],
    )
    assert 2 == ag.output_results([result])
    assert (
        "Results for test 'assert_title_contains':\n"
        " Pass! default correct (2 points)\n" == capsys.readouterr().out
    )


def test_output_results_fail(pt_scatter_plt, capsys):
    """Test that the correct points are returned when a test fails"""
    result = ag.run_test(
        pt_scatter_plt.assert_title_contains,
        points=2,
        strings_expected=["NotAWord"],
    )
    assert 0 == ag.output_results([result])
    assert (
        "Results for test 'assert_title_contains':\n"
        " Fail! default error (0 points)\n"
        " Traceback: Title does not contain expected string: NotAWord\n"
        == capsys.readouterr().out
    )
