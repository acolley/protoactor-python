import asyncio
from unittest.mock import Mock

from protoactor.actor.persistence import InMemoryProviderState


def test_InMemoryProviderState_get_snapshot():
    loop = asyncio.new_event_loop()
    mem_ps = InMemoryProviderState()

    snapshot = loop.run_until_complete(mem_ps.get_snapshot('test_actor_name'))

    assert snapshot is None


def test_InMemoryProviderState_get_events():
    loop = asyncio.new_event_loop()
    mem_ps = InMemoryProviderState()
    callback_m = Mock()

    loop.run_until_complete(mem_ps.get_events('test_actor_name', 0, callback_m))

    assert callback_m.called == False


def test_InMemoryProviderState_persist_event():
    loop = asyncio.new_event_loop()
    mem_ps = InMemoryProviderState()
    callback_m = Mock()
    obj = object()

    loop.run_until_complete(mem_ps.persist_event('test_actor_name', 0, obj))
    loop.run_until_complete(mem_ps.get_events('test_actor_name', 0, callback_m))

    callback_m.assert_called_once_with(obj)
