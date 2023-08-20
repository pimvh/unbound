import testinfra


def test_unbound_running(host):
    """test that the unbound service is running"""

    with host.sudo():
        assert host.service("unbound").is_running


def test_unbound_config_created(host):
    """test that the unbound config file"""

    assert host.file("/etc/unbound/conf.d/unbound.conf")


def test_unbound_can_resolve(host):
    """test that the unbound can resolve external hosts"""

    lookup = host.run("drill @127.0.0.1 google.com")
    assert lookup.rc == 0
