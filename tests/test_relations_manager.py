import datetime
import pytest
from relations_manager import RelationsManager

@pytest.fixture
def rm():
    """Fixture to provide a fresh instance of RelationsManager for each test."""
    return RelationsManager()

def test_john_doe_is_leader_and_birthdate(rm):
    """Check if there is a team leader called John Doe whose birthdate is 31.01.1970[cite: 131]."""
    john = next((e for e in rm.get_all_employees() if e.first_name == "John" and e.last_name == "Doe"), None)
    
    assert john is not None
    assert rm.is_leader(john) is True
    assert john.birth_date == datetime.date(1970, 1, 31)

def test_john_doe_team_members(rm):
    """Check if John Doe's team members are Myrta Torkelson and Jettie Lynch[cite: 132]."""
    john = next(e for e in rm.get_all_employees() if e.id == 1)
    team_member_ids = rm.get_team_members(john)
    
    assert 2 in team_member_ids
    assert 3 in team_member_ids
    assert len(team_member_ids) == 2

def test_tomas_andre_not_in_johns_team(rm):
    """Make sure that Tomas Andre is not John Doe's team member[cite: 133]."""
    john = next(e for e in rm.get_all_employees() if e.id == 1)
    tomas = next(e for e in rm.get_all_employees() if e.first_name == "Tomas")
    
    team_member_ids = rm.get_team_members(john)
    assert tomas.id not in team_member_ids

def test_gretchen_watford_salary(rm):
    """Check if Gretchen Watford's base salary equals 4000$[cite: 134]."""
    gretchen = next(e for e in rm.get_all_employees() if e.first_name == "Gretchen" and e.last_name == "Watford")
    
    assert gretchen.base_salary == 4000

def test_tomas_andre_not_leader_and_retrieve_team(rm):
    """Make sure Tomas Andre is not a team leader. Check what happens if you try to retrieve his team members[cite: 135]."""
    tomas = next(e for e in rm.get_all_employees() if e.first_name == "Tomas" and e.last_name == "Andre")
    
    assert rm.is_leader(tomas) is False
    
    assert rm.get_team_members(tomas) is None

def test_jude_overcash_not_in_database(rm):
    """Make sure that Jude Overcash is not stored in the database[cite: 136]."""
    jude = next((e for e in rm.get_all_employees() if e.first_name == "Jude" and e.last_name == "Overcash"), None)
    
    assert jude is None