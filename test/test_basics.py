import os
import tempfile

import pytest
 
@pytest.fixture
def client():
    jothidam_test = create_app()
    db_fd, jothidam_test.app.config['DATABASE'] = tempfile.mkstemp()
    jothidam_test.app.config['TESTING'] = True
    client = jothidam_test.app.test_client()

    with jothidam_test.app.app_context():
        jothidam_test.init_db()

    yield client

    os.close(db_fd)
    os.unlink(jothidam_test.app.config['DATABASE'])