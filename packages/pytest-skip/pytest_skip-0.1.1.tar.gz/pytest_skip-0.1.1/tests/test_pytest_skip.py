import pytest

TEST_CONTENT = """
    import pytest

    @pytest.mark.parametrize(
        ('a', 'b'),
        (
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
        )
    )
    def test_a(a, b):
        assert b in (1, 4)
"""

TEST_CONTENT_WITH_NESTED_BRACKETS = """
    import pytest

    @pytest.mark.parametrize(
        ('a', 'b'),
        (
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
        )
    )
    def test_a(a, b):
        assert b in (1, 4)

    @pytest.mark.parametrize(
        ('a', 'b'),
        (
            (1, 'a[1]'),
            (1, '2'),
            (1, '3'),
            (1, '4'),
        )
    )
    def test_b(a, b):
        assert b in ('a[1]', '4')
"""

SELECT_OPT = "--select-from-file"
DESELECT_OPT = "--deselect-from-file"
SKIP_OPT = "--skip-from-file"


@pytest.mark.parametrize("option_name", (SELECT_OPT, DESELECT_OPT))
def test_select_options_exist(testdir, option_name):
    selection_file_name = testdir.makefile(".txt", "test_a", "test_b")
    result = testdir.runpytest(option_name, selection_file_name)

    result.assert_outcomes()
    assert result.ret == 5


def test_select_options_conflict(testdir):
    result = testdir.runpytest(SELECT_OPT, "smth", DESELECT_OPT, "smth")

    assert result.ret == 4
    result.stderr.re_match_lines(
        [f"ERROR: '{SELECT_OPT}', '{DESELECT_OPT}' and '{SKIP_OPT}' cannot be used together."])


@pytest.mark.parametrize("option_name", (SELECT_OPT, DESELECT_OPT))
def test_missing_selection_file_fails(testdir, option_name):
    missing_file_name = "no_such_file.txt"
    result = testdir.runpytest(option_name, missing_file_name)

    assert result.ret == 4
    result.stderr.re_match_lines(
        [f"ERROR: Given selection file '{missing_file_name}' doesn't exist."])


@pytest.mark.parametrize(
    ("select_option", "select_content", "exit_code", "outcomes", "stdout_lines"),
    (
        (None, "", 1, {
            "passed": 2,
            "failed": 2
        }, []),
        (SELECT_OPT, ["test_a[1-1]", "test_a[1-4]"], 0, {
            "passed": 2
        }, []),
        (
            SELECT_OPT,
            ["{testfile}::test_a[1-2]", "test_a[1-4]"],
            1,
            {
                "passed": 1,
                "failed": 1
            },
            [],
        ),
        (
            SELECT_OPT,
            [
                "{testfile}::test_a[1-2]",
                "test_a[1-3]",
                "test_a[3-1]",
                "test_that_does_not_exist",
            ],
            1,
            {
                "failed": 2
            },
            [
                r".*Not all selected tests exist \(or have been deselected otherwise\).*",
                r"\s+Missing selected test names:",
                r"\s+- test_a\[3-1\]",
                r"\s+- test_that_does_not_exist",
            ],
        ),
        (DESELECT_OPT, ["test_a[1-1]", "test_a[1-4]"], 1, {
            "failed": 2
        }, []),
        (
            DESELECT_OPT,
            ["{testfile}::test_a[1-2]", "test_a[1-4]"],
            1,
            {
                "passed": 1,
                "failed": 1
            },
            [],
        ),
        (
            DESELECT_OPT,
            [
                "{testfile}::test_a[1-2]",
                "test_a[1-3]",
                "test_a[3-1]",
                "test_that_does_not_exist",
            ],
            0,
            {
                "passed": 2
            },
            [
                r".*Not all deselected tests exist \(or have been selected otherwise\).*",
                r"\s+Missing deselected test names:",
                r"\s+- test_a\[3-1\]",
                r"\s+- test_that_does_not_exist",
            ],
        ),
        (
            DESELECT_OPT,
            ["{testfile}::test_a"],
            5,
            {
                "passed": 0,
                "failed": 0
            },
            [],
        ),
        (
            SKIP_OPT,
            ["{testfile}::test_a"],
            0,
            {
                "skipped": 4
            },
            [],
        ),
        (
            SKIP_OPT,
            [
                "{testfile}::test_a[1-2]",
                "test_a[1-3]",
                "test_a[3-1]",
                "test_that_does_not_exist",
            ],
            0,
            {
                "passed": 2,
                "skipped": 2
            },
            [
                r".*Not all tests to skip exist \(or have been not skipped otherwise\).*",
                r"\s+Missing test names to skip:",
                r"\s+- test_a\[3-1\]",
                r"\s+- test_that_does_not_exist",
            ],
        ),
    ),
)
def test_tests_are_selected(  # pylint: disable=R0913, disable=R0917
    testdir,
    select_option,
    exit_code,
    select_content,
    outcomes,
    stdout_lines,
):
    testfile = testdir.makefile(".py", TEST_CONTENT)
    args = ["-v", "-Walways"]
    if select_option and select_content:
        select_file = testdir.makefile(
            ".txt",
            *[line.format(testfile=testfile.relto(testdir.tmpdir)) for line in select_content],
        )
        args.extend([select_option, select_file])
    result = testdir.runpytest(*args)

    assert result.ret == exit_code
    result.assert_outcomes(**outcomes)
    if stdout_lines:
        result.stdout.re_match_lines_random(stdout_lines)


