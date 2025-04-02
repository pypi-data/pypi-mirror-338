import platform_checker.detector as detector

def test_is_windows():
    assert isinstance(detector.is_windows(), bool)

def test_is_mac():
    assert isinstance(detector.is_mac(), bool)

def test_is_linux():
    assert isinstance(detector.is_linux(), bool)

def test_is_wsl():
    assert isinstance(detector.is_wsl(), bool)

def test_is_unix():
    assert isinstance(detector.is_unix(), bool)

def test_is_posix():
    assert isinstance(detector.is_posix(), bool)

def test_is_arm():
    assert isinstance(detector.is_arm(), bool)

def test_is_x86():
    assert isinstance(detector.is_x86(), bool)
