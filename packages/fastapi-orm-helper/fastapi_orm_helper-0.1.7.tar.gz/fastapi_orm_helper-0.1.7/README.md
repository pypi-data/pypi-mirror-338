# FastAPI ORM Helper

FastAPI ORM Helper helps us to work with SQLAlchemy easier with lots of useful functions

## How to use

```python
from fastapi_orm_helper import BaseRepository
from users.entities.user import UserEntity

class UserRepository(BaseRepository[UserEntity]):
    _entity = UserEntity
```

### CRUD examples

```python
class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def create_user(self, **kwargs):
        return await self.user_repo.create(**kwargs)

    async def bulk_create_users(self, **kwargs):
        return await self.user_repo.inserts(**kwargs)

    async def first_or_create_user(self, **kwargs):
        return await self.user_repo.first_or_create(**kwargs)

    async def delete_users(self, **kwargs):
        return await self.user_repo.delete(**kwargs)

    async def get_user_by_id(self, user_id: int):
        return await self.user_repo.find_by_id(user_id)

    async def find_users(self, **kwargs):
        return await self.user_repo.order(UserEntity.created_at).find(**kwargs)

    async def first_or_fail_user(self, **kwargs):
        return await self.user_repo.first_or_fail(**kwargs)

    async def find_user(self, **kwargs):
        return await self.user_repo.joins((UserEntity.address, JoinType.LEFT_JOIN)).first(**kwargs)

    async def find_users_by_ids(self, **kwargs):
        return await self.user_repo.find_by_ids(**kwargs)

    async def count_users(self, **kwargs):
        return await self.user_repo.count(**kwargs)

    async def is_existed_user(self, **kwargs):
        return await self.user_repo.exists(**kwargs)

    async def update(self, **kwargs):
        return await self.user_repo.update(**kwargs)

    async def update_not_change_updated_at(self, **kwargs):
        return await self.user_repo.update_not_change_updated_at(**kwargs)

    async def upsert(self, **kwargs):
        return await self.user_repo.upsert(**kwargs)

    async def update_user_by_id(self, user_id: int, **kwargs):
        return await self.user_repo.update_by_id(user_id, **kwargs)
```

### query examples

#### joinedload relationships

```python
async def get_user_by_id(self, user_id: int):
    return await self.user_repo.joinedload(UserEntity.avatar).find_by_id(user_id)
```

### select_in_load relationships

```python
async def get_user_posts(self, user_id: int):
    return await self.user_repo.select_in_load(UserEntity.posts).find_by_id(user_id)
```

### load relationships

```python
_relationships = [
    joinedload(UserEntity.avatar),
    select_in_load(UserEntity.posts),
]

async def find_users(self, **kwargs):
    return await self.user_repo.load(*_relationships).find(**kwargs)
```

### scope columns in response

```python
async def get_user_email(self, user_id: int):
    return await self.user_repo.with_entities(UserEntity.email).find_by_id(user_id)
```

### paginate query
```python

class PaginationParams:
    def __init__(
        self,
        page: int = Query(default=1, ge=1),
        per_page: int = Query(default=10, ge=1, le=20),
    ):
        self.page = page
        self.per_page = per_page

async def paginate_users(self, **kwargs, pagination_params: PaginationParams):
    return await self.user_repo.order(UserEntity.created_at).paginate(**kwargs, pagination_params=pagination_params)

async def infinite_paginate_users(self, **kwargs, pagination_params: PaginationParams):
    return await self.user_repo.order(UserEntity.created_at).order_desc(UserEntity.username).infinite_paginate(**kwargs, pagination_params=pagination_params)
```

### join query

```python
async def get_user_posts(self, city: str):
    return await self.user_repo.joins(UserEntity.address).find(AddressEntity.city.ilike('%' + city + '%'))
```

### using raw sql

```python
class UserRepository(BaseRepository[UserEntity]):
    async def search_users(self, **kwargs):
        query = (
          select(
            UserEntity.id,
            func.count(
              ...
            ).label('...'),
          )
          .select_from(UserEntity)
          .outerjoin(PostEntity, PostEntity.author_id == UserEntity.id)
          .filter(*criteria)
          .group_by(UserEntity.id)
          .offset((pagination_params.page - 1) * pagination_params.per_page)
          .limit(pagination_params.per_page)
          .order_by(desc('username'))
        )
        return (await self.session.execute(query)).all()
```



