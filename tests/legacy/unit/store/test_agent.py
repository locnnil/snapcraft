# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2017-2020 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from testtools.matchers import Equals

from snapcraft_legacy import ProjectOptions
from snapcraft_legacy import __version__ as snapcraft_version
from snapcraft_legacy.storeapi import agent
from tests.legacy import unit
from tests.legacy.fixture_setup.os_release import FakeOsRelease


class UserAgentTestCase(unit.TestCase):
    def test_user_agent_linux(self):
        self.useFixture(FakeOsRelease())

        arch = ProjectOptions().deb_arch
        expected = f"snapcraft/{snapcraft_version} Ubuntu/18.04 ({arch})"

        self.expectThat(agent.get_user_agent("linux"), Equals(expected))

    def test_user_agent_linux_unknown(self):
        self.useFixture(FakeOsRelease(name=None, version_id=None))

        arch = ProjectOptions().deb_arch
        expected = f"snapcraft/{snapcraft_version} Unknown/Unknown Version ({arch})"

        self.expectThat(agent.get_user_agent("linux"), Equals(expected))

    def test_user_agent_windows(self):
        arch = ProjectOptions().deb_arch
        expected = f"snapcraft/{snapcraft_version} Windows ({arch})"

        self.expectThat(agent.get_user_agent(platform="windows"), Equals(expected))

    def test_user_agent_darwin(self):
        arch = ProjectOptions().deb_arch
        expected = f"snapcraft/{snapcraft_version} Darwin ({arch})"

        self.expectThat(agent.get_user_agent(platform="darwin"), Equals(expected))
