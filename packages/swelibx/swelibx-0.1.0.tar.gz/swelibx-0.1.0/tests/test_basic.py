from swelibx.patch_utils import generate_unified_diff


def test_generate_unified_diff():
    old_code = "print('Hello, world!')"
    new_code = "print('Hello, world!')"
    diff = generate_unified_diff(old_code, new_code)
    assert diff == "", "Diff should be empty"
