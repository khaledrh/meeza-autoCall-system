import sqlite3

conn = sqlite3.connect('Room.db')

c = conn.cursor()


# c.execute(
#     """CREATE TABLE rooms(
#         roomNum int,
#         EngName text,
#         ArName
#     )"""
# )

# c.execute(
#     """INSERT INTO rooms 
#        VALUES 
#               ('1','CT','مقطعية')
#               ('2','MRI', 'رنين مغناطيسي')
#               ('3','US', 'موجات صوتيه')
#               ('4','XRAY','موجات صوتيه')
#               ('5','ECHO/stress ECG', 'وحدة القلب')
#               ('EMG', 'رسم عصب')
#               ('EEG', 'رسم مخ')
#               ('DEXA', 'هشاشة عظام')
#               ('MAMO', 'وحدة الثدي')
#      """
# )


conn.commit()

conn.close()

conn2 = sqlite3.connect('patient.db')

c2 = conn2.cursor()

# c2.execute(
#     """CREATE TABLE patients (
#     patient_id INT AUTO_INCREMENT PRIMARY KEY,
#     patient_name VARCHAR(100) NOT NULL,
#     age INT,
#     gender VARCHAR(10),
#     room_id INT,
#     FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE)
#     """
# )

c2.execute(
    """INSERT INTO patient (patient_name, age, gender, room_id)
VALUES ('John Doe', 30, 'Male', 101)"""
)

c2.execute(
    """
DELETE FROM patient WHERE patient_id = 1;   
"""
)

conn2.commit()

conn2.close()

