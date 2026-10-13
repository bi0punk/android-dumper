from app import get_android_data_directories


def test_returns_expected_categories(tmp_path):
    (tmp_path / "DCIM").mkdir()
    (tmp_path / "Download").mkdir()

    result = get_android_data_directories(root_path=str(tmp_path))

    assert result["Images"]
    assert result["Downloads"]
    assert result["Videos"] == []
