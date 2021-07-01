import db

query_sql = "select * from user"
a = db.query_data(query_sql)
print(a)

insert_sql = "delete from user where user_code = 99999"
db.insert_or_update_data(insert_sql)

insert_sql = "insert into user value(99999,'David')"
db.insert_or_update_data(insert_sql)

update_sql = "update user set user_name = 'DD' where user_code = 99999"
db.insert_or_update_data(update_sql)