#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import shutil
from contextlib import suppress
from pathlib import Path

import pytest

import cmk.utils.paths

from cmk.core_helpers.paths import (
    ConfigPath,
    ConfigSerial,
    LATEST_CONFIG,
    LATEST_SERIAL,
    LatestConfigPath,
    VersionedConfigPath,
)


class TestConfigPath:
    @pytest.mark.parametrize("serial", (LATEST_SERIAL, LATEST_CONFIG))
    def test_from_deprecated_latest(self, serial):
        # LATEST_CONFIG is a singleton -> comparing with `is` is correct.
        assert ConfigPath.from_deprecated(serial) is LATEST_CONFIG
        assert ConfigPath.from_deprecated(str(serial)) is LATEST_CONFIG

    def test_to_deprecated_latest(self):
        assert ConfigPath.from_deprecated(LATEST_CONFIG.to_deprecated()) is LATEST_CONFIG
        assert ConfigPath.from_deprecated(LATEST_SERIAL).to_deprecated() == LATEST_SERIAL

    def test_from_deprecated_versioned(self):
        assert ConfigPath.from_deprecated(ConfigSerial("69")) == VersionedConfigPath(69)
        assert ConfigPath.from_deprecated("69") == VersionedConfigPath(69)
        assert ConfigPath.from_deprecated(VersionedConfigPath(69)) == VersionedConfigPath(69)

    def test_to_deprecated_versioned(self):
        assert (ConfigPath.from_deprecated(
            VersionedConfigPath(69).to_deprecated()) == VersionedConfigPath(69))
        assert ConfigPath.from_deprecated(ConfigSerial("69")).to_deprecated() == ConfigSerial("69")

    def test_from_deprecated_default(self):
        assert ConfigPath.from_deprecated("i don't know") is LATEST_CONFIG


class TestVersionedConfigPath:
    @pytest.fixture
    def config_path(self):
        ConfigPath.ROOT.mkdir(parents=True, exist_ok=True)
        # Call next because this is where `latest` etc. are created and updated.
        yield next(VersionedConfigPath(0))
        shutil.rmtree(ConfigPath.ROOT)

    def test_iter(self, config_path):
        for it, elem in enumerate(config_path, config_path.serial + 1):
            if it == 10:
                break
            assert elem == type(config_path)(it)

    def test_next(self, config_path):
        assert config_path == VersionedConfigPath.current() == VersionedConfigPath(1)

        config_path = next(config_path)
        assert config_path == VersionedConfigPath.current() == VersionedConfigPath(2)

        config_path = next(config_path)
        assert config_path == VersionedConfigPath.current() == VersionedConfigPath(3)

    def test_str(self, config_path):
        assert str(config_path) == str(config_path.serial)

    def test_repr(self, config_path):
        assert isinstance(repr(config_path), str)

    def test_eq(self, config_path):
        assert config_path == type(config_path)(config_path.serial)
        assert config_path != LATEST_CONFIG
        assert config_path != next(config_path)

    def test_hash(self, config_path):
        assert isinstance(hash(config_path), int)
        assert hash(config_path) == hash(type(config_path)(config_path.serial))
        assert hash(config_path) != hash(LATEST_CONFIG)
        assert hash(config_path) != hash(next(config_path))

    def test_truediv(self, config_path):
        assert config_path.serial == 1
        assert config_path / "filename" == Path("1/filename")
        assert Path("dir") / config_path == Path("dir/1")
        assert Path("dir") / config_path / "filename" == Path("dir/1/filename")

    @pytest.mark.parametrize("is_cmc", (True, False))
    def test_create_success(self, config_path, is_cmc):
        assert not config_path.helper_config_path().exists()
        assert not LATEST_CONFIG.helper_config_path().exists()

        with config_path.create(is_cmc=is_cmc):
            assert config_path.helper_config_path().exists()
            assert not LATEST_CONFIG.helper_config_path().exists()

        assert config_path.helper_config_path().exists()
        assert LATEST_CONFIG.helper_config_path().exists()
        assert (LATEST_CONFIG.helper_config_path().resolve() ==
                config_path.helper_config_path().resolve())

        next_config_path = next(config_path)
        with next_config_path.create(is_cmc=is_cmc):
            assert next_config_path.helper_config_path().exists()
            assert LATEST_CONFIG.helper_config_path().exists()
            assert (LATEST_CONFIG.helper_config_path().resolve() ==
                    config_path.helper_config_path().resolve())

        assert next_config_path.helper_config_path().exists()
        assert LATEST_CONFIG.helper_config_path().exists()
        assert (
            LATEST_CONFIG.helper_config_path().resolve() == next_config_path.helper_config_path())

    @pytest.mark.parametrize("is_cmc", (True, False))
    def test_create_no_latest_link_update_on_failure(self, config_path, is_cmc):
        assert not config_path.helper_config_path().exists()
        assert not LATEST_CONFIG.helper_config_path().exists()

        with config_path.create(is_cmc=is_cmc):
            assert config_path.helper_config_path().exists()
            assert not LATEST_CONFIG.helper_config_path().exists()

        assert config_path.helper_config_path().exists()
        assert LATEST_CONFIG.helper_config_path().exists()
        assert (LATEST_CONFIG.helper_config_path().resolve() ==
                config_path.helper_config_path().resolve())

        next_config_path = next(config_path)
        with suppress(RuntimeError), next_config_path.create(is_cmc=is_cmc):
            assert next_config_path.helper_config_path().exists()
            assert LATEST_CONFIG.helper_config_path().exists()
            assert (LATEST_CONFIG.helper_config_path().resolve() ==
                    config_path.helper_config_path().resolve())
            raise RuntimeError("boom")

        assert next_config_path.helper_config_path().exists()
        assert LATEST_CONFIG.helper_config_path().exists()
        assert (LATEST_CONFIG.helper_config_path().resolve() !=
                next_config_path.helper_config_path().resolve())
        assert (LATEST_CONFIG.helper_config_path().resolve() ==
                config_path.helper_config_path().resolve())


class TestLatestConfigPath:
    @pytest.fixture
    def config_path(self):
        yield LatestConfigPath()
        (cmk.utils.paths.core_helper_config_dir / "serial.mk").unlink(missing_ok=True)

    def test_str(self, config_path):
        assert str(config_path) == "latest"

    def test_repr(self, config_path):
        assert isinstance(repr(config_path), str)

    def test_eq(self, config_path):
        assert config_path == LATEST_CONFIG
        assert config_path == type(config_path)()
        assert config_path != VersionedConfigPath(0)

    def test_hash(self, config_path):
        assert isinstance(hash(config_path), int)
        assert hash(config_path) == hash(LATEST_CONFIG)
        assert hash(config_path) != hash(VersionedConfigPath(0))
