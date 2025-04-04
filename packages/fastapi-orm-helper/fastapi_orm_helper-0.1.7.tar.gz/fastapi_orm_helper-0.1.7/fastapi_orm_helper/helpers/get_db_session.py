from contextlib import asynccontextmanager
from typing import AsyncGenerator, Callable

from fastapi import Request
from fastapi_global_variable import GlobalVariable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
  autoflush=False,
  bind=GlobalVariable.get_or_fail('engine'),
  expire_on_commit=False,
  class_=AsyncSession,
)


SessionLocalReadOnly = sessionmaker(
  autoflush=False,
  bind=GlobalVariable.get('engine_read_only'),
  expire_on_commit=False,
  class_=AsyncSession,
)


async def get_db_session(request: Request):
  is_read_only = (
    hasattr(request, 'scope') and request.scope.get('endpoint') and hasattr(request.scope['endpoint'], 'read_only')
  )

  is_transactional = (
    hasattr(request, 'scope') and request.scope.get('endpoint') and hasattr(request.scope['endpoint'], 'transaction')
  )

  session = SessionLocalReadOnly() if is_read_only else SessionLocal()

  if is_transactional:
    setattr(session, 'transaction', True)

  try:
    yield session

    if is_transactional:
      await session.commit()
  except Exception as e:
    if is_transactional:
      await session.rollback()
    raise e
  finally:
    await session.close()


@asynccontextmanager
async def get_db_session_generator(request: Request):
  is_read_only = (
    hasattr(request, 'scope') and request.scope.get('endpoint') and hasattr(request.scope['endpoint'], 'read_only')
  )

  is_transactional = (
    hasattr(request, 'scope') and request.scope.get('endpoint') and hasattr(request.scope['endpoint'], 'transaction')
  )

  session = SessionLocalReadOnly() if is_read_only else SessionLocal()

  if is_transactional:
    setattr(session, 'transaction', True)

  try:
    yield session

    if is_transactional:
      await session.commit()
  except Exception as e:
    if is_transactional:
      await session.rollback()
    raise e
  finally:
    await session.close()


def get_db_session_factory(request: Request) -> Callable[[], AsyncGenerator[AsyncSession, None]]:
  return lambda: get_db_session_generator(request)
