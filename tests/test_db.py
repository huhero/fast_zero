from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='cercero', email='cer@miemail.com', password='senha')
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'cer@miemail.com')
    )

    assert result.username == 'cercero'
