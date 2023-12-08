
# import from module
from dbConnection import cursor, mydb


class Car:
    # init
    def __init__(self, id, name, model, year, color, description, user_id, status, created_at):
        self.id = id
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.description = description
        self.user_id = user_id
        self.status = status
        self.created_at = created_at

    @classmethod
    def fetch_all_cars(cls):
        sql = "SELECT * FROM cars"

        cursor.execute(sql)

        # return list of cars
        return cursor.fetchall()

    # insert single value
    def insert_into_cars(self):
        sql = "INSERT INTO cars values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (self.id,
               self.name,
               self.model,
               self.year,
               self.color,
               self.description,
               self.user_id,
               self.status,
               self.created_at)

        cursor.execute(sql, val)
        
        # effect changes
        mydb.commit()

# instantiation
car1 = Car(6, "Volvo", "Toyota", "2023-12-08", "red", "New car",
           5, "available", "2023/12/8 12:00:00")

car1.insert_into_cars()
print(car1.fetch_all_cars())
