import brownie


def test_release_management(gov, registry, create_vault):
    # No deployments yet
    with brownie.reverts():
        registry.latestRelease()

    # Creating a new release updates the previous
    v1_vault = create_vault(version="1.0.0")
    registry.newRelease(v1_vault, {"from": gov})
    assert registry.latestRelease() == v1_vault

    # Can't release same vault twice
    with brownie.reverts():
        registry.newRelease(v1_vault, {"from": gov})

    # New release overrides previous
    v2_vault = create_vault(version="2.0.0")
    registry.newRelease(v2_vault, {"from": gov})
    assert registry.latestRelease() == v2_vault
