from django.conf import settings
import socket


def test_connection_to_db(database_name):
    try:
        db_definition = getattr(settings, 'DATABASES')[database_name]
        s = socket.create_connection(
            (db_definition['HOST'], db_definition['PORT']), 5)
        s.close()
        return True
    except:
        return False


class MasterSlaveRouter(object):
    """
    Minor master-slave router
    """
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen slave.
        """
        if test_connection_to_db('master'):
            return 'master'
        return 'slave'

    def db_for_write(self, model, **hints):
        """
        Writes always go to master.
        """
        if test_connection_to_db('master'):
            return 'master'
        return 'slave'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        db_list = ('master', 'slave')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True