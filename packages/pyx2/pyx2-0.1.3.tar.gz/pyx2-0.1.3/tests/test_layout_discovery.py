"""Test layout auto-discovery functionality."""

import pytest
from pathlib import Path
from typing import Dict

from pyxie.pyxie import Pyxie
from pyxie.layouts import registry


@pytest.fixture
def test_paths(tmp_path: Path) -> Dict[str, Path]:
    """Create test directory structure for layout discovery."""
    paths = {
        'app_root': tmp_path / "app",
        'content': tmp_path / "app" / "content",
        'layouts': tmp_path / "app" / "layouts",
        'templates': tmp_path / "app" / "templates",
        'static': tmp_path / "app" / "static",
        'static_subdir': tmp_path / "app" / "static" / "components",
        'cache': tmp_path / "app" / "cache"
    }
    
    # Create all directories
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
        
    return paths


@pytest.fixture(autouse=True)
def clear_registry():
    """Clear the layout registry before each test and restore it after."""
    # Save existing layouts
    saved_layouts = registry._layouts.copy()
    
    # Clear registry
    registry._layouts.clear()
    
    yield
    
    # Restore previous layouts
    registry._layouts.clear()
    registry._layouts.update(saved_layouts)


def create_layout_file(path: Path, name: str, layout_name: str = "test_layout") -> None:
    """Create a Python file with a layout function."""
    content = f"""
from pyxie.layouts import layout
from fastcore.xml import Div, H1, FT

@layout("{layout_name}")
def {name}_layout(title="Default Title") -> FT:
    return Div(
        H1(title),
        Div(None, data_slot="content"),
        cls="test-layout {name}-layout"
    )
"""
    path.write_text(content)


def test_autodiscover_root(test_paths):
    """Test auto-discovery of layouts in the root directory."""
    # Create a layout in the root directory
    create_layout_file(test_paths['app_root'] / "main.py", "main", "root_layout")
    
    # Initialize Pyxie with auto-discovery
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache']
    )
    
    # Check if the layout was discovered
    assert "root_layout" in registry._layouts
    assert registry._layouts["root_layout"].name == "root_layout"


def test_autodiscover_layouts_dir(test_paths):
    """Test auto-discovery of layouts in the layouts directory."""
    # Create layouts in the layouts directory
    create_layout_file(test_paths['layouts'] / "blog.py", "blog", "blog_layout")
    create_layout_file(test_paths['layouts'] / "page.py", "page", "page_layout")
    
    # Initialize Pyxie with auto-discovery
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache']
    )
    
    # Check if layouts were discovered
    assert "blog_layout" in registry._layouts
    assert "page_layout" in registry._layouts


def test_autodiscover_subdirectories(test_paths):
    """Test auto-discovery of layouts in subdirectories."""
    # Create a layout in a subdirectory
    test_paths['static_subdir'].mkdir(exist_ok=True)
    create_layout_file(test_paths['static_subdir'] / "component.py", "component", "component_layout")
    
    # Initialize Pyxie with auto-discovery
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache']
    )
    
    # Check if the layout was discovered
    assert "component_layout" in registry._layouts


def test_autodiscover_custom_paths(test_paths):
    """Test auto-discovery with custom layout paths."""
    # Create a custom directory
    custom_dir = test_paths['app_root'] / "custom_layouts"
    custom_dir.mkdir()
    
    # Create a layout in the custom directory
    create_layout_file(custom_dir / "custom.py", "custom", "custom_layout")
    
    # Initialize Pyxie with custom layout path
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache'],
        layout_paths=[custom_dir]
    )
    
    # Check if the layout was discovered
    assert "custom_layout" in registry._layouts


def test_autodiscover_disabled(test_paths):
    """Test disabling auto-discovery."""
    # Create layouts in various places
    create_layout_file(test_paths['app_root'] / "main.py", "main", "root_layout")
    create_layout_file(test_paths['layouts'] / "page.py", "page", "page_layout")
    
    # Initialize Pyxie with auto-discovery disabled
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache'],
        auto_discover_layouts=False
    )
    
    # Verify no layouts were discovered
    assert "root_layout" not in registry._layouts
    assert "page_layout" not in registry._layouts


