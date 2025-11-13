import os
import sys
import pytest

# Ensure the src directory is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import print_structure, trim_dictionary, build_structure


# --- Fixtures -----------------------------------------------------------------

@pytest.fixture
def mock_src(tmp_path):
    src = tmp_path / "src"
    components = src / "components"
    components.mkdir(parents=True)
    (components / "App.jsx").write_text("")
    (src / "main.jsx").write_text("")
    return src


@pytest.fixture
def mock_test1(tmp_path):
    test1 = tmp_path / "test1"
    images = test1 / "images"
    images.mkdir(parents=True)
    for name in [
        "f9b366a76e4c6a74_jpg.rf.9f4be57b21ebedb7600831e1091c788d.jpg",
        "4b3dc989762088ec_jpg.rf.ad207fff1623cc3e4956684c1e052e36.jpg",
        "376aa7453cb2a506_jpg.rf.8753e6fca01deb3c18b979f3226805ca.jpg",
        "80045832db4c7299_jpg.rf.e14ec257699e9af223e6fb30459333ea.jpg",
        "cdbc0ab2dd1ae3c5_jpg.rf.f60e59e9a1763f1f3d8803038baca8c7.jpg",
        "a191ee873b7096a2_jpg.rf.42a13d35d67cd418d3ccbf15fe249058.jpg",
        "be273036add61d83_jpg.rf.448df7336df3b366423b2c87f38ca8c6.jpg",
        "73d763d3db3093d5_jpg.rf.b23078bc098424cc0ea03a6282db927d.jpg",
        "1ff81e1a8a7a60d9_jpg.rf.ff0879dfecb967902dae02e5f025ec47.jpg",
        "475481b3737b7d38_jpg.rf.40566cfb8a813bc9411d70714a89ff8c.jpg",
    ]:
        (images / name).write_text("")
    (test1 / "file1.txt").write_text("")
    (test1 / "file.py").write_text("")
    (test1 / "file.js").write_text("")
    return test1


# --- Tests --------------------------------------------------------------------

def test_build_structure(mock_src):
    expected = {
        "src": {
            "components": {"App.jsx": None},
            "main.jsx": None,
        }
    }
    result = {"src": build_structure(str(mock_src))}
    assert result == expected


def test_trim_dictionary(mock_test1):
    expected = {
        "test1": {
            "images": {name: None for name in os.listdir(mock_test1 / "images")},
            "file1.txt": None,
            "file.py": None,
            "file.js": None,
        }
    }
    structure = build_structure(str(mock_test1))
    trimmed = trim_dictionary(structure, 10)
    result = {"test1": trimmed}
    assert result == expected


def test_print_structure_simple():
    structure = {
        "src": {
            "components": {"App.jsx": None},
            "main.jsx": None,
        }
    }

    expected_output = (
        "src/\n"
        "├── components/\n"
        "│   └── App.jsx\n"
        "└── main.jsx\n"
    )

    result = print_structure(structure)
    assert result == expected_output
