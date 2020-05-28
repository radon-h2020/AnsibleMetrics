import pytest
from io import StringIO
from ansiblemetrics.playbook.num_import_playbook import NumImportPlaybook

# script_import
script_0 = "- debug:\n\tmsg: task1\n- name: This fails because I'm inside a play already"
script_2 = "- debug:\n\tmsg: play1\n\n- name: Include a play after another play\n\timport_playbook: otherplays.yaml\n- name: This fails because I'm inside a play already\n\timport_playbook: stuff.yaml"

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumImportPlaybook(script).count()
    script.close()
    assert count == expected