def test_autodiscover_error_handling(test_paths):
    """Test error handling during auto-discovery."""
    # Create an invalid layout file
    invalid_file = test_paths['layouts'] / "invalid.py"
    invalid_file.write_text("This is not valid Python code :")
    
    # Create a valid layout file
    create_layout_file(test_paths['layouts'] / "valid.py", "valid", "valid_layout")
    
    # Initialize Pyxie - should handle the error gracefully
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache']
    )
    
    # Check that valid layout was discovered despite the error
    assert "valid_layout" in registry._layouts


def test_autodiscover_nonexistent_directory(test_paths):
    """Test auto-discovery with nonexistent directory."""
    # Create a valid layout file
    create_layout_file(test_paths['layouts'] / "valid.py", "valid", "valid_layout")
    
    # Initialize Pyxie with a nonexistent directory
    nonexistent_dir = test_paths['app_root'] / "nonexistent"
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache'],
        layout_paths=[nonexistent_dir]
    )
    
    # Check that valid layout was discovered despite the nonexistent directory
    assert "valid_layout" in registry._layouts


def test_multiple_layouts_in_file(test_paths):
    """Test discovering multiple layouts in a single file."""
    # Create a file with multiple layouts
    multiple_file = test_paths['layouts'] / "multiple.py"
    content = """
from pyxie.layouts import layout
from fastcore.xml import Div, H1, FT

@layout("layout1")
def layout_one(title="Layout One") -> FT:
    return Div(H1(title), cls="layout-one")

@layout("layout2")
def layout_two(title="Layout Two") -> FT:
    return Div(H1(title), cls="layout-two")
"""
    multiple_file.write_text(content)
    
    # Initialize Pyxie
    Pyxie(
        content_dir=test_paths['content'],
        cache_dir=test_paths['cache']
    )
    
    # Check that both layouts were discovered
    assert "layout1" in registry._layouts
    assert "layout2" in registry._layouts


def test_autodiscover_excludes_cache_files(tmp_path):
    """Test that __pycache__ directories and .pyc files are excluded."""
    # Create a layout directory with cache files
    layout_dir = tmp_path / "layouts"
    layout_dir.mkdir()

    # Create a valid layout file
    valid_layout = layout_dir / "valid.py"
    valid_layout.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("valid")
def valid_layout():
    return Div("Valid layout")
""")

    # Create __pycache__ directory with .pyc file
    pycache_dir = layout_dir / "__pycache__"
    pycache_dir.mkdir()
    pyc_file = pycache_dir / "valid.cpython-311.pyc"
    pyc_file.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("invalid_cache")
def invalid_layout():
    return Div("Invalid layout")
""")

    # Create a .pyc file directly in layouts
    direct_pyc = layout_dir / "direct.pyc"
    direct_pyc.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("invalid_direct")
def invalid_layout():
    return Div("Invalid layout")
""")

    # Initialize Pyxie with auto-discovery
    Pyxie(tmp_path, auto_discover_layouts=True, layout_paths=[layout_dir])

    # Verify only the valid layout was registered
    assert "valid" in registry._layouts
    assert "invalid_cache" not in registry._layouts
    assert "invalid_direct" not in registry._layouts
    assert len(registry._layouts) == 1


def test_autodiscover_excludes_hidden_files(tmp_path):
    """Test that hidden files and directories are excluded."""
    # Create a layout directory
    layout_dir = tmp_path / "layouts"
    layout_dir.mkdir()

    # Create a valid layout file
    valid_layout = layout_dir / "valid.py"
    valid_layout.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("valid")
def valid_layout():
    return Div("Valid layout")
""")

    # Create hidden files and directories
    hidden_file = layout_dir / ".hidden.py"
    hidden_file.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("invalid_hidden")
def invalid_layout():
    return Div("Invalid layout")
""")

    hidden_dir = layout_dir / ".hidden"
    hidden_dir.mkdir()
    hidden_layout = hidden_dir / "layout.py"
    hidden_layout.write_text("""
from pyxie.layouts import layout
from fastcore.xml import Div

@layout("invalid_hidden_dir")
def invalid_layout():
    return Div("Invalid layout")
""")

    # Initialize Pyxie with auto-discovery
    Pyxie(tmp_path, auto_discover_layouts=True, layout_paths=[layout_dir])

    # Verify only the valid layout was registered
    assert "valid" in registry._layouts
    assert "invalid_hidden" not in registry._layouts
    assert "invalid_hidden_dir" not in registry._layouts
    assert len(registry._layouts) == 1 