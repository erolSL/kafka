import pymysql.cursors


def db_write(table_name, value):
    connection = pymysql.connect(host='192.168.56.101',
                                 user='test',
                                 password='Qwerty1!!',
                                 database='testdb',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, 'c'+table_name[1:], value)
            # print(sql)
            cursor.execute(sql)

        connection.commit()


if __name__ == "__main__":
    # connection = pymysql.connect(host='192.168.56.101',
    #                              user='test',
    #                              password='Qwerty1!!',
    #                              database='testdb',
    #                              cursorclass=pymysql.cursors.DictCursor)
    #
    # with connection:
    #     with connection.cursor() as cursor:
    #         # Read a single record
    #         sql = "select * from tname"
    #         cursor.execute(sql)
    #         result = cursor.fetchone()
    #         print(result)
    #
    db_write('tname', 'test1')
