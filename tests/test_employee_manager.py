import datetime
from unittest.mock import patch, MagicMock
from employee import Employee
from employee_manager import EmployeeManager

@patch('employee_manager.datetime')
def test_salary_non_leader(mock_datetime):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = False
    
    em = EmployeeManager(mock_rm)
    employee = Employee(id=99, first_name="Test", last_name="User", 
                        birth_date=datetime.date(1980, 1, 1), 
                        base_salary=1000, 
                        hire_date=datetime.date(1998, 10, 10))
    
    assert em.calculate_salary(employee) == 3000

@patch('employee_manager.datetime')
def test_salary_leader_with_3_members(mock_datetime):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = True
    mock_rm.get_team_members.return_value = [101, 102, 103] 
    
    em = EmployeeManager(mock_rm)
    leader = Employee(id=100, first_name="Jane", last_name="Doe", 
                      birth_date=datetime.date(1985, 1, 1), 
                      base_salary=2000, 
                      hire_date=datetime.date(2008, 10, 10))
    
    assert em.calculate_salary(leader) == 3600

@patch('employee_manager.datetime')
@patch('builtins.print')
def test_calculate_salary_and_send_email(mock_print, mock_datetime):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = True
    mock_rm.get_team_members.return_value = [101, 102, 103]
    
    em = EmployeeManager(mock_rm)
    leader = Employee(id=100, first_name="Jane", last_name="Doe", 
                      birth_date=datetime.date(1985, 1, 1), 
                      base_salary=2000, 
                      hire_date=datetime.date(2008, 10, 10))
    
    em.calculate_salary_and_send_email(leader)
    
    expected_message = "Jane Doe your salary: 3600 has been transferred to you."
    
    mock_print.assert_called_once_with(expected_message)