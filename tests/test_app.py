from http import HTTPStatus


def test_read_root_debe_return_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


def test_create_user(client):
    response = client.post(
        url='/users/',
        json={
            'username': 'testusername',
            'password': 'passuser01',
            'email': 'user01@example.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'user01@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get(
        url='/users/',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            'id': 1,
            'username': 'testusername',
            'email': 'user01@example.com',
        }
    ]


def test_read_users_by_id(client):
    response = client.get(
        url='/users/2',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}

    response = client.get(
        url='/users/1',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'user01@example.com',
    }


def test_update_users(client):
    response = client.put(
        url='/users/2',
        json={
            'username': 'testusername_upd',
            'password': 'passuser01',
            'email': 'user01_upd@example.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}

    response = client.put(
        url='/users/1',
        json={
            'username': 'testusername_upd',
            'password': 'passuser01',
            'email': 'user01_upd@example.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername_upd',
        'email': 'user01_upd@example.com',
    }


def test_delete_users(client):
    response = client.delete(
        url='/users/2',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found.'}

    response = client.delete(
        url='/users/1',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}
