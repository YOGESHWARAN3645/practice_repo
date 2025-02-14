
import pytest
import main  # Import your main.py file

def test_print_output(monkeypatch):
    # Capture the printed output
    captured = monkeypatch.stdout
    main()  # Run the main function
    assert captured == "Hi YOGESH\n"
