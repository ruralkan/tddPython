import pytest
import tasks
@pytest.mark.smoke
def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):

        """statement says that whatever is in the next block of code should
        raise a TypeError exception. If no exception is raised, the test fails. 
        If the test raises a different exception, it fails."""

        tasks.add(task='not a Task object')

@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


""" also check the parameters to the exception. For start_tasks_db(db_path, db_type), not only does db_type need
to be a string, it really has to be either ’tiny’ or ’mongo’ 
You can check to make sure the exception message is correct by adding as excinfo"""
def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception.
    The variable name you put after as (excinfo in this case)
    is filled with information about the exception, and is of type ExceptionInfo."""

    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"