@pytest.mark.parametrize("deselect", (False, True))
def test_fail_on_missing(testdir, deselect):
    testdir.makefile(".py", TEST_CONTENT)
    selectfile = testdir.makefile(".txt", "test_a[1-1]", "test_a[2-1]")
    result = testdir.runpytest(
        "-v",
        "--select-fail-on-missing",
        f"--{'de' if deselect else ''}select-from-file",  # pylint: disable=W1405
        selectfile,
    )
    assert result.ret == 4
    if deselect:
        first_line = r"pytest-skip: Not all deselected tests exist \(or have been selected otherwise\)."
        second_line = r"Missing deselected test names:"
    else:
        first_line = r"pytest-skip: Not all selected tests exist \(or have been deselected otherwise\)."
        second_line = r"Missing selected test names:"
    result.stderr.re_match_lines([
        first_line,
        second_line,
        # "  - test_a[2-1]",
    ])


@pytest.mark.parametrize(("fail_on_missing", "deselect"), [(True, False), (True, True),
                                                           (False, False), (False, True)])
def test_report_header(testdir, fail_on_missing, deselect):
    testdir.makefile(".py", TEST_CONTENT)
    selectfile = testdir.makefile(".txt", "test_a[1-1]")
    args = [
        "-v",
        f"--{'de' if deselect else ''}select-from-file",  # pylint: disable=W1405
        selectfile,
    ]
    if fail_on_missing:
        args.append("--select-fail-on-missing")
    result = testdir.runpytest(*args)

    failing_suffix = ", failing on missing selection items" if fail_on_missing else ""
    deselect_prefix = "de" if deselect else ""
    result.stdout.re_match_lines(
        [fr"select: {deselect_prefix}selecting tests from '{selectfile}'{failing_suffix}$"])


@pytest.mark.parametrize(
    ("option_name", "select_content", "exit_code", "outcomes"),
    [
        (
            DESELECT_OPT,
            ["{testfile}::test_a[1-2]", "test_a[1-4]", "# Ignore comment", ""],
            1,
            {
                "passed": 1,
                "failed": 1
            },
        ),
    ],
)
def test_comment_and_blanc_lines(testdir, option_name, select_content, exit_code, outcomes):
    testfile = testdir.makefile(".py", TEST_CONTENT)
    args = ["-v", "-Walways"]
    select_file = testdir.makefile(
        ".txt",
        *[line.format(testfile=testfile.relto(testdir.tmpdir)) for line in select_content],
    )
    args.extend([option_name, select_file])
    result = testdir.runpytest(*args)

    assert result.ret == exit_code
    result.assert_outcomes(**outcomes)


@pytest.mark.parametrize(
    ("option_name", "select_content", "exit_code", "outcomes"),
    [
        (
            DESELECT_OPT,
            [
                "{testfile}::test_a[1-2]",
                "test_a[1-4]",
                "{testfile}::test_b",
                "# Smth",
                "",
            ],
            1,
            {
                "passed": 1,
                "failed": 1
            },
        ),
    ],
)
def test_nested_brackets(testdir, option_name, select_content, exit_code, outcomes):
    testfile = testdir.makefile(".py", TEST_CONTENT_WITH_NESTED_BRACKETS)
    args = ["-v", "-Walways"]
    select_file = testdir.makefile(
        ".txt",
        *[line.format(testfile=testfile.relto(testdir.tmpdir)) for line in select_content],
    )
    args.extend([option_name, select_file])
    result = testdir.runpytest(*args)

    assert result.ret == exit_code
    result.assert_outcomes(**outcomes)
