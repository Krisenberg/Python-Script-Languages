from model.models import User, SpotiClient

def get_spoti_client(user_id):
    user = User.query.filter_by(id=user_id).first()
    print(f'user id: {user.id}, user name: {user.username}')
    if user:
        spoti_client = SpotiClient.query.filter_by(user_id=user.id).first()
        print(f'spoti id: {spoti_client.id}, user name: {user.username}')
        if spoti_client:
            return spoti_client
    return